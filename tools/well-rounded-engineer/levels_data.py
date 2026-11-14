# Per tab: levels F/P/S/E (lists of bullets), study-next topics, links (title, url, note)
D = {}

D["linux"] = dict(
 F=["Navigate, read and search files and logs","Run, stop and inspect processes","Understand permissions well enough to fix 'permission denied'"],
 P=["Write safe bash scripts with set -euo pipefail, traps and quoting","Diagnose disk, memory and CPU problems with df, free, top, dmesg","Manage services with systemd and read journalctl"],
 S=["Tune a host or container for a workload (file limits, memory, I/O)","Debug with strace, lsof and tcpdump","Decide when a script should become a real program"],
 E=["Understand kernel mechanisms behind containers (namespaces, cgroups)","Set the team's base images and hardening standards","Lead performance investigations end to end"],
 topics=["cgroups and namespaces: what a container really is","strace, perf and eBPF tools for tracing","File descriptors, signals and process lifecycle","Shell portability: bash vs POSIX sh","Log rotation and journald retention"],
 links=[("The Linux Command Line (free book)","https://linuxcommand.org/tlcl.php","A full beginner-to-practitioner course"),
        ("Linux man pages","https://man7.org/linux/man-pages/","Authoritative reference for every command and syscall"),
        ("GNU Bash manual","https://www.gnu.org/software/bash/manual/","Expansion, quoting and builtins in detail"),
        ("ShellCheck","https://www.shellcheck.net/","Lints shell scripts and explains each warning"),
        ("systemd documentation","https://systemd.io/","Units, timers, journald"),
        ("Wizard Zines (Julia Evans)","https://wizardzines.com/","Short illustrated guides to Linux, networking and debugging")])

D["networking"] = dict(
 F=["Explain IP, port, DNS, TCP vs UDP and HTTP status classes","Use curl, dig and nc to test reachability","Tell a DNS failure from a refusal from a timeout"],
 P=["Size subnets with CIDR; read firewall rules and routes","Debug TLS and certificate errors","Configure private access, NAT and egress for cloud workloads"],
 S=["Design a VPC: ranges, subnets, private service access, load balancers","Choose L4 vs L7 load balancing and set health checks","Trace a latency problem across the network path"],
 E=["Design hybrid and multi-region connectivity","Set network security policy for an organisation","Lead incident response for network-level outages"],
 topics=["TCP handshake, congestion control and keep-alive","TLS 1.3 handshake and certificate chains","HTTP/2 and HTTP/3 (QUIC)","Anycast, global load balancing and CDNs","VPC Service Controls and Private Service Connect"],
 links=[("High Performance Browser Networking (free book)","https://hpbn.co/","TCP, TLS, HTTP/2 explained for engineers"),
        ("MDN: HTTP","https://developer.mozilla.org/en-US/docs/Web/HTTP","Methods, headers, caching, CORS"),
        ("Cloudflare Learning Center","https://www.cloudflare.com/learning/","Clear explainers on DNS, TLS, CDN, DDoS"),
        ("Google Cloud VPC overview","https://cloud.google.com/vpc/docs/overview","Networks, subnets, firewall, routes on GCP"),
        ("Cloud Load Balancing overview","https://cloud.google.com/load-balancing/docs/load-balancing-overview","Which load balancer for which job")])

D["docker"] = dict(
 F=["Build, run, stop and inspect containers","Read a Dockerfile and explain each instruction","Use docker compose for a local stack"],
 P=["Write small multi-stage Dockerfiles with good layer caching","Run as non-root; keep secrets out of layers","Build for linux/amd64; debug exit codes and OOM kills"],
 S=["Set image standards: base images, scanning, SBOMs, signing","Optimise image size and startup time for Cloud Run or Kubernetes","Design local development environments for a team"],
 E=["Own the organisation's container supply chain","Understand the OCI image and runtime specs","Choose and govern registries, build systems and policies"],
 topics=["BuildKit cache mounts and secrets","Distroless and minimal base images","OCI image format and digests","Rootless containers","Image signing with cosign and SLSA provenance"],
 links=[("Docker documentation","https://docs.docker.com/","Official docs for engine, build and compose"),
        ("Dockerfile best practices","https://docs.docker.com/build/building/best-practices/","Caching, multi-stage, small images"),
        ("Docker Compose","https://docs.docker.com/compose/","Multi-container local stacks"),
        ("Distroless images","https://github.com/GoogleContainerTools/distroless","Minimal runtime images from Google"),
        ("Trivy","https://trivy.dev/","Scan images and dependencies for CVEs")])

D["sql"] = dict(
 F=["SELECT, WHERE, GROUP BY, ORDER BY and simple joins","Know how NULL behaves in comparisons and aggregates","Dry-run before running in BigQuery"],
 P=["Window functions, QUALIFY, CTEs, semi- and anti-joins","Check grain and fan-out before trusting a number","Write readable, tested SQL in dbt"],
 S=["Patterns: gaps and islands, spines, SCD joins, recursion","Read execution plans and cut cost and slot time","Review others' SQL for correctness and cost"],
 E=["Design query patterns and models for a whole platform","Teach SQL; set standards and linting","Know engine internals well enough to predict plans"],
 topics=["Logical vs physical query plans","Approximate aggregation (HyperLogLog, quantiles)","Pipe syntax and modern SQL features","SQL style guides and SQLFluff linting","Testing SQL with dbt unit tests"],
 links=[("BigQuery query syntax","https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax","The full GoogleSQL SELECT reference"),
        ("Modern SQL","https://modern-sql.com/","Window functions, recursion and newer standard features across engines"),
        ("Use The Index, Luke","https://use-the-index-luke.com/","How queries and indexes really interact"),
        ("PostgreSQL tutorial: window functions","https://www.postgresql.org/docs/current/tutorial-window.html","A clear introduction to windows"),
        ("SQLFluff","https://docs.sqlfluff.com/","Linter and formatter for SQL, including dbt and BigQuery")])

D["database"] = dict(
 F=["Design a normalised table with a primary key and constraints","Add an index for a slow lookup","Understand what a transaction guarantees"],
 P=["Read EXPLAIN ANALYZE and fix the plan","Choose composite, partial and covering indexes","Write safe, additive migrations"],
 S=["Partition large tables; plan retention and archiving","Choose isolation levels and locking strategies","Plan replicas, pooling and capacity"],
 E=["Decide between scaling up, partitioning, sharding or a distributed database","Run zero-downtime migrations on very large tables","Set database standards and review all schema changes"],
 topics=["MVCC and vacuum in Postgres","B-tree internals and index-only scans","Logical replication and change data capture","Isolation anomalies: write skew, phantom reads","Distributed SQL: Spanner, CockroachDB, Citus"],
 links=[("PostgreSQL documentation","https://www.postgresql.org/docs/current/","The reference for everything Postgres"),
        ("Postgres: table partitioning","https://www.postgresql.org/docs/current/ddl-partitioning.html","Range, list, hash partitions and pruning"),
        ("Postgres: transaction isolation","https://www.postgresql.org/docs/current/transaction-iso.html","What each level allows"),
        ("Use The Index, Luke","https://use-the-index-luke.com/","Indexing explained for developers"),
        ("Designing Data-Intensive Applications","https://dataintensive.net/","The standard book on storage, replication and partitioning"),
        ("explain.dalibo.com","https://explain.dalibo.com/","Visualise Postgres query plans")])

D["java"] = dict(
 F=["Write classes, records, collections and streams","Use Optional and java.time correctly","Run and write JUnit tests"],
 P=["Use modern features (records, sealed types, pattern switch, virtual threads)","Handle concurrency safely with executors and CompletableFuture","Build with Gradle or Maven and manage dependencies"],
 S=["Tune the JVM for containers (memory, GC, startup)","Design APIs and module boundaries","Profile and fix performance problems"],
 E=["Lead platform upgrades across LTS releases","Understand JVM internals (JIT, GC, class loading)","Set the organisation's Java standards and libraries"],
 topics=["JEPs for each release since 17","Garbage collectors: G1, ZGC, Shenandoah","Java Flight Recorder and JDK Mission Control","Structured concurrency and scoped values","GraalVM native image and AOT caches"],
 links=[("dev.java: Learn","https://dev.java/learn/","Oracle's official tutorials for modern Java"),
        ("OpenJDK JEP index","https://openjdk.org/jeps/0","Every enhancement proposal, with status and release"),
        ("JDK project releases","https://openjdk.org/projects/jdk/","What shipped in each JDK version"),
        ("JUnit 5 user guide","https://junit.org/junit5/docs/current/user-guide/","Tests, parameterised tests, extensions"),
        ("BigQuery Java client","https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview","API reference"),
        ("Apache Beam documentation","https://beam.apache.org/documentation/","Programming guide for Dataflow pipelines")])

D["python"] = dict(
 F=["Write functions, comprehensions and dataclasses","Use virtual environments and install packages","Write simple pytest tests"],
 P=["Type hints, logging, error handling and context managers","Use the BigQuery and GCS clients in pipelines","Package a project with pyproject.toml"],
 S=["Choose between threads, processes and asyncio","Design reusable libraries with clear APIs and tests","Profile memory and CPU; optimise data handling"],
 E=["Understand CPython internals, the GIL and free-threading","Own the organisation's Python tooling and packaging","Mentor and set code standards"],
 topics=["Typing: generics, Protocols, mypy or pyright","asyncio internals and TaskGroups","Packaging: wheels, lockfiles, uv","Free-threaded CPython (3.13+)","Data libraries: pandas, Polars, PyArrow"],
 links=[("Python documentation","https://docs.python.org/3/","Language and standard library reference"),
        ("What's new in Python","https://docs.python.org/3/whatsnew/index.html","Changes in each release"),
        ("PEP 8 style guide","https://peps.python.org/pep-0008/","Conventions for readable Python"),
        ("pytest documentation","https://docs.pytest.org/en/stable/","Fixtures, parametrize, plugins"),
        ("uv","https://docs.astral.sh/uv/","Fast package and project manager"),
        ("BigQuery Python client","https://cloud.google.com/python/docs/reference/bigquery/latest","API reference")])

