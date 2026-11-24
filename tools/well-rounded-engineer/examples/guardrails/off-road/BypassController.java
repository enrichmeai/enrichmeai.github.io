package com.example.stock;

import org.springframework.http.HttpStatus;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

/** The quieter shortcuts: JdbcTemplate instead of JdbcClient, and a controller-local handler. */
@RestController
class BypassController {
    private final JdbcTemplate jdbc;
    BypassController(JdbcTemplate jdbc) { this.jdbc = jdbc; }

    @GetMapping("/stock-count")
    Integer count() { return jdbc.queryForObject("SELECT COUNT(*) FROM stock", Integer.class); }

    @ExceptionHandler(IllegalStateException.class)
    String oops() { return "oops"; }
}
