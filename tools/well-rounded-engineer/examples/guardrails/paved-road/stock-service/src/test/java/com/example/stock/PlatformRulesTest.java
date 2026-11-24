package com.example.stock;

import com.example.platform.PlatformRules;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import org.junit.jupiter.api.Test;

/** The platform's standards, checked on this service's own classes in every build. */
class PlatformRulesTest {
    @Test
    void thisServiceFollowsThePlatformRules() {
        PlatformRules.check(new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.example.stock"));
    }
}