D["testing"] = dict(
 F=["Write unit tests with clear arrange-act-assert","Run the suite locally and read CI failures","Reproduce a bug with a failing test before fixing it"],
 P=["Use Testcontainers and WireMock for integration tests","Test edge cases, errors and dependency failures","Keep tests fast, independent and deterministic"],
 S=["Design a test strategy across unit, integration, contract and end to end","Add property-based, load and mutation testing where they pay off","Eliminate flaky tests and slow suites"],
 E=["Set testing standards and quality gates for the organisation","Build test infrastructure: environments, data, emulators","Measure test effectiveness, not just coverage"],
 topics=["Contract testing with Pact","Mutation testing with PIT or mutmut","Test data management and synthetic data","Testing in production: canaries and feature flags","Chaos engineering"],
 links=[("The Practical Test Pyramid (Martin Fowler)","https://martinfowler.com/articles/practical-test-pyramid.html","How to balance test levels"),
        ("JUnit 5 user guide","https://junit.org/junit5/docs/current/user-guide/","Java testing"),
        ("pytest documentation","https://docs.pytest.org/en/stable/","Python testing"),
        ("Testcontainers","https://testcontainers.com/","Real dependencies in Docker for tests"),
        ("WireMock","https://wiremock.org/docs/","HTTP stubs and recording"),
        ("Hypothesis","https://hypothesis.readthedocs.io/","Property-based testing in Python"),
        ("Grafana k6","https://grafana.com/docs/k6/latest/","Load testing"),
        ("PIT mutation testing","https://pitest.org/","Measure test strength in Java")])

D["security"] = dict(
 F=["Spot phishing; use a password manager and passkeys","Parameterise every query; never commit secrets","Check that users can only reach their own data","Apply the PR security checklist"],
 P=["Hash passwords correctly and run containers to the Restricted profile","Implement OAuth 2.0 / OIDC with a provider and validate tokens properly","Use least-privilege IAM and a secret manager","Fix findings from SAST, SCA and image scans"],
 S=["Threat-model a system and turn threats into tests","Design authentication, authorisation and audit for a product","Respond to and contain a security incident"],
 E=["Own the security architecture and policies across teams","Lead compliance (DPDP, GDPR, SOC 2) and external testing","Build a security culture and secure-by-default platforms"],
 topics=["OWASP ASVS verification levels","OAuth 2.0 security best current practice","Supply-chain security with SLSA","Cloud security posture management","LLM and AI application security"],
 links=[("OWASP Top 10","https://owasp.org/www-project-top-ten/","Most critical web application risks"),
        ("OWASP GenAI LLM Top 10 (2026)","https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/","Risks for applications built on language models"),
        ("OWASP Password Storage Cheat Sheet","https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html","Argon2id, scrypt, bcrypt and PBKDF2 settings"),
        ("Kubernetes Pod Security Standards","https://kubernetes.io/docs/concepts/security/pod-security-standards/","Privileged, Baseline and Restricted profiles"),
        ("OWASP Cheat Sheet Series","https://cheatsheetseries.owasp.org/","Concise how-tos for each security topic"),
        ("OWASP API Security Top 10","https://owasp.org/www-project-api-security/","Risks specific to APIs"),
        ("OWASP ASVS","https://owasp.org/www-project-application-security-verification-standard/","A checklist of security requirements by level"),
        ("Spring Security reference","https://docs.spring.io/spring-security/reference/","Authentication and authorisation in Spring"),
        ("Google Cloud security best practices","https://cloud.google.com/security/best-practices","IAM, network and data protection on GCP"),
        ("SLSA","https://slsa.dev/","Supply-chain levels for software artefacts")])

D["data"] = dict(
 F=["Explain the lifecycle and the layers","Load a file into a warehouse and query it","Write a simple, idempotent transformation"],
 P=["Build incremental, tested pipelines end to end","Choose batch vs streaming and ingestion patterns","Model data at a stated grain with keys and tests"],
 S=["Design a data platform: layers, contracts, orchestration, observability","Own data quality and reconciliation across sources","Plan cost, retention and governance"],
 E=["Set data architecture and standards across the organisation","Lead migrations between platforms without losing trust","Shape data products and their contracts with consumers"],
 topics=["Dimensional modelling (Kimball)","Data contracts and schema evolution","Open table formats: Iceberg, Delta","Change data capture","Data observability and lineage"],
 links=[("Fundamentals of Data Engineering (book)","https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/","Reis &amp; Housley: the lifecycle and its undercurrents"),
        ("Designing Data-Intensive Applications","https://dataintensive.net/","Storage, replication, batch and stream processing"),
        ("Kimball dimensional modelling techniques","https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/","Facts, dimensions, SCDs"),
        ("dbt best practices","https://docs.getdbt.com/best-practices","How to structure a transformation project"),
        ("Google Cloud Architecture Center","https://cloud.google.com/architecture","Reference architectures for data on GCP"),
        ("Apache Iceberg","https://iceberg.apache.org/","Open table format for lakehouses")])

D["bigquery"] = dict(
 F=["Query with named columns and partition filters","Dry-run and read bytes processed","Load data from GCS"],
 P=["Design partitioned and clustered tables","Write MERGE, scripting and parameterised queries","Use INFORMATION_SCHEMA to find cost and usage"],
 S=["Optimise slot time and cost across a project","Choose pricing models and reservations","Design security: datasets, authorised views, row and column policies"],
 E=["Own the warehouse platform and its cost governance","Integrate BigQuery with streaming, ML and the wider lakehouse","Advise on architecture across many teams"],
 topics=["Storage Write API and streaming","Editions, reservations and autoscaling","Row-level security and policy tags","BigLake and external tables","BigQuery ML and vector search"],
 links=[("BigQuery documentation","https://cloud.google.com/bigquery/docs","Official docs"),
        ("Query performance best practices","https://cloud.google.com/bigquery/docs/best-practices-performance-overview","Reduce bytes and slot time"),
        ("Functions and operators","https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators","Every GoogleSQL function"),
        ("Partitioned tables","https://cloud.google.com/bigquery/docs/partitioned-tables","Types, limits and pruning"),
        ("INFORMATION_SCHEMA","https://cloud.google.com/bigquery/docs/information-schema-intro","Metadata and job history views"),
        ("BigQuery pricing","https://cloud.google.com/bigquery/pricing","On-demand and capacity pricing")])

D["dbt"] = dict(
 F=["Run, test and select models; read compiled SQL","Use ref and source; add not_null and unique tests","Understand views vs tables"],
 P=["Write incremental models with the right strategy","Write macros, generic tests and unit tests","Configure partitioning and clustering on BigQuery"],
 S=["Structure a multi-project dbt platform","Set up slim CI with state and defer","Use contracts, versions and access controls for shared models"],
 E=["Own modelling standards across the organisation","Design cross-project dependencies and data mesh boundaries","Contribute packages and tooling"],
 topics=["Model contracts and versions","Microbatch incremental models","dbt packages: dbt_utils, dbt_expectations","Semantic layer and metrics","Exposures and documentation"],
 links=[("dbt documentation","https://docs.getdbt.com/docs/introduction","Official docs"),
        ("dbt reference","https://docs.getdbt.com/reference/references-overview","Every config, command and property"),
        ("Incremental models","https://docs.getdbt.com/docs/build/incremental-models","Strategies and is_incremental()"),
        ("BigQuery configs","https://docs.getdbt.com/reference/resource-configs/bigquery-configs","Partitioning, clustering, labels"),
        ("dbt best practices","https://docs.getdbt.com/best-practices","Project structure and style"),
        ("dbt package hub","https://hub.getdbt.com/","Reusable packages"),
        ("dbt Learn courses","https://learn.getdbt.com/","Free official courses")])

D["dags"] = dict(
 F=["Read a DAG; find and read a failed task's log","Rerun a task or a date","Understand logical dates and data intervals"],
 P=["Write idempotent TaskFlow DAGs with retries and templates","Use provider operators and deferrable sensors","Test DAGs locally and in CI"],
 S=["Design orchestration across many pipelines (assets, pools, SLAs)","Run Composer or Airflow reliably; plan upgrades","Decide what belongs in Airflow vs inside the job"],
 E=["Choose the orchestration platform for the organisation","Run large Airflow estates: scaling, multi-tenancy, security","Set standards for scheduling and data-aware workflows"],
 topics=["Assets and data-aware scheduling","Dynamic task mapping","Deferrable operators and triggers","Airflow 3 Task SDK and execution API","Alternatives: Cloud Workflows, Dagster, Temporal"],
 links=[("Apache Airflow documentation","https://airflow.apache.org/docs/apache-airflow/stable/index.html","Concepts and reference"),
        ("Airflow best practices","https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html","Idempotency, top-level code, testing"),
        ("Google provider for Airflow","https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html","BigQuery, GCS, Dataflow operators"),
        ("Cloud Composer","https://cloud.google.com/composer/docs","Managed Airflow on GCP"),
        ("Astronomer Cosmos","https://astronomer.github.io/astronomer-cosmos/","Run dbt projects as Airflow tasks")])

D["spring"] = dict(
 F=["Build a REST endpoint with validation and a test","Configure an app with application.yml and profiles","Use Spring Data or JdbcClient for simple queries"],
 P=["Handle errors with ProblemDetail; write slice and integration tests","Use transactions correctly; understand proxies","Add Actuator, metrics and structured logging"],
 S=["Choose servlet vs reactive and design for throughput","Secure APIs with Spring Security and OAuth 2.0","Tune startup, memory and connection pools for the cloud"],
 E=["Lead major upgrades (3.x to 4.x) across services","Build internal starters and platform libraries","Set architecture and module boundaries (Spring Modulith)"],
 topics=["Auto-configuration and writing your own starter","Spring Modulith","Observability with Micrometer and OpenTelemetry","GraalVM native images and CDS","Spring Boot 4 migration"],
 links=[("Spring Boot reference","https://docs.spring.io/spring-boot/index.html","Official reference"),
        ("Spring guides","https://spring.io/guides","Short task-focused tutorials"),
        ("Spring Framework reference","https://docs.spring.io/spring-framework/reference/","Core, web, data access, testing"),
        ("Spring Boot release notes","https://github.com/spring-projects/spring-boot/wiki","What changed in each version"),
        ("Spring Cloud GCP","https://googlecloudplatform.github.io/spring-cloud-gcp/","GCP integrations for Spring"),
        ("Testcontainers guides","https://testcontainers.com/guides/","Integration testing with Spring Boot")])

D["quarkus"] = dict(
 F=["Create a project and run dev mode","Write a REST endpoint and a @QuarkusTest","Configure with application.properties and profiles"],
 P=["Use Panache, REST clients and fault tolerance","Choose blocking, reactive or virtual-thread endpoints","Package as a container; use Dev Services"],
 S=["Build and run native images; fix reflection issues","Design for Kubernetes and serverless startup","Migrate services from Spring with clear trade-offs"],
 E=["Write Quarkus extensions","Set framework strategy across Spring and Quarkus estates","Understand build-time processing and ArC internals"],
 topics=["Mutiny reactive programming","Native image configuration","Writing extensions","Quarkus with Kafka and messaging","Command-mode applications"],
 links=[("Quarkus guides","https://quarkus.io/guides/","Task-focused official guides"),
        ("Get started with Quarkus","https://quarkus.io/get-started/","Install and first app"),
        ("code.quarkus.io","https://code.quarkus.io/","Generate a project with chosen extensions"),
        ("SmallRye Mutiny","https://smallrye.io/smallrye-mutiny/","Reactive programming library used by Quarkus"),
        ("Quarkiverse","https://docs.quarkiverse.io/","Community extensions, including Google Cloud")])

