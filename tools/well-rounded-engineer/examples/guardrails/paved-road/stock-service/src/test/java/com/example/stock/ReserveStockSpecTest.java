package com.example.stock;

import static org.assertj.core.api.Assertions.assertThat;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.UUID;
import java.util.concurrent.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.env.Environment;
import org.springframework.jdbc.core.simple.JdbcClient;

/** One test per acceptance criterion in specs/001-reserve-stock/spec.md, tagged with its id. */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ReserveStockSpecTest {

    @Autowired Environment env;
    @Autowired JdbcClient db;
    @Autowired ReservationService service;
    final HttpClient http = HttpClient.newHttpClient();

    @BeforeEach
    void clean() {
        db.sql("DELETE FROM reservation").update();
        db.sql("DELETE FROM stock").update();
    }

    void stock(String sku, int n) {
        db.sql("INSERT INTO stock (sku, available) VALUES (:s, :n)").param("s", sku).param("n", n).update();
    }

    HttpResponse<String> reserve(String sku, int qty, String key) throws Exception {
        var req = HttpRequest.newBuilder(URI.create("http://localhost:" + env.getProperty("local.server.port") + "/reservations"))
                .header("Content-Type", "application/json").header("Idempotency-Key", key)
                .POST(HttpRequest.BodyPublishers.ofString("{\"sku\":\"" + sku + "\",\"quantity\":" + qty + "}"))
                .build();
        return http.send(req, HttpResponse.BodyHandlers.ofString());
    }

    @Test @Tag("AC-1")
    void reservingFromEnoughStockLeavesTheRest() throws Exception {
        stock("A", 5);
        var r = reserve("A", 2, "k1");
        assertThat(r.statusCode()).isEqualTo(201);
        assertThat(r.body()).contains("\"id\"");
        assertThat(service.available("A")).isEqualTo(3);
    }

    @Test @Tag("AC-2")
    void notEnoughStockIs409AndChangesNothing() throws Exception {
        stock("A", 1);
        var r = reserve("A", 2, "k2");
        assertThat(r.statusCode()).isEqualTo(409);
        assertThat(r.body()).contains("INSUFFICIENT_STOCK");
        assertThat(service.available("A")).isEqualTo(1);
    }

    @Test @Tag("AC-3")
    void aRetryWithTheSameKeyReturnsTheSameReservation() throws Exception {
        stock("A", 5);
        var first = service.reserve("A", 2, "k3");
        var retry = service.reserve("A", 2, "k3");
        assertThat(retry.id()).isEqualTo(first.id());
        assertThat(service.available("A")).isEqualTo(3);
        assertThat(reserve("A", 2, "k3").statusCode()).isEqualTo(200);
    }

    @Test @Tag("AC-3")
    void theSameKeySentTwiceAtOnceReservesOnce() throws Exception {
        for (int round = 0; round < 30; round++) {          // a race: repeat it so a lucky order cannot pass
            clean();
            stock("A", 1);                                    // the last unit: the case that used to fail
            String key = "race-" + round;
            var start = new CountDownLatch(1);
            try (ExecutorService pool = Executors.newFixedThreadPool(2)) {
                Callable<ReservationService.Reservation> call = () -> { start.await(); return service.reserve("A", 1, key); };
                var a = pool.submit(call);
                var b = pool.submit(call);
                start.countDown();
                assertThat(a.get().id()).isEqualTo(b.get().id());
            }
            assertThat(service.available("A")).isZero();
        }
    }

    @Test @Tag("AC-4")
    void twentyRacersForTheLastUnitExactlyOneWins() throws Exception {
        stock("A", 1);
        var start = new CountDownLatch(1);
        try (ExecutorService pool = Executors.newFixedThreadPool(20)) {
            var results = new java.util.ArrayList<Future<Integer>>();
            for (int i = 0; i < 20; i++) {
                results.add(pool.submit(() -> { start.await(); return reserve("A", 1, UUID.randomUUID().toString()).statusCode(); }));
            }
            start.countDown();
            int won = 0;
            for (var f : results) if (f.get() == 201) won++;
            assertThat(won).isEqualTo(1);
        }
        assertThat(service.available("A")).isZero();
    }

    @Test @Tag("AC-5")
    void releasingReturnsStockOnce() throws Exception {
        stock("A", 5);
        var r = service.reserve("A", 2, "k5");
        for (int i = 0; i < 2; i++) {                         // the second DELETE must change nothing
            var req = HttpRequest.newBuilder(URI.create("http://localhost:" + env.getProperty("local.server.port") + "/reservations/" + r.id()))
                    .DELETE().build();
            assertThat(http.send(req, HttpResponse.BodyHandlers.ofString()).statusCode()).isEqualTo(204);
        }
        assertThat(service.available("A")).isEqualTo(5);
    }

    @Test @Tag("AC-6")
    void quantityOutsideOneToHundredIs400() throws Exception {
        stock("A", 500);
        assertThat(reserve("A", 0, "k6a").statusCode()).isEqualTo(400);
        assertThat(reserve("A", 101, "k6b").statusCode()).isEqualTo(400);
        assertThat(service.available("A")).isEqualTo(500);
    }

    @Test @Tag("AC-7")
    void aKeyReusedForADifferentRequestIs422() throws Exception {
        stock("A", 5);
        stock("B", 5);
        assertThat(reserve("A", 2, "k7").statusCode()).isEqualTo(201);
        var r = reserve("B", 2, "k7");
        assertThat(r.statusCode()).isEqualTo(422);
        assertThat(r.body()).contains("IDEMPOTENCY_KEY_REUSED");
        assertThat(reserve("A", 3, "k7").statusCode()).isEqualTo(422);
        assertThat(service.available("A")).isEqualTo(3);
        assertThat(service.available("B")).isEqualTo(5);
    }

    @Test @Tag("AC-8")
    void anUnknownSkuIs404() throws Exception {
        var r = reserve("Z", 1, "k8");
        assertThat(r.statusCode()).isEqualTo(404);
        assertThat(r.body()).contains("UNKNOWN_SKU");
    }
}
