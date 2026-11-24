package com.example.stock;

import java.util.Optional;
import java.util.UUID;
import com.example.platform.DomainException;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.http.HttpStatus;
import org.springframework.jdbc.core.simple.JdbcClient;
import org.springframework.stereotype.Service;
import org.springframework.transaction.support.TransactionTemplate;

/** Spec 001. All state is in the database (NFR-1), so any number of instances can run. */
@Service
public class ReservationService {

    public record Reservation(String id, String sku, int quantity, boolean replayed) {}

    public static class InsufficientStock extends DomainException {
        InsufficientStock() { super(HttpStatus.CONFLICT, "INSUFFICIENT_STOCK", "Not enough stock for this sku"); }
    }

    public static class KeyReused extends DomainException {
        KeyReused() { super(HttpStatus.UNPROCESSABLE_CONTENT, "IDEMPOTENCY_KEY_REUSED", "This Idempotency-Key was used for a different request"); }
    }

    public static class UnknownSku extends DomainException {
        UnknownSku() { super(HttpStatus.NOT_FOUND, "UNKNOWN_SKU", "No such sku"); }
    }

    private final JdbcClient db;
    private final TransactionTemplate tx;

    public ReservationService(JdbcClient db, TransactionTemplate tx) {
        this.db = db;
        this.tx = tx;
    }

    public Reservation reserve(String sku, int quantity, String idempotencyKey) {
        try {
            return tx.execute(status -> {
                Optional<Reservation> earlier = findByKey(idempotencyKey);      // AC-3: a plain retry
                if (earlier.isPresent()) return sameRequest(earlier.get(), sku, quantity);
                boolean known = db.sql("SELECT COUNT(*) FROM stock WHERE sku = :sku").param("sku", sku)
                        .query(Integer.class).single() > 0;
                if (!known) throw new UnknownSku();                           // AC-8
                String id = UUID.randomUUID().toString();
                // Claim the key FIRST. A second request with the same key, on any instance, now waits
                // on the unique index until this transaction ends, instead of racing for the stock.
                db.sql("""
                        INSERT INTO reservation (id, idempotency_key, sku, quantity, released)
                        VALUES (:id, :key, :sku, :q, FALSE)""")
                        .param("id", id).param("key", idempotencyKey)
                        .param("sku", sku).param("q", quantity).update();
                int changed = db.sql("""
                        UPDATE stock SET available = available - :q
                        WHERE sku = :sku AND available >= :q""")              // AC-2, AC-4: one conditional UPDATE
                        .param("q", quantity).param("sku", sku).update();
                if (changed == 0) throw new InsufficientStock();             // rolls back the INSERT too
                return new Reservation(id, sku, quantity, false);
            });
        } catch (DuplicateKeyException sameKeyAtSameTime) {
            // The same key arrived twice at once. The first one committed; answer with its reservation.
            return sameRequest(findByKey(idempotencyKey).orElseThrow(), sku, quantity);
        }
    }

    /** AC-7: a key reused for a different request is refused, never answered with the old result. */
    private Reservation sameRequest(Reservation earlier, String sku, int quantity) {
        if (!earlier.sku().equals(sku) || earlier.quantity() != quantity) throw new KeyReused();
        return earlier;
    }

    /** AC-5: returns stock once. A second release finds released = TRUE and changes nothing. */
    public boolean release(String id) {
        return Boolean.TRUE.equals(tx.execute(status -> {
            var row = db.sql("""
                    SELECT sku, quantity FROM reservation WHERE id = :id AND released = FALSE FOR UPDATE""")
                    .param("id", id).query((rs, n) -> new Object[] {rs.getString(1), rs.getInt(2)})
                    .optional();
            if (row.isEmpty()) return false;
            db.sql("UPDATE reservation SET released = TRUE WHERE id = :id").param("id", id).update();
            db.sql("UPDATE stock SET available = available + :q WHERE sku = :sku")
                    .param("q", row.get()[1]).param("sku", row.get()[0]).update();
            return true;
        }));
    }

    public int available(String sku) {
        return db.sql("SELECT available FROM stock WHERE sku = :sku").param("sku", sku)
                .query(Integer.class).single();
    }

    private Optional<Reservation> findByKey(String key) {
        return db.sql("SELECT id, sku, quantity FROM reservation WHERE idempotency_key = :key")
                .param("key", key)
                .query((rs, n) -> new Reservation(rs.getString(1), rs.getString(2), rs.getInt(3), true))
                .optional();
    }
}