D["architecture"] = dict(
 F=["Explain layered and hexagonal architecture","Tell events from commands; choreography from orchestration","Recognise retries that need idempotency"],
 P=["Implement outbox, idempotent consumers and retries with backoff","Design a saga with compensations","Apply circuit breakers, bulkheads and timeouts"],
 S=["Choose monolith, modular monolith or services for a context","Design event-driven systems with contracts and evolution","Run design reviews and write decision records"],
 E=["Set architecture direction across many teams","Balance consistency, availability, cost and team structure","Lead large migrations (strangler fig) safely"],
 topics=["Domain-driven design: bounded contexts","Architecture decision records (ADRs)","Event schema evolution and registries","CQRS and event sourcing in practice","Team topologies and Conway's law"],
 links=[("microservices.io patterns","https://microservices.io/patterns/","Saga, outbox, CQRS and more, with trade-offs"),
        ("Martin Fowler: architecture","https://martinfowler.com/architecture/","Essays on patterns and evolution"),
        ("Azure cloud design patterns","https://learn.microsoft.com/en-us/azure/architecture/patterns/","Vendor-neutral pattern catalogue"),
        ("Enterprise Integration Patterns","https://www.enterpriseintegrationpatterns.com/","Messaging patterns"),
        ("Google Cloud Architecture Center","https://cloud.google.com/architecture","Reference architectures on GCP")])

D["sysdesign"] = dict(
 F=["Follow the method: requirements, estimates, API, data, diagram","Name the building blocks and what each is for","Do back-of-the-envelope estimates"],
 P=["Design a small service end to end with caching and a queue","Identify bottlenecks and failure modes","Write a design document others can build from"],
 S=["Design for scale, availability targets and cost together","Choose storage and consistency models with clear trade-offs","Lead design reviews and challenge assumptions with numbers"],
 E=["Design multi-region, highly available systems","Set reliability and capacity strategy for the organisation","Mentor others in design and trade-off thinking"],
 topics=["Consistent hashing and partitioning","Consensus (Raft) and leader election","Multi-region active-active design","Capacity planning and load testing","SLOs and error budgets"],
 links=[("System Design Primer","https://github.com/donnemartin/system-design-primer","Free, broad introduction with examples"),
        ("Designing Data-Intensive Applications","https://dataintensive.net/","The deep reference behind most designs"),
        ("Google SRE books (free)","https://sre.google/books/","Reliability, SLOs, operations at scale"),
        ("Google Cloud Architecture Framework","https://cloud.google.com/architecture/framework","Reliability, cost, security, performance pillars"),
        ("High Scalability","https://highscalability.com/","Real-world architecture write-ups")])

D["devops"] = dict(
 F=["Use Git daily: branch, commit, rebase, PR","Read a CI run and find why it failed","Roll back a deploy"],
 P=["Write CI/CD workflows with caching and keyless cloud auth","Add structured logs, metrics and alerts","Take part in incident response"],
 S=["Design release strategies (canary, blue/green, flags)","Define SLOs and alerting on symptoms","Improve DORA metrics; lead post-incident reviews"],
 E=["Build an internal developer platform and golden paths","Set delivery and reliability standards for the organisation","Lead culture change toward small, safe, frequent releases"],
 topics=["Trunk-based development","OpenTelemetry for traces, metrics and logs","GitOps (Argo CD, Flux)","Platform engineering and golden paths","Chaos engineering"],
 links=[("Pro Git (free book)","https://git-scm.com/book/en/v2","Git from basics to internals"),
        ("GitHub Actions documentation","https://docs.github.com/en/actions","Workflows, environments, OIDC"),
        ("DORA","https://dora.dev/","Research on delivery performance and its capabilities"),
        ("Google SRE books (free)","https://sre.google/books/","SLOs, alerting, incident response"),
        ("The Twelve-Factor App","https://12factor.net/","Principles for cloud-native services"),
        ("Trunk-based development","https://trunkbaseddevelopment.com/","Branching that supports continuous delivery"),
        ("OpenTelemetry","https://opentelemetry.io/docs/","Vendor-neutral observability")])

D["terraform"] = dict(
 F=["Run init, plan and apply; read a plan","Change a resource's arguments safely","Use variables and outputs"],
 P=["Write reusable modules with validation","Manage state in a remote backend; use moved and import blocks","Run Terraform from CI with keyless auth"],
 S=["Design module and state layout for many environments","Refactor live infrastructure without destroying it","Write terraform tests and policy checks"],
 E=["Own infrastructure-as-code standards for the organisation","Design org-wide landing zones and guardrails","Lead provider upgrades and large migrations"],
 topics=["State locking and drift detection","Policy as code (OPA, Sentinel)","Terraform test and mock providers","Ephemeral values and write-only arguments","Landing zones on GCP"],
 links=[("Terraform documentation","https://developer.hashicorp.com/terraform/docs","Official docs"),
        ("Terraform language","https://developer.hashicorp.com/terraform/language","HCL, modules, expressions, state"),
        ("Terraform tutorials","https://developer.hashicorp.com/terraform/tutorials","Step-by-step learning"),
        ("Google provider docs","https://registry.terraform.io/providers/hashicorp/google/latest/docs","Every GCP resource and argument"),
        ("Terraform on Google Cloud","https://cloud.google.com/docs/terraform","Google's guides and best practices")])

D["cloudrun"] = dict(
 F=["Deploy a service and read its logs","Execute a job and check its result","Roll traffic back to a previous revision"],
 P=["Set scaling, CPU, memory, concurrency and timeouts deliberately","Secure services with IAM, secrets and service accounts","Connect to private resources with VPC egress"],
 S=["Design job sharding, retries and run records","Tune cold starts and cost","Design service-to-service auth and traffic management"],
 E=["Set the serverless platform blueprint for the organisation","Decide Cloud Run vs GKE vs other compute","Design multi-region serverless architectures"],
 topics=["Container runtime contract","Direct VPC egress and Cloud NAT","Startup CPU boost and minimum instances","Cloud Run jobs with Workflows","Eventarc triggers"],
 links=[("Cloud Run documentation","https://cloud.google.com/run/docs","Official docs"),
        ("Container runtime contract","https://cloud.google.com/run/docs/container-contract","What your container must do"),
        ("Cloud Run jobs","https://cloud.google.com/run/docs/create-jobs","Create and execute jobs"),
        ("General development tips","https://cloud.google.com/run/docs/tips/general","Performance and cost tips"),
        ("Quotas and limits","https://cloud.google.com/run/quotas","Memory, CPU, timeouts, request size")])

D["kubernetes"] = dict(
 F=["Use kubectl to get, describe, log and exec","Read a Deployment and Service manifest","Explain why a pod is Pending or crashing"],
 P=["Write manifests with probes, resources and config","Use Helm or Kustomize per environment","Set up Workload Identity and RBAC"],
 S=["Design namespaces, network policies and autoscaling","Run production clusters: upgrades, PDBs, capacity","Debug networking, DNS and scheduling problems"],
 E=["Design multi-cluster platforms and tenancy models","Build operators and platform abstractions","Set Kubernetes strategy and security policy"],
 topics=["Gateway API","Operators and custom resources","Pod security standards","Service meshes","GKE Autopilot vs Standard"],
 links=[("Kubernetes documentation","https://kubernetes.io/docs/home/","Official docs"),
        ("kubectl quick reference","https://kubernetes.io/docs/reference/kubectl/quick-reference/","Common commands"),
        ("Troubleshooting","https://kubernetes.io/docs/tasks/debug/","Debug pods, services and clusters"),
        ("GKE documentation","https://cloud.google.com/kubernetes-engine/docs","Google Kubernetes Engine"),
        ("Helm","https://helm.sh/docs/","Package manager for Kubernetes"),
        ("Gateway API","https://gateway-api.sigs.k8s.io/","The successor to Ingress")])

D["ai"] = dict(
 F=["Call a model API and get structured output","Explain tokens, context, hallucination and prompt injection","Use an AI assistant with tests and review"],
 P=["Build a RAG feature with retrieval, citations and an eval set","Use tools and handle refusals, errors and cost","Brief an AI agent with context, rules and a definition of done"],
 S=["Design AI features with evals, guardrails, observability and fallbacks","Tune cost and latency (caching, batch, model choice)","Set up repos so AI agents work safely (context files, hooks, gates)"],
 E=["Set AI strategy, governance and security across the organisation","Design agentic systems and their safety boundaries","Build shared AI platforms, blueprints and evaluation infrastructure"],
 topics=["Evaluation design and model-graded evals","Retrieval: hybrid search, reranking, chunking","Agents, tool design and MCP","Prompt injection defences","Cost and latency engineering"],
 links=[("Claude developer docs","https://platform.claude.com/docs","Anthropic API, tools, structured outputs, prompt caching"),
        ("Building effective agents (Anthropic)","https://www.anthropic.com/engineering/building-effective-agents","When to use workflows vs agents"),
        ("Claude Code docs","https://code.claude.com/docs/en/overview","Agentic coding, hooks, subagents"),
        ("Model Context Protocol","https://modelcontextprotocol.io/","Open protocol for tools and data"),
        ("Vertex AI generative AI","https://cloud.google.com/vertex-ai/generative-ai/docs","Models and tooling on GCP"),
        ("BigQuery vector search","https://cloud.google.com/bigquery/docs/vector-search-intro","Embeddings and VECTOR_SEARCH"),
        ("pgvector","https://github.com/pgvector/pgvector","Vector search in Postgres"),
        ("OWASP GenAI security","https://genai.owasp.org/","LLM application risks")])

