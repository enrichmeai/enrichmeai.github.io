package com.example.platform;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noMethods;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.lang.ArchRule;
import com.tngtech.archunit.lang.CompositeArchRule;
import com.tngtech.archunit.library.GeneralCodingRules;
import java.util.List;

/** The standards every service shares, as tests. Owned by the platform team; agents and people meet the same rules. */
public final class PlatformRules {

    public static final ArchRule CONTROLLERS_DO_NOT_TOUCH_THE_DATABASE =
            noClasses().that().areAnnotatedWith(org.springframework.web.bind.annotation.RestController.class)
                    .or().areAnnotatedWith(org.springframework.stereotype.Controller.class)
                    .should().dependOnClassesThat().resideInAnyPackage("org.springframework.jdbc..", "org.springframework.data..", "jakarta.persistence..", "javax.sql..")
                    .because("data access belongs in a service, where transactions are");

    public static final ArchRule SERVICE_EXCEPTIONS_GO_THROUGH_THE_PLATFORM =
            classes().that().areAssignableTo(RuntimeException.class).and().resideOutsideOfPackage("com.example.platform..")
                    .and().areNotAnnotatedWith(NotClientFacing.class)
                    .should().beAssignableTo(DomainException.class)
                    .because("one error format for every service; mark internal-only exceptions @NotClientFacing");

    public static final ArchRule NO_OWN_ERROR_HANDLERS =
            noClasses().that().resideOutsideOfPackage("com.example.platform..")
                    .should().beAnnotatedWith(org.springframework.web.bind.annotation.RestControllerAdvice.class)
                    .orShould().beAnnotatedWith(org.springframework.web.bind.annotation.ControllerAdvice.class)
                    .because("the platform already maps errors; a second handler drifts");

    public static final ArchRule NO_LOCAL_EXCEPTION_HANDLERS =
            noMethods().that().areDeclaredInClassesThat().resideOutsideOfPackage("com.example.platform..")
                    .should().beAnnotatedWith(org.springframework.web.bind.annotation.ExceptionHandler.class)
                    .because("the platform already maps errors; a second handler drifts");

    public static final List<ArchRule> ALL = List.of(
            CONTROLLERS_DO_NOT_TOUCH_THE_DATABASE,
            SERVICE_EXCEPTIONS_GO_THROUGH_THE_PLATFORM,
            NO_OWN_ERROR_HANDLERS,
            NO_LOCAL_EXCEPTION_HANDLERS,
            GeneralCodingRules.NO_CLASSES_SHOULD_ACCESS_STANDARD_STREAMS);

    /** Checks every rule and reports every violation at once, so a reviewer (person or agent) sees them all. */
    public static void check(JavaClasses service) {
        CompositeArchRule.of(ALL).check(service);
    }

    private PlatformRules() {}
}
