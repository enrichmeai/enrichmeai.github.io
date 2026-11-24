package com.example.platform;

import org.springframework.http.ProblemDetail;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/** One error format for every service: RFC 9457 problem details with a stable code. */
@RestControllerAdvice
public class PlatformErrors {
    @ExceptionHandler(DomainException.class)
    ProblemDetail domain(DomainException e) {
        var p = ProblemDetail.forStatusAndDetail(e.status(), e.getMessage());
        p.setProperty("code", e.code());
        return p;
    }
}