D["gcpdata"] = dict(
 F=["Name the GCP service for each lifecycle stage","Load files from GCS into BigQuery and query them","Navigate IAM roles for data access"],
 P=["Build a batch ELT pipeline: landing, BigQuery layers, dbt, scheduling","Set up Pub/Sub to BigQuery, or Datastream CDC","Apply dataset-level IAM and cost controls"],
 S=["Choose between Dataflow, Dataproc, SQL and Cloud Run for a workload","Design a platform with governance (Dataplex), lineage and quality","Plan cost, regions and data residency"],
 E=["Own the organisation's GCP data architecture","Lead migrations from other clouds or on-premises","Hold the Professional Data Engineer or Architect level of judgement, and teach it"],
 topics=["Dataflow streaming: windows, triggers, late data","BigLake and Iceberg on GCS","Dataplex data quality and lineage","Analytics Hub data sharing","Professional Data Engineer exam guide"],
 links=[("Google Cloud data analytics products","https://cloud.google.com/products/data-analytics","Overview of every data service"),
        ("Dataflow documentation","https://cloud.google.com/dataflow/docs","Beam pipelines on GCP"),
        ("Pub/Sub documentation","https://cloud.google.com/pubsub/docs","Messaging, including BigQuery subscriptions"),
        ("Datastream documentation","https://cloud.google.com/datastream/docs","Change data capture"),
        ("Dataproc documentation","https://cloud.google.com/dataproc/docs","Spark and Hadoop"),
        ("Dataplex documentation","https://cloud.google.com/dataplex/docs","Governance, quality and lineage"),
        ("Professional Data Engineer certification","https://cloud.google.com/learn/certification/data-engineer","Exam guide and learning path")])

D["apis"] = dict(
 F=["Explain REST resources, methods and status codes","Call an API with curl and read its OpenAPI spec","Tell sync from async integration"],
 P=["Design a REST API with pagination, errors and versioning","Write and publish an OpenAPI contract","Add timeouts, retries and idempotency keys"],
 S=["Choose REST, gRPC, GraphQL or events for a context","Design gateway, mesh and BFF responsibilities","Run API evolution: deprecation and contract tests"],
 E=["Set API standards and governance across the organisation","Design a partner and public API programme","Lead integration architecture across many systems"],
 topics=["Problem Details (RFC 9457)","AsyncAPI for event-driven contracts","gRPC streaming and deadlines","GraphQL federation","API design guides (Google AIP)"],
 links=[("Google API Improvement Proposals (AIP)","https://google.aip.dev/","Google's detailed API design rules"),
        ("OpenAPI Specification","https://spec.openapis.org/oas/latest.html","The contract format for HTTP APIs"),
        ("gRPC documentation","https://grpc.io/docs/","Concepts and language guides"),
        ("GraphQL","https://graphql.org/learn/","Official introduction"),
        ("AsyncAPI","https://www.asyncapi.com/docs","Contracts for event-driven APIs"),
        ("RFC 9457: Problem Details for HTTP APIs","https://www.rfc-editor.org/rfc/rfc9457","Standard error format"),
        ("Enterprise Integration Patterns","https://www.enterpriseintegrationpatterns.com/","Messaging and integration patterns")])

D["kafka"] = dict(
 F=["Explain topics, partitions, offsets and consumer groups","Produce and consume with the CLI","Read consumer lag"],
 P=["Build producers and consumers in Spring, Quarkus or Python with correct acks and commits","Make consumers idempotent; use dead-letter topics","Use a schema registry"],
 S=["Design topics, keys and partition counts for scale and ordering","Run Kafka Connect and CDC pipelines","Tune throughput, latency and durability"],
 E=["Operate Kafka platforms (or choose managed) for the organisation","Design event-driven architectures across domains","Lead stream processing with Kafka Streams or Flink"],
 topics=["Exactly-once semantics and transactions","Consumer rebalancing protocols","Tiered storage","KRaft operations","Kafka Streams state stores"],
 links=[("Apache Kafka documentation","https://kafka.apache.org/documentation/","Design, configuration, operations"),
        ("Spring for Apache Kafka","https://docs.spring.io/spring-kafka/reference/","Templates, listeners, error handling"),
        ("Quarkus Kafka guide","https://quarkus.io/guides/kafka","Reactive messaging with Kafka"),
        ("confluent-kafka-python","https://docs.confluent.io/kafka-clients/python/current/overview.html","Python client"),
        ("Confluent Developer courses","https://developer.confluent.io/","Free courses on Kafka fundamentals and patterns"),
        ("Managed Service for Apache Kafka","https://cloud.google.com/managed-service-for-apache-kafka/docs","Kafka on Google Cloud"),
        ("Debezium","https://debezium.io/documentation/","Change data capture into Kafka")])

D["apigee"] = dict(
 F=["Explain proxies, policies, products and apps","Call an API through Apigee with a key","Read Apigee analytics for an API"],
 P=["Build a proxy with key/token verification, spike arrest and quota","Use shared flows; deploy through environments from CI","Connect securely to Cloud Run backends"],
 S=["Design API products, tiers and the developer portal","Run Apigee across environments with Terraform and CI","Secure APIs at the edge with OAuth and Advanced API Security"],
 E=["Own the organisation's API management platform and governance","Design hybrid or multi-region Apigee deployments","Lead API monetisation and partner programmes"],
 topics=["Shared flows and flow hooks","Apigee hybrid on GKE","Advanced API Security","Developer portals (integrated and Drupal)","apigeelint and proxy testing"],
 links=[("Apigee documentation","https://cloud.google.com/apigee/docs","Official docs for Apigee X and hybrid"),
        ("Apigee policy reference","https://cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy","Every policy and its options"),
        ("Apigee samples","https://github.com/GoogleCloudPlatform/apigee-samples","Working proxy examples"),
        ("apigeelint","https://github.com/apigee/apigeelint","Static checks for proxy bundles"),
        ("API Gateway documentation","https://cloud.google.com/api-gateway/docs","The lighter-weight alternative")])

D["oauth"] = dict(
 F=["Explain access, ID and refresh tokens and scopes","Protect an API with a JWT resource server configuration","Use the authorisation code flow with PKCE through a library"],
 P=["Validate tokens fully: signature, issuer, audience, expiry, scopes","Choose the right flow per client type","Store tokens safely in web and mobile apps"],
 S=["Design identity for a product: providers, BFF, service-to-service, token lifetimes","Review OAuth implementations for the common mistakes","Integrate gateways (Apigee) and workload identity"],
 E=["Own identity architecture across the organisation","Apply advanced specs (DPoP, PAR, token exchange)","Lead identity incidents and provider migrations"],
 topics=["RFC 9700 security best current practice","OpenID Connect discovery and dynamic registration","Token exchange (RFC 8693)","Sender-constrained tokens (DPoP, mTLS)","Workload Identity Federation"],
 links=[("OAuth 2.0 (oauth.net)","https://oauth.net/2/","Overview and links to every OAuth spec"),
        ("RFC 6749: OAuth 2.0","https://www.rfc-editor.org/rfc/rfc6749","The core framework"),
        ("RFC 7636: PKCE","https://www.rfc-editor.org/rfc/rfc7636","Proof Key for Code Exchange"),
        ("RFC 9700: OAuth 2.0 Security Best Current Practice","https://www.rfc-editor.org/rfc/rfc9700","Current security guidance"),
        ("OpenID Connect Core","https://openid.net/specs/openid-connect-core-1_0.html","The OIDC specification"),
        ("OWASP OAuth 2.0 cheat sheet","https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html","Practical security checklist"),
        ("jwt.io","https://jwt.io/","Decode and inspect JWTs (never paste production tokens)")])

D["harness"] = dict(
 F=["Run a pipeline and read its logs","Understand stages, steps, services and environments","Approve or roll back a deployment"],
 P=["Build CI and CD pipelines with connectors, secrets and triggers","Use canary or blue-green with verification","Keep pipelines in Git and use templates"],
 S=["Design org-wide templates and OPA policies","Set up delegates, RBAC and environments securely","Integrate verification with monitoring and feature flags"],
 E=["Own the delivery platform strategy and its governance","Lead migrations from other CI/CD tools","Measure and improve delivery (DORA) across teams"],
 topics=["Pipeline, stage and step templates","Continuous verification","OPA policies in Harness","GitOps with Harness","Feature flags for progressive delivery"],
 links=[("Harness developer hub","https://developer.harness.io/docs","Official documentation and tutorials"),
        ("Harness University","https://university.harness.io/","Courses and certifications"),
        ("Open Policy Agent","https://www.openpolicyagent.org/docs/latest/","Policy as code used by Harness"),
        ("DORA","https://dora.dev/","Measuring delivery performance")])

D["graphql"] = dict(
 F=["Read a schema and write queries with variables and fragments","Explain queries, mutations, subscriptions and resolvers","Tell when GraphQL fits better than REST"],
 P=["Build a server with Spring for GraphQL, SmallRye or Strawberry","Avoid N+1 with batch loaders; paginate with connections","Return useful errors and test resolvers"],
 S=["Secure a GraphQL API: field authorisation, depth and cost limits, persisted queries","Evolve a schema without breaking clients; schema checks in CI","Tune performance with tracing and caching"],
 E=["Design a federated graph across teams","Set GraphQL governance and standards for the organisation","Decide GraphQL vs REST vs gRPC strategy across products"],
 topics=["GraphQL specification: execution and validation","DataLoader and batching","Relay connection specification","Apollo Federation and supergraphs","Persisted queries and query cost analysis"],
 links=[("Learn GraphQL","https://graphql.org/learn/","Official introduction"),
        ("GraphQL specification","https://spec.graphql.org/","How queries are parsed, validated and executed"),
        ("Spring for GraphQL","https://docs.spring.io/spring-graphql/reference/","Annotated controllers, batching, testing"),
        ("Quarkus SmallRye GraphQL guide","https://quarkus.io/guides/smallrye-graphql","Code-first GraphQL in Quarkus"),
        ("Strawberry","https://strawberry.rocks/docs","Python GraphQL with type hints"),
        ("Relay connection spec","https://relay.dev/graphql/connections.htm","Cursor pagination convention"),
        ("Apollo Federation","https://www.apollographql.com/docs/federation/","Composing subgraphs into one graph"),
        ("OWASP GraphQL cheat sheet","https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html","Security checklist")])

D["web"] = dict(
 F=["Explain what happens from typing a URL to seeing a page","Read requests, responses, headers and status codes in DevTools","Know what cookies, sessions and CORS are"],
 P=["Set caching, cookie and security headers correctly","Debug CORS, redirects, mixed content and caching problems","Choose a rendering model for a feature"],
 S=["Design front-end delivery: CDN, caching, rendering, performance budgets","Lead web security (CSP, session design) and accessibility for a product","Diagnose Core Web Vitals problems with field data"],
 E=["Set web platform standards across products","Know the HTTP, TLS and browser specs in depth","Lead large front-end architecture and performance programmes"],
 topics=["HTTP semantics (RFC 9110) and caching (RFC 9111)","Browser rendering pipeline and the event loop","Service workers and offline apps","Content Security Policy in depth","WCAG 2.2 success criteria"],
 links=[("MDN Web Docs","https://developer.mozilla.org/en-US/docs/Web","The reference for HTML, CSS, JavaScript and HTTP"),
        ("MDN: How the web works","https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works","A gentle overview"),
        ("MDN: CORS","https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS","Preflights, credentials and headers"),
        ("web.dev","https://web.dev/","Google's guides on performance, Core Web Vitals and modern web practice"),
        ("RFC 9110: HTTP Semantics","https://www.rfc-editor.org/rfc/rfc9110","Methods, status codes and headers, authoritatively"),
        ("WCAG 2.2","https://www.w3.org/TR/WCAG22/","Accessibility guidelines"),
        ("OWASP Cheat Sheet Series","https://cheatsheetseries.owasp.org/","XSS, CSRF, session management and more")])

