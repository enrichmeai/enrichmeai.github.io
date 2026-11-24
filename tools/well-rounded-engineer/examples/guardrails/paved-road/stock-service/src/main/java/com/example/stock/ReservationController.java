package com.example.stock;

import jakarta.validation.Valid;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import java.net.URI;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/reservations")
public class ReservationController {

    public record ReserveRequest(@NotBlank String sku, @Min(1) @Max(100) int quantity) {}  // AC-6

    private final ReservationService service;

    public ReservationController(ReservationService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ReservationService.Reservation> reserve(
            @RequestHeader("Idempotency-Key") String key, @Valid @RequestBody ReserveRequest body) {
        var r = service.reserve(body.sku(), body.quantity(), key);
        var status = r.replayed() ? HttpStatus.OK : HttpStatus.CREATED;
        return ResponseEntity.status(status).location(URI.create("/reservations/" + r.id())).body(r);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> release(@PathVariable String id) {
        service.release(id);
        return ResponseEntity.noContent().build();   // the same answer the second time (AC-5)
    }
    // No error handlers here: the platform starter maps every DomainException to a problem detail.
}
