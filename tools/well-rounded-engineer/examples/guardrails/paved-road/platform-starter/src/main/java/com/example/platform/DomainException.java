package com.example.platform;

import org.springframework.http.HttpStatus;

/** Every service error the client should see extends this. The platform turns it into a problem detail. */
public abstract class DomainException extends RuntimeException {
    private final HttpStatus status;
    private final String code;

    protected DomainException(HttpStatus status, String code, String detail) {
        super(detail);
        this.status = status;
        this.code = code;
    }

    public HttpStatus status() { return status; }
    public String code() { return code; }
}