D["microservices"] = dict(
 F=["Explain monolith vs modular monolith vs microservices","Work in one service: build, test, deploy, read its logs and traces","Know why services own their data"],
 P=["Build a service with timeouts, retries, circuit breakers and health checks","Use events and the outbox to integrate with other services","Write contract tests with consumers"],
 S=["Draw service boundaries from the domain; decide when not to split","Design sagas, read models and observability across services","Lead a strangler-fig extraction from a monolith"],
 E=["Set the organisation's service architecture and platform blueprint","Align team structure with service ownership","Decide when to consolidate services as well as split them"],
 topics=["Domain-driven design: bounded contexts and context maps","Contract testing with Pact","Service mesh traffic management","Team Topologies","Platform engineering and service templates"],
 links=[("Microservices (Martin Fowler &amp; James Lewis)","https://martinfowler.com/articles/microservices.html","The original description and its trade-offs"),
        ("microservices.io","https://microservices.io/patterns/","Pattern language: decomposition, data, communication, observability"),
        ("Building Microservices, 2nd ed. (Sam Newman)","https://samnewman.io/books/building_microservices_2nd_edition/","The standard book on the subject"),
        ("Monolith to Microservices (Sam Newman)","https://samnewman.io/books/monolith-to-microservices/","Migration patterns"),
        ("Resilience4j","https://resilience4j.readme.io/docs","Circuit breakers, retries, bulkheads for Java"),
        ("OpenTelemetry","https://opentelemetry.io/docs/","Distributed tracing and metrics"),
        ("Team Topologies","https://teamtopologies.com/","Organising teams around services and platforms")])

D["eventsourcing"] = dict(
 F=["Explain events, streams, aggregates, projections and CQRS","Read an event stream and follow how state was built","Tell an append-only ledger from full event sourcing"],
 P=["Implement an aggregate with decide/apply and given-when-then tests","Build idempotent projections with checkpoints","Append with optimistic concurrency"],
 S=["Decide where event sourcing fits in a system and where it does not","Design event schemas, versioning and upcasting","Plan snapshots, replay, rebuilds and personal-data handling"],
 E=["Lead event-sourced architectures across domains and teams","Choose and operate event stores at scale","Set standards for event modelling and governance"],
 topics=["Event storming workshops","Upcasting and event versioning","Process managers and sagas over events","Crypto-shredding for personal data","Projection rebuild strategies"],
 links=[("Event Sourcing (Martin Fowler)","https://martinfowler.com/eaaDev/EventSourcing.html","The classic explanation"),
        ("CQRS (Martin Fowler)","https://martinfowler.com/bliki/CQRS.html","When separate read and write models help"),
        ("Event sourcing pattern (microservices.io)","https://microservices.io/patterns/data/event-sourcing.html","In a microservices context"),
        ("Event Sourcing pattern (Azure Architecture Center)","https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing","Issues and considerations"),
        ("Versioning in an Event Sourced System (Greg Young)","https://leanpub.com/esversioning","Free book on evolving events"),
        ("KurrentDB documentation","https://docs.kurrent.io/","Event store (formerly EventStoreDB)"),
        ("Axon documentation","https://docs.axoniq.io/","Java framework for event sourcing and CQRS")])

D["llm"] = dict(
 F=["Explain tokens, context windows, next-token prediction and training cutoffs","Make a single model call with structured output","Know when to prompt, retrieve, use tools or fine-tune"],
 P=["Build a tool loop or use an SDK tool runner","Run a local or self-hosted model and compare it with a hosted API","Log, budget and handle errors for LLM calls"],
 S=["Choose runtimes and models by quality, cost, latency and data controls","Design agent harnesses with bounded loops, context management and approvals","Plan self-hosting capacity (GPU memory, batching, quantisation)"],
 E=["Set the organisation's model and runtime strategy","Lead fine-tuning or custom model programmes where justified","Design platform-level AI infrastructure and governance"],
 topics=["Transformer architecture and attention","Inference optimisation: KV cache, batching, speculative decoding","Fine-tuning with LoRA","Agent design and context management","Model evaluation and benchmarking"],
 links=[("Claude developer docs","https://platform.claude.com/docs","Messages API, tools, streaming, caching"),
        ("Building effective agents (Anthropic)","https://www.anthropic.com/engineering/building-effective-agents","Workflows vs agents"),
        ("Claude Agent SDK","https://code.claude.com/docs/en/agent-sdk","Claude Code's harness as a library"),
        ("Vertex AI Model Garden","https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models","Hosted and open models on GCP"),
        ("vLLM documentation","https://docs.vllm.ai/","High-throughput self-hosted inference"),
        ("Ollama","https://ollama.com/","Run models locally"),
        ("Hugging Face course","https://huggingface.co/learn","Free courses on transformers and LLMs"),
        ("The Illustrated Transformer (Jay Alammar)","https://jalammar.github.io/illustrated-transformer/","Visual explanation of attention")])

D["rag"] = dict(
 F=["Explain the ingestion, retrieval and generation phases","Run a vector search over embedded chunks","Prompt a model to answer from passages with citations"],
 P=["Build an incremental ingestion pipeline with chunking, metadata and embeddings","Add hybrid search, reranking and permission filters","Build a golden question set and measure recall and faithfulness"],
 S=["Design RAG for a domain: chunking strategy, index choice, latency and cost","Diagnose retrieval vs generation failures from evals","Secure RAG: access control, prompt injection, suppressions"],
 E=["Own retrieval and knowledge platforms across products","Lead advanced retrieval (agentic, graph-based) where it measurably helps","Set evaluation standards for AI answers in the organisation"],
 topics=["Contextual retrieval","Hybrid search and reciprocal rank fusion","Rerankers and cross-encoders","Evaluation frameworks for RAG","GraphRAG and agentic retrieval"],
 links=[("Contextual Retrieval (Anthropic)","https://www.anthropic.com/news/contextual-retrieval","Reducing retrieval failures with chunk context"),
        ("Claude citations","https://platform.claude.com/docs/en/build-with-claude/citations","Cited answers from documents"),
        ("pgvector","https://github.com/pgvector/pgvector","Vector search in Postgres"),
        ("BigQuery vector search","https://cloud.google.com/bigquery/docs/vector-search-intro","Embeddings and VECTOR_SEARCH"),
        ("Vertex AI Vector Search","https://cloud.google.com/vertex-ai/docs/vector-search/overview","Managed approximate nearest neighbour search"),
        ("Vertex AI RAG Engine","https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview","Managed RAG on GCP"),
        ("OWASP GenAI security","https://genai.owasp.org/","Prompt injection and LLM risks")])

D["mcp"] = dict(
 F=["Explain servers, clients, tools, resources and transports","Add an existing MCP server to Claude Code and use it","Know the security risks of untrusted servers"],
 P=["Build an MCP server with FastMCP and test it with the Inspector","Expose read-only pipeline or warehouse tools with guardrails","Share servers with a team via project configuration"],
 S=["Design task-shaped tool sets with honest errors and compact outputs","Deploy remote servers on Cloud Run with OAuth or IAM","Integrate MCP with data pipelines without putting it on the critical path"],
 E=["Set MCP standards, review and approval process for the organisation","Build shared MCP platforms over core data and systems","Contribute to the protocol ecosystem"],
 topics=["MCP specification and transports","MCP authorisation (OAuth)","Tool design for agents","MCP Toolbox for Databases","Tool poisoning and prompt injection defences"],
 links=[("Model Context Protocol","https://modelcontextprotocol.io/","Specification, concepts and SDKs"),
        ("MCP Python SDK","https://github.com/modelcontextprotocol/python-sdk","FastMCP and server examples"),
        ("MCP TypeScript SDK","https://github.com/modelcontextprotocol/typescript-sdk","Servers and clients in TypeScript"),
        ("MCP Inspector","https://github.com/modelcontextprotocol/inspector","Test servers interactively"),
        ("Claude Code: MCP","https://code.claude.com/docs/en/mcp","Adding servers, scopes and permissions"),
        ("MCP connector (Claude API)","https://platform.claude.com/docs/en/agents-and-tools/mcp-connector","Calling remote MCP servers from the API"),
        ("MCP Toolbox for Databases","https://github.com/googleapis/genai-toolbox","Google's MCP server for BigQuery, Postgres and more")])

D["observability"] = dict(
 F=["Find a request's or run's logs and errors in Cloud Logging","Read a service dashboard: traffic, errors, latency","Write structured logs with IDs and evidence"],
 P=["Instrument a service with OpenTelemetry and custom metrics","Write log queries, log-based metrics and PromQL","Build dashboards and actionable alerts with runbooks"],
 S=["Design observability for a system: signals, sampling, cardinality, cost","Trace problems across services, queues and pipelines","Set dashboard and alert templates for teams"],
 E=["Own the observability platform and its standards","Lead cost and data-governance strategy for telemetry","Drive observability-led reliability across the organisation"],
 topics=["OpenTelemetry Collector pipelines and tail sampling","High-cardinality observability and wide events","Continuous profiling","Exemplars linking metrics to traces","eBPF-based instrumentation"],
 links=[("OpenTelemetry documentation","https://opentelemetry.io/docs/","APIs, SDKs, collector, semantic conventions"),
        ("Cloud Logging documentation","https://cloud.google.com/logging/docs","Logs, sinks, log-based metrics"),
        ("Logging query language","https://cloud.google.com/logging/docs/view/logging-query-language","Filter syntax for Logs Explorer and alerts"),
        ("Cloud Monitoring documentation","https://cloud.google.com/monitoring/docs","Metrics, dashboards, alerting, PromQL"),
        ("Cloud Trace documentation","https://cloud.google.com/trace/docs","Distributed tracing on GCP"),
        ("Prometheus documentation","https://prometheus.io/docs/","Metric types and PromQL"),
        ("Micrometer documentation","https://docs.micrometer.io/micrometer/reference/","Metrics and observations for Java"),
        ("Observability Engineering (book)","https://www.oreilly.com/library/view/observability-engineering/9781492076438/","Majors, Fong-Jones and Miranda")])

