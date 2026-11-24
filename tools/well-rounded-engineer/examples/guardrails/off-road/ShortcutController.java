package com.example.stock;

import org.springframework.http.HttpStatus;
import org.springframework.http.ProblemDetail;
import org.springframework.jdbc.core.simple.JdbcClient;
import org.springframework.web.bind.annotation.*;

/** What a model might write when asked for "a quick endpoint to list stock". */
@RestController
@RestControllerAdvice
class ShortcutController {
    private final JdbcClient db;
    ShortcutController(JdbcClient db) { this.db = db; }

    static class NotFound extends RuntimeException {}

    @GetMapping("/stock/{sku}")
    Integer available(@PathVariable String sku) {
        System.out.println("looking up " + sku);
        return db.sql("SELECT available FROM stock WHERE sku = :sku").param("sku", sku).query(Integer.class).single();
    }

    @ExceptionHandler(NotFound.class)
    ProblemDetail notFound() { return ProblemDetail.forStatus(HttpStatus.NOT_FOUND); }
}
