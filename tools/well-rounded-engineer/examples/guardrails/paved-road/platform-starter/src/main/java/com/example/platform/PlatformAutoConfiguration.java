package com.example.platform;

import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.context.annotation.Import;

/** Switched on in every service that depends on the starter: no copy-paste, one place to fix. */
@AutoConfiguration
@Import(PlatformErrors.class)
public class PlatformAutoConfiguration {}