D["sre"] = dict(
 F=["Explain SLI, SLO, error budget and SLA","Follow a runbook and escalate during an incident","Contribute to a blameless postmortem"],
 P=["Define SLIs and SLOs for a service or pipeline","Set up burn-rate alerts and runbooks","Take on-call shifts and lead mitigation"],
 S=["Act as incident commander; run postmortems and track actions","Write and enforce an error budget policy with product owners","Run production readiness reviews and capacity plans"],
 E=["Set reliability strategy and SRE practice for the organisation","Design multi-region resilience and DR programmes","Build a culture of blameless learning and toil reduction"],
 topics=["Multi-window, multi-burn-rate alerting","Incident command system","Chaos engineering and game days","Capacity planning and load testing","Disaster recovery: RPO, RTO and restore drills"],
 links=[("Google SRE books (free)","https://sre.google/books/","Site Reliability Engineering, The SRE Workbook, Building Secure and Reliable Systems"),
        ("Implementing SLOs (SRE Workbook)","https://sre.google/workbook/implementing-slos/","Choosing SLIs and targets"),
        ("Alerting on SLOs (SRE Workbook)","https://sre.google/workbook/alerting-on-slos/","Burn-rate alerting in detail"),
        ("Postmortem culture (SRE book)","https://sre.google/sre-book/postmortem-culture/","Blameless learning from failure"),
        ("Cloud Monitoring SLOs","https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring","Service monitoring and SLO alerts"),
        ("PagerDuty incident response guide","https://response.pagerduty.com/","Open incident response process"),
        ("Implementing Service Level Objectives (book)","https://www.oreilly.com/library/view/implementing-service-level/9781492076803/","Alex Hidalgo")])

D["performance"] = dict(
 F=["Read p50/p95/p99 latency and throughput on a dashboard","Spot an obvious N+1 query or missing index","Run an existing load test and report the result"],
 P=["Profile a JVM or Python service and fix the hot spot","Write load tests with goals and thresholds","Size pools and concurrency with Little's law"],
 S=["Lead performance investigations end to end with evidence","Set performance goals, budgets and capacity plans","Balance latency, throughput and cost in design"],
 E=["Own performance engineering practice across the organisation","Understand runtime, OS and hardware effects deeply","Design systems for extreme scale and tail latency"],
 topics=["Flame graphs and off-CPU analysis","JVM garbage collector tuning","Queueing theory basics","The Tail at Scale","Coordinated omission in load testing"],
 links=[("Brendan Gregg's site","https://www.brendangregg.com/","The USE method, flame graphs, Linux performance tools"),
        ("The Tail at Scale (Dean &amp; Barroso)","https://research.google/pubs/the-tail-at-scale/","Why tail latency dominates in fan-out systems"),
        ("async-profiler","https://github.com/async-profiler/async-profiler","Low-overhead JVM profiling and flame graphs"),
        ("JMH","https://github.com/openjdk/jmh","Correct Java micro-benchmarks"),
        ("py-spy","https://github.com/benfred/py-spy","Sampling profiler for Python"),
        ("Cloud Profiler","https://cloud.google.com/profiler/docs","Continuous profiling on GCP"),
        ("Grafana k6","https://grafana.com/docs/k6/latest/","Load testing")])

D["caching"] = dict(
 F=["Explain cache-aside, TTL and hit ratio","Use an in-process cache for reference data","Read HTTP caching headers"],
 P=["Add Spring or Python caching with keys, TTLs and eviction on write","Use Redis safely with TTLs, eviction policy and a fallback","Measure hit ratio and staleness"],
 S=["Design multi-layer caching for a system with explicit staleness rules","Prevent stampedes and invalidation races","Decide what must never be cached (outages, permissions, legal effect)"],
 E=["Set caching standards and shared cache platforms","Design caching for global, multi-region systems","Lead consistency and cost trade-offs across products"],
 topics=["Caffeine's W-TinyLFU eviction","Redis data structures and persistence","CDN cache keys and purging","Materialised views and incremental maintenance","Semantic caching for LLM calls (and its risks)"],
 links=[("Redis documentation","https://redis.io/docs/latest/","Commands, data types, eviction"),
        ("Caffeine","https://github.com/ben-manes/caffeine","High-performance Java cache"),
        ("Spring Boot caching","https://docs.spring.io/spring-boot/reference/io/caching.html","Cache abstraction and providers"),
        ("cachetools","https://cachetools.readthedocs.io/","Python caches with TTL and LRU"),
        ("Memorystore documentation","https://cloud.google.com/memorystore/docs","Managed Redis and Valkey on GCP"),
        ("MDN: HTTP caching","https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching","Browser and shared caches"),
        ("BigQuery cached results","https://cloud.google.com/bigquery/docs/cached-results","When BigQuery reuses query results")])

D["architecture"]["links"] += [
 ("Patterns of Distributed Systems (Unmesh Joshi)","https://martinfowler.com/articles/patterns-of-distributed-systems/","Leader election, write-ahead log, quorum and more"),
 ("Architecture decision records","https://adr.github.io/","Templates and tools for ADRs")]
D["architecture"]["topics"] += ["Architecture characteristics and fitness functions"]

D["payments"] = dict(
 F=["Explain authorisation, capture, settlement, refunds and chargebacks","Explain the order → checkout → verify → webhook flow","Know why card data must never touch your servers"],
 P=["Integrate a gateway with server-side verification and signed webhooks","Make payment calls and webhook handling idempotent","Model payments as a state machine; test with test-mode fixtures"],
 S=["Design subscriptions, dunning and entitlements","Build a double-entry ledger and daily reconciliation","Own payment security, PCI scope and regulatory rules (RBI)"],
 E=["Design multi-gateway routing and payment platforms","Lead payments compliance and audits","Set money-handling standards across the organisation"],
 topics=["3-D Secure and strong customer authentication","UPI AutoPay and e-mandates","Card network tokenisation","Double-entry accounting for engineers","Fraud detection and chargeback management"],
 links=[("Razorpay documentation","https://razorpay.com/docs/","Orders, checkout, webhooks, subscriptions"),
        ("Stripe documentation","https://docs.stripe.com/","PaymentIntents, webhooks, billing"),
        ("Stripe: idempotent requests","https://docs.stripe.com/api/idempotent_requests","How idempotency keys work"),
        ("PCI Security Standards Council","https://www.pcisecuritystandards.org/","PCI DSS requirements"),
        ("NPCI: UPI","https://www.npci.org.in/what-we-do/upi/product-overview","How UPI works"),
        ("Reserve Bank of India","https://www.rbi.org.in/","Circulars on payments, e-mandates, tokenisation"),
        ("Accounting for developers (Modern Treasury)","https://www.moderntreasury.com/journal/accounting-for-developers-part-i","Double-entry ledgers explained")])

D["opstools"] = dict(
 F=["Read a Grafana or Dynatrace dashboard and find a service's errors","Look up and update a ServiceNow incident","Know what Prometheus, Fluent Bit and Alertmanager each do"],
 P=["Write PromQL queries, recording and alerting rules","Configure log shipping and Grafana dashboards as code","Connect alerts to ServiceNow incidents and CI/CD to change requests"],
 S=["Design the monitoring stack and alert routing for a platform","Integrate Dynatrace or open-source tooling with OpenTelemetry","Automate change management while keeping control"],
 E=["Own observability and ITSM tooling strategy and cost","Lead tool consolidation or migration across the organisation","Set standards for telemetry, alerting and incident process"],
 topics=["Prometheus long-term storage (Thanos, Mimir)","Grafana LGTM stack (Loki, Grafana, Tempo, Mimir)","Fluent Bit processors and multiline parsing","Dynatrace DQL and Grail","ServiceNow DevOps change automation"],
 links=[("Prometheus documentation","https://prometheus.io/docs/","Concepts, PromQL, alerting"),
        ("Alertmanager","https://prometheus.io/docs/alerting/latest/alertmanager/","Routing, grouping, silences"),
        ("Grafana documentation","https://grafana.com/docs/grafana/latest/","Dashboards, data sources, alerting, provisioning"),
        ("Fluent Bit documentation","https://docs.fluentbit.io/","Inputs, filters, outputs"),
        ("Fluentd documentation","https://docs.fluentd.org/","Configuration and plugins"),
        ("Dynatrace documentation","https://docs.dynatrace.com/docs","OneAgent, Davis, DQL"),
        ("ServiceNow developer site","https://developer.servicenow.com/","APIs, including the Table API"),
        ("Google Cloud Managed Service for Prometheus","https://cloud.google.com/stackdriver/docs/managed-prometheus","Prometheus without running it")])

D["blueprints"] = dict(
 F=["Explain why owning generated code costs more than writing it","Use the team's templates and libraries instead of generating new boilerplate","Fill a blueprint's slots with AI help"],
 P=["Spot repeated code and propose a blueprint after the third use","Write codemods with AI to apply a change across repos","Point AI context files at the blueprints"],
 S=["Design framework APIs with escape hatches","Own a blueprint: versioning, docs, migration guides","Decide build vs generate with a cost model"],
 E=["Run a platform team with golden paths and scorecards","Set the organisation's policy on AI generation vs shared frameworks","Measure developer productivity and adoption"],
 topics=["Platform engineering and golden paths","Backstage software templates and scorecards","Codemods (OpenRewrite for Java, LibCST for Python)","Semantic versioning and deprecation","Inner-platform effect"],
 links=[("Platform engineering (CNCF white paper)","https://tag-app-delivery.cncf.io/whitepapers/platforms/","What internal platforms are for"),
        ("Backstage software templates","https://backstage.io/docs/features/software-templates/","Scaffolding from organisation templates"),
        ("OpenRewrite","https://docs.openrewrite.org/","Automated refactoring and upgrades for Java"),
        ("Renovate","https://docs.renovatebot.com/","Automated dependency and version updates"),
        ("Semantic Versioning","https://semver.org/","Version numbers that communicate compatibility"),
        ("Team Topologies","https://teamtopologies.com/","Platform teams and their consumers")])

D["cloudcompare"] = dict(
 F=["Map common services across GCP, AWS and Azure","Explain projects vs accounts vs subscriptions","Use each provider's CLI for basic tasks"],
 P=["Translate a design from one cloud to another, including IAM and networking","Compare prices for a workload, including egress","Use Terraform across providers"],
 S=["Choose a provider for a workload with written trade-offs","Design portable architectures where it matters, and accept lock-in deliberately","Plan data residency and region choices"],
 E=["Set the organisation's cloud strategy, contracts and multi-cloud policy","Lead migrations between clouds or from on-premises","Govern cost, security and compliance across providers"],
 topics=["Well-Architected frameworks of each provider","Cloud IAM models compared","Cross-cloud networking and egress costs","Open table formats for portability","FinOps practices"],
 links=[("Google Cloud: compare AWS and Azure services","https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison","Google's official service mapping"),
        ("Azure for AWS professionals","https://learn.microsoft.com/en-us/azure/architecture/aws-professional/","Microsoft's AWS-to-Azure mapping"),
        ("Google Cloud Architecture Framework","https://cloud.google.com/architecture/framework","Google's design pillars"),
        ("AWS Well-Architected","https://aws.amazon.com/architecture/well-architected/","AWS design pillars"),
        ("Azure Well-Architected Framework","https://learn.microsoft.com/en-us/azure/well-architected/","Azure design pillars"),
        ("FinOps Foundation","https://www.finops.org/","Managing cloud cost across providers")])

D["datalibs"] = dict(
 F=["Load, filter and aggregate a file with pandas or Polars","Read Parquet and inspect its schema","Know which library suits which data size"],
 P=["Use lazy Polars, DuckDB or PyArrow with pushdown on large files","Write a PySpark or Beam job for data beyond one machine","Validate data with pandera or dbt tests and count rejects"],
 S=["Choose engines per workload: warehouse SQL, single-node, distributed, streaming","Tune memory, partitioning and file layout","Design portable pipelines with open formats"],
 E=["Set the organisation's processing stack and standards","Lead migrations between engines (pandas to Polars, Spark to BigQuery)","Understand engine internals: query optimisers, vectorised execution"],
 topics=["Apache Arrow memory format","Polars lazy query optimisation","DuckDB extensions (httpfs, Iceberg)","Spark adaptive query execution","Beam windowing and triggers"],
 links=[("pandas","https://pandas.pydata.org/docs/","User guide and API"),
        ("Polars","https://docs.pola.rs/","User guide, lazy API"),
        ("DuckDB","https://duckdb.org/docs/","SQL, Python API, Parquet and remote files"),
        ("Apache Arrow (PyArrow)","https://arrow.apache.org/docs/python/","Datasets, Parquet, compute"),
        ("Apache Spark","https://spark.apache.org/docs/latest/","PySpark and SQL"),
        ("Apache Beam","https://beam.apache.org/documentation/","Programming guide"),
        ("BigQuery DataFrames","https://cloud.google.com/bigquery/docs/bigquery-dataframes-introduction","pandas-like API in BigQuery"),
        ("pandera","https://pandera.readthedocs.io/","DataFrame validation")])

D["culvert"] = dict(
 F=["Explain contracts, adapters and the conformance suite","Install culvert with the right extras or add the Maven artifacts","Use an adapter through auto-discovery instead of a cloud SDK"],
 P=["Write pipeline code against BlobStore, Warehouse and job control","Use LoadOptions, head() and merge() for idempotent loads","Run and test against emulators locally"],
 S=["Design pipelines whose logic is cloud-neutral","Add an adapter that passes the conformance suite","Use StageClaim, InputReadiness and orchestration gates"],
 E=["Shape the contract spec and its evolution","Lead adoption across teams and clouds","Contribute adapters for new clouds (Azure)"],
 topics=["The contract specification (CONTRACT.md)","Conformance suites as a design tool","Job control and run records","Orchestration renderers","Upgrading across 0.x releases"],
 links=[("Culvert on enrichmeai.com","/culvert/","Overview, libraries, releases, status"),
        ("Culvert on GitHub","https://github.com/enrichmeai/culvert","Source, issues"),
        ("Contract specification","https://github.com/enrichmeai/culvert/blob/main/docs/CONTRACT.md","The authoritative list of contracts"),
        ("Changelog","https://github.com/enrichmeai/culvert/blob/main/CHANGELOG.md","Every release, including fixes"),
        ("Migration guide","https://github.com/enrichmeai/culvert/blob/main/MIGRATION.md","Upgrading between versions"),
        ("culvert on PyPI","https://pypi.org/project/culvert/","Python package")])

D["claudetools"] = dict(
 F=["Run Claude Code in a repo; review and accept its changes","Write a useful CLAUDE.md with commands and rules","Use plan mode and permission prompts sensibly"],
 P=["Add hooks, skills, subagents and MCP servers for the team","Run headless and GitHub Action workflows","Use Cowork with plugins and connectors for knowledge work"],
 S=["Design an agent workflow with gates, reviewers and attempt limits","Govern permissions, secrets and sandboxing","Turn recurring corrections into skills and hooks"],
 E=["Set the organisation's agentic engineering practice","Build shared plugins and blueprints across teams","Measure productivity and quality impact"],
 topics=["Hooks reference and exit codes","Subagent design","Skills and plugins","Claude Code in CI","Agent SDK"],
 links=[("Claude Code overview","https://code.claude.com/docs/en/overview","Install, surfaces, getting started"),
        ("Settings and permissions","https://code.claude.com/docs/en/settings","settings.json, rules, modes"),
        ("Hooks","https://code.claude.com/docs/en/hooks","Events, matchers, exit codes"),
        ("Subagents","https://code.claude.com/docs/en/sub-agents","Defining and using subagents"),
        ("Skills","https://code.claude.com/docs/en/skills","Packaging procedures"),
        ("claude-code-action","https://github.com/anthropics/claude-code-action","Claude Code in GitHub Actions"),
        ("Claude Help Center","https://support.claude.com/","Product guides, including Cowork")])

D["copilot"] = dict(
 F=["Use completions and chat; review every suggestion","Know the difference between GitHub Copilot and Microsoft 365 Copilot","Find and follow the repo's Copilot instructions"],
 P=["Write repository and path instructions and prompt files","Use agent mode and the coding agent on scoped issues","Request and act on Copilot code review"],
 S=["Configure policies, content exclusion and MCP for a team","Set up the coding agent environment and protections","Keep Copilot and Claude Code instructions consistent"],
 E=["Own AI-assisted development policy across the organisation","Evaluate tools and models with real task metrics","Lead adoption and training"],
 topics=["Copilot coding agent","Custom instructions and prompt files","MCP in Copilot","Copilot policies for enterprises","Measuring AI-assisted development"],
 links=[("GitHub Copilot documentation","https://docs.github.com/en/copilot","Features, setup, administration"),
        ("GitHub Copilot features","https://github.com/features/copilot","Overview and plans"),
        ("AGENTS.md","https://agents.md/","Shared format for agent instructions")])

D["agentharness"] = dict(
 F=["Explain loop, tools, context, permissions and gates","Configure a ready-made harness (context file, permissions)","Recognise runaway loops and false completion"],
 P=["Build a bounded tool loop with honest errors and logging","Write agent-friendly tools","Add deterministic gates and a separate reviewer"],
 S=["Design harnesses with context engineering, memory and resume","Evaluate harnesses on task success, cost and interventions","Defend against prompt injection and gate gaming"],
 E=["Build agent platforms and shared harness components","Set safety and governance policy for autonomous agents","Research and adopt new agent patterns with evidence"],
 topics=["Context engineering","Tool design for agents","Multi-agent orchestration","Agent evaluation","Sandboxing and permission design"],
 links=[("Building effective agents","https://www.anthropic.com/engineering/building-effective-agents","Workflows vs agents, patterns"),
        ("Effective context engineering for AI agents","https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents","Managing what the model sees"),
        ("Writing effective tools for agents","https://www.anthropic.com/engineering/writing-tools-for-agents","Tool design"),
        ("Claude Agent SDK","https://code.claude.com/docs/en/agent-sdk","Claude Code's harness as a library"),
        ("LangGraph","https://langchain-ai.github.io/langgraph/","Graph-based agent orchestration")])

D["web3"] = dict(
 F=["Tell Web3 (blockchain) from the Semantic Web","Explain blockchains, wallets, smart contracts and tokens","Ask whether a problem really needs a blockchain"],
 P=["Write and test a simple smart contract on a testnet","Publish structured data with JSON-LD and schema.org","Query linked data with SPARQL"],
 S=["Assess security, cost, privacy and regulation of a Web3 design","Design knowledge graphs and ontologies for a domain","Integrate legal-document standards (Akoma Ntoso, ELI)"],
 E=["Set strategy on decentralised and linked-data technologies","Lead audits and governance for on-chain systems","Shape open data standards in a sector"],
 topics=["Ethereum and proof of stake","Smart contract security","Layer 2 rollups","RDF, OWL and SHACL","Knowledge graphs for AI grounding"],
 links=[("ethereum.org developers","https://ethereum.org/en/developers/","Concepts and tutorials"),
        ("Solidity documentation","https://docs.soliditylang.org/","Language reference"),
        ("W3C Semantic Web","https://www.w3.org/2001/sw/wiki/Main_Page","RDF, SPARQL, OWL standards"),
        ("JSON-LD","https://json-ld.org/","Linked data in JSON"),
        ("schema.org","https://schema.org/","Shared vocabulary for structured data"),
        ("SPARQL 1.1 Query Language","https://www.w3.org/TR/sparql11-query/","The specification"),
        ("OASIS LegalDocML (Akoma Ntoso)","https://www.oasis-open.org/committees/legaldocml/","Standard for legal documents")])

D["solid"] = dict(
 F=["Explain Pods, WebIDs and why apps and data are separated","Read a public resource from a Pod","Compare Solid with Web3 and platforms"],
 P=["Build an app that logs in with Solid-OIDC and reads and writes Pod data","Set access control with WAC or ACP","Model data with shared RDF vocabularies"],
 S=["Design consent-based data sharing on Solid","Choose and operate Solid servers","Plan performance and querying across many Pods"],
 E=["Lead Solid adoption in an organisation or sector","Contribute to the specifications","Set data-sovereignty strategy"],
 topics=["Solid Protocol specification","Solid-OIDC","WAC vs ACP access control","Linked data vocabularies","Community Solid Server"],
 links=[("Solid Project","https://solidproject.org/","Overview, apps, community"),
        ("Solid Protocol","https://solidproject.org/TR/protocol","The specification"),
        ("Web Access Control","https://solidproject.org/TR/wac","Access control specification"),
        ("Inrupt documentation","https://docs.inrupt.com/","Client libraries and server"),
        ("Community Solid Server","https://communitysolidserver.github.io/CommunitySolidServer/latest/","Open-source server")])

D["helm"] = dict(
 F=["Install, upgrade, roll back and inspect a release","Read a chart's values and override them per environment","Render a chart locally with helm template"],
 P=["Write charts with helpers, schema-validated values and sane defaults","Use hooks for migrations and helm test for smoke tests","Publish charts to an OCI registry"],
 S=["Design library charts as a shared blueprint for many services","Deliver charts with GitOps (Argo CD or Flux) and diffs","Choose between Helm and Kustomize per case"],
 E=["Own the organisation's deployment packaging standards","Run chart supply chain: signing, provenance, registries","Lead migrations between delivery models"],
 topics=["Library charts","values.schema.json","Helm hooks and their limits","Argo CD ApplicationSets","Chart signing and provenance"],
 links=[("Helm documentation","https://helm.sh/docs/","Concepts, commands, charts"),
        ("Chart template guide","https://helm.sh/docs/chart_template_guide/","Templates, functions, helpers"),
        ("Chart best practices","https://helm.sh/docs/chart_best_practices/","Conventions for maintainable charts"),
        ("Artifact Hub","https://artifacthub.io/","Find public charts and operators"),
        ("helm-unittest","https://github.com/helm-unittest/helm-unittest","Unit tests for templates"),
        ("chart-testing (ct)","https://github.com/helm/chart-testing","Lint and install-test charts in CI"),
        ("Argo CD","https://argo-cd.readthedocs.io/","GitOps for Kubernetes")])

D["operators"] = dict(
 F=["Explain CRDs, custom resources, controllers and reconcile","Use existing operators (cert-manager, CloudNativePG, Strimzi)","Read a resource's status and conditions"],
 P=["Write a CRD with schema validation","Build a simple controller with kubebuilder, Java Operator SDK or Kopf","Use owner references, finalizers and status correctly"],
 S=["Design operators for stateful systems and day-2 operations","Test with envtest and real clusters; version CRDs with conversion","Decide operator vs Helm vs managed service"],
 E=["Build platform APIs on Kubernetes for the organisation","Maintain operators at high capability levels","Contribute to the operator ecosystem"],
 topics=["controller-runtime internals","CEL validation rules","Conversion webhooks","Operator Lifecycle Manager","Crossplane and Config Connector"],
 links=[("Operator pattern","https://kubernetes.io/docs/concepts/extend-kubernetes/operator/","Kubernetes documentation"),
        ("Custom Resource Definitions","https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/","Defining and versioning CRDs"),
        ("The Kubebuilder Book","https://book.kubebuilder.io/","Building controllers in Go"),
        ("Operator SDK","https://sdk.operatorframework.io/","Operator Framework tooling"),
        ("Java Operator SDK","https://javaoperatorsdk.io/","Operators in Java"),
        ("Kopf","https://kopf.readthedocs.io/","Operators in Python"),
        ("OperatorHub","https://operatorhub.io/","Catalogue of operators"),
        ("Config Connector","https://cloud.google.com/config-connector/docs/overview","GCP resources as Kubernetes objects")])

D["servicemesh"] = dict(
 F=["Explain mTLS, workload identity and east-west vs north-south traffic","Read VirtualService, DestinationRule and AuthorizationPolicy resources","Find a pod's sidecar logs and proxy status"],
 P=["Enrol namespaces and roll out STRICT mTLS safely","Write authorisation policies and canary routes","Debug 503s and RBAC denials with istioctl"],
 S=["Decide whether a mesh is worth it, and sidecar vs ambient","Design zero-trust service-to-service security","Run mesh upgrades with revisions; keep config in GitOps"],
 E=["Own the mesh platform across clusters and environments","Design multi-cluster and multi-network meshes","Set network security strategy combining mesh, gateway and cloud controls"],
 topics=["Istio ambient mode (ztunnel and waypoints)","Kubernetes Gateway API","Envoy proxy internals","Multi-cluster Istio","SPIFFE workload identity"],
 links=[("Istio documentation","https://istio.io/latest/docs/","Concepts, tasks, reference"),
        ("Istio traffic management","https://istio.io/latest/docs/concepts/traffic-management/","Routing, resilience, gateways"),
        ("Istio security","https://istio.io/latest/docs/concepts/security/","mTLS, identity, authorisation"),
        ("Istio ambient mode","https://istio.io/latest/docs/ambient/","Sidecar-less data plane"),
        ("Kubernetes Gateway API","https://gateway-api.sigs.k8s.io/","Standard routing API"),
        ("Kiali","https://kiali.io/docs/","Service graph and mesh console"),
        ("Cloud Service Mesh","https://cloud.google.com/service-mesh/docs","Google's managed mesh"),
        ("Linkerd","https://linkerd.io/","A lighter-weight alternative")])

D["mathematics"] = dict(
 F=["Work out percentages, compound growth and risk in daily life","Read Big-O and spot a nested loop over large data","Use median and percentiles rather than averages","Know why floats are wrong for money"],
 P=["Reason about complexity when choosing data structures and queries","Apply basic probability to retries, availability and alerts","Estimate capacity and cost with orders of magnitude"],
 S=["Design experiments and read their statistics critically","Use linear algebra and statistics confidently in data and ML work","Prove or argue correctness of algorithms and migrations"],
 E=["Bring mathematical rigour to architecture and research decisions","Teach the maths behind the team's systems","Spot subtle statistical and numerical errors in others' work"],
 topics=["Personal finance: compounding and inflation","Discrete mathematics for computer science","Probability and Bayes' rule","Statistics for experiments (A/B testing)","Linear algebra for embeddings and ML","Floating-point arithmetic"],
 links=[("Mathematics for Computer Science (MIT OpenCourseWare)","https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/","Free course: logic, proofs, graphs, counting, probability"),
        ("Essence of Linear Algebra (3Blue1Brown)","https://www.3blue1brown.com/topics/linear-algebra","Visual introduction to vectors and matrices"),
        ("Khan Academy: Statistics and probability","https://www.khanacademy.org/math/statistics-probability","Free self-paced statistics"),
        ("Seeing Theory","https://seeing-theory.brown.edu/","Interactive probability and statistics"),
        ("What Every Computer Scientist Should Know About Floating-Point Arithmetic","https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html","David Goldberg's classic paper")])

D["science"] = dict(
 F=["Reproduce a bug before fixing it","Change one thing at a time and measure before and after","Write down hypotheses and results while debugging"],
 P=["Debug systematically with falsifiable hypotheses and bisection","Run fair benchmarks with baselines and error bars","Spot common biases in your own reasoning"],
 S=["Design controlled experiments and A/B tests correctly","Read papers critically and apply their results with care","Teach the method through how you run investigations"],
 E=["Build a culture of evidence and experiment across the organisation","Lead research-style work with rigour and reproducibility","Judge competing claims across fields"],
 topics=["Falsifiability (Karl Popper)","Experimental design and controls","Cognitive biases","Memory hierarchy and computer architecture","How to read a paper"],
 links=[("You and Your Research (Richard Hamming)","https://www.cs.virginia.edu/~robins/YouAndYourResearch.html","A classic talk on doing important work"),
        ("The Art of Doing Science and Engineering (Hamming)","https://press.stripe.com/the-art-of-doing-science-and-engineering","Book on thinking as a scientist-engineer"),
        ("Cargo Cult Science (Richard Feynman)","https://calteches.library.caltech.edu/51/2/CargoCult.htm","On scientific integrity"),
        ("How to Read a Paper (S. Keshav)","http://ccr.sigcomm.org/online/files/p83-keshavA.pdf","The three-pass method"),
        ("Computer Systems: A Programmer's Perspective","https://csapp.cs.cmu.edu/","How computers really work, for programmers")])

D["philosophy"] = dict(
 F=["Ask \"how do we know?\" before accepting a claim","Recognise common fallacies in debates","Know the professional codes of ethics exist and what they ask"],
 P=["Reason clearly with deduction, induction and abduction","Use razors and principles (Occam, Chesterton, Goodhart) in decisions","Raise ethical concerns about a feature constructively"],
 S=["Apply systems thinking to recurring problems and incentives","Weigh ethical trade-offs in designs with several lenses","Lead discussions with Socratic questions that improve the work"],
 E=["Shape organisational values, incentives and ethical standards","Advise on AI ethics and societal impact","Model wise judgement under uncertainty"],
 topics=["Epistemology and calibration","Logic and argument","Systems thinking","Ethics of technology and AI","Stoicism"],
 links=[("Stanford Encyclopedia of Philosophy","https://plato.stanford.edu/","Free, authoritative articles on every topic"),
        ("ACM Code of Ethics and Professional Conduct","https://www.acm.org/code-of-ethics","Computing professionals' code"),
        ("IEEE Code of Ethics","https://www.ieee.org/about/corporate/governance/p7-8.html","Engineers' code"),
        ("Thinking in Systems (Donella Meadows)","https://donellameadows.org/systems-thinking-book-sale/","Introduction to systems thinking"),
        ("Internet Encyclopedia of Philosophy: fallacies","https://iep.utm.edu/fallacy/","A catalogue of reasoning errors")])

D["goodhuman"] = dict(
 F=["Be honest about mistakes and what you do not know","Thank people specifically; review kindly","Look after your health and ask for help early"],
 P=["Give and receive feedback well","Handle disagreement with respect and evidence","Build for all users, including accessibility"],
 S=["Create psychological safety in your team","Mentor others and share credit generously","Raise ethical concerns and stand by them"],
 E=["Shape a humane, inclusive culture across the organisation","Lead with integrity under pressure","Give back to the wider community"],
 topics=["Psychological safety","Feedback models","Conflict resolution","Inclusive and accessible design","Sustainable pace and burnout"],
 links=[("Google re:Work","https://rework.withgoogle.com/","Research on team effectiveness, including psychological safety"),
        ("WHO: burn-out an occupational phenomenon","https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases","How burnout is defined"),
        ("ACM Code of Ethics","https://www.acm.org/code-of-ethics","Honesty, avoiding harm, the public good"),
        ("Web Content Accessibility Guidelines","https://www.w3.org/WAI/standards-guidelines/wcag/","Building for everyone")])

D["body"] = dict(
 F=["Explain fight-or-flight and rest-and-digest in plain words","Keep regular sleep, daily movement and real breaks","Notice your own stress signals"],
 P=["Plan hard thinking for your best hours; protect focus","Recover after on-call and crunch periods","Switch off idle resources you own"],
 S=["Set a sustainable pace and humane on-call for a team","Spot burnout signals in others and act early","Design systems that are lean in energy and cost"],
 E=["Shape a culture where health and rest are normal","Make sustainability part of architecture decisions","Model a full life, not only a full calendar"],
 topics=["The autonomic nervous system","Sleep and the body clock","How learning works: spacing and retrieval","Ergonomics and eye care","Biomimicry","Sustainable software"],
 links=[("NHS: sleep and tiredness","https://www.nhs.uk/live-well/sleep-and-tiredness/","Practical advice on sleep"),
        ("NHS: exercise","https://www.nhs.uk/live-well/exercise/","Activity guidance for adults"),
        ("NINDS: Brain Basics","https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-know-your-brain","How the brain and nervous system are organised"),
        ("AskNature","https://asknature.org/","The Biomimicry Institute's library of nature's designs"),
        ("Green Software Foundation","https://greensoftware.foundation/","Principles and practice for greener software")])
