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
        ("JUnit user guide","https://junit.org/junit5/docs/current/user-guide/","Tests, parameterised tests, extensions"),
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
        ("JUnit user guide","https://junit.org/junit5/docs/current/user-guide/","Java testing"),
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
        ("Google Cloud Well-Architected Framework","https://cloud.google.com/architecture/framework","Reliability, cost, security, performance pillars"),
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
 topics=["Dataflow streaming: windows, triggers, late data","BigLake and Iceberg on GCS","Dataplex data quality and lineage","BigQuery sharing (formerly Analytics Hub)","Professional Data Engineer exam guide"],
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
 P=["Build an MCP server with the Python SDK and test it with the Inspector","Expose read-only pipeline or warehouse tools with guardrails","Share servers with a team via project configuration"],
 S=["Design task-shaped tool sets with honest errors and compact outputs","Deploy remote servers on Cloud Run with OAuth or IAM","Integrate MCP with data pipelines without putting it on the critical path"],
 E=["Set MCP standards, review and approval process for the organisation","Build shared MCP platforms over core data and systems","Contribute to the protocol ecosystem"],
 topics=["MCP specification and transports","MCP authorisation (OAuth)","Tool design for agents","MCP Toolbox for Databases","Tool poisoning and prompt injection defences"],
 links=[("Model Context Protocol","https://modelcontextprotocol.io/","Specification, concepts and SDKs"),
        ("MCP Python SDK","https://github.com/modelcontextprotocol/python-sdk","MCPServer (formerly FastMCP) and server examples"),
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

D["cloudinside"] = dict(
 F=["Explain zones, regions and why work is spread across them","Tell a virtual machine from a container and a serverless function","Name what the provider secures and what you secure"],
 P=["Choose zones and regions for a service's availability, latency and data residency","Read a bill and trace each line to a layer: compute, storage, network","Explain what a managed service still leaves to you"],
 S=["Design for a machine, a zone or a region failing, and test it","Choose isolation (VM, container, sandbox) for untrusted or multi-tenant work","Estimate cost from first principles, including egress and copies"],
 E=["Set organisation standards for failure domains, tenancy and shared responsibility","Lead decisions on regions, providers and lock-in with the layers in view","Teach how the cloud works underneath, not only which button to press"],
 topics=["Failure domains: machine, zone, region","Hypervisors and microVMs","Container isolation and sandboxes","Cluster scheduling and bin packing","The shared responsibility model"],
 links=[("Firecracker","https://github.com/firecracker-microvm/firecracker","MicroVMs built at AWS for services such as Lambda, open source"),
        ("gVisor","https://github.com/google/gvisor","An application kernel that sandboxes containers"),
        ("Kubernetes","https://github.com/kubernetes/kubernetes","The open-source scheduler and orchestrator for containers"),
        ("The Borg paper","https://research.google.com/pubs/pub43438.html?authuser=1","Google's paper on Borg, as linked from the Kubernetes README")])

D["cloudcompare"] = dict(
 F=["Map common services across GCP, AWS and Azure","Explain projects vs accounts vs subscriptions","Use each provider's CLI for basic tasks"],
 P=["Translate a design from one cloud to another, including IAM and networking","Compare prices for a workload, including egress","Use Terraform across providers"],
 S=["Choose a provider for a workload with written trade-offs","Design portable architectures where it matters, and accept lock-in deliberately","Plan data residency and region choices"],
 E=["Set the organisation's cloud strategy, contracts and multi-cloud policy","Lead migrations between clouds or from on-premises","Govern cost, security and compliance across providers"],
 topics=["Well-Architected frameworks of each provider","Cloud IAM models compared","Cross-cloud networking and egress costs","Open table formats for portability","FinOps practices"],
 links=[("Google Cloud: compare AWS and Azure services","https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison","Google's official service mapping"),
        ("Azure for AWS professionals","https://learn.microsoft.com/en-us/azure/architecture/aws-professional/","Microsoft's AWS-to-Azure mapping"),
        ("Google Cloud Well-Architected Framework","https://cloud.google.com/architecture/framework","Google's design pillars"),
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
 S=["Assess security, cost, privacy and regulation of a Web3 design","Design knowledge graphs and ontologies for a domain","Model product data with shared vocabularies (schema.org Product, GTIN codes)"],
 E=["Set strategy on decentralised and linked-data technologies","Lead audits and governance for on-chain systems","Shape open data standards in a sector"],
 topics=["Ethereum and proof of stake","Smart contract security","Layer 2 rollups","RDF, OWL and SHACL","Knowledge graphs for AI grounding"],
 links=[("ethereum.org developers","https://ethereum.org/en/developers/","Concepts and tutorials"),
        ("Solidity documentation","https://docs.soliditylang.org/","Language reference"),
        ("W3C Semantic Web","https://www.w3.org/2001/sw/wiki/Main_Page","RDF, SPARQL, OWL standards"),
        ("JSON-LD","https://json-ld.org/","Linked data in JSON"),
        ("schema.org","https://schema.org/","Shared vocabulary for structured data"),
        ("SPARQL 1.1 Query Language","https://www.w3.org/TR/sparql11-query/","The specification"),
        ("schema.org vocabulary source","https://github.com/schemaorg/schemaorg","The Product, Offer and other type definitions")])

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

D["agentsgcp"] = dict(
 F=["Explain where an agent runs, what it can reach and who sees its logs","Run a containerised task as a Cloud Run job","Keep secrets in Secret Manager"],
 P=["Give each agent its own least-privilege service account","Trigger agent jobs from Scheduler, Pub/Sub or a Workflow","Preview agent changes on a tagged, no-traffic revision"],
 S=["Design an agent platform with workspaces, approvals and audit","Set budgets, timeouts and network limits for agents","Evaluate agents on real tasks before widening their access"],
 E=["Own the organisation's policy for where agents run and what they touch","Balance hosted agent services against self-run ones","Make agent work auditable end to end"],
 topics=["Cloud Workstations","Cloud Run jobs","Workflows and Eventarc","Secret Manager and IAM","VPC Service Controls","Vertex AI Model Garden"],
 links=[("Cloud Workstations","https://cloud.google.com/workstations/docs","Managed development environments"),
        ("Cloud Run jobs","https://cloud.google.com/run/docs/create-jobs","Containers that run to completion"),
        ("Workflows","https://cloud.google.com/workflows/docs","Orchestrate steps and services"),
        ("Secret Manager","https://cloud.google.com/secret-manager/docs","Store and audit secrets"),
        ("Vertex AI Model Garden","https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models","Google and partner models")])

D["cyber"] = dict(
 F=["Explain how a typical intrusion unfolds","Spot phishing and report incidents quickly","Know that you only test systems you may test"],
 P=["Map your system's exposure to common attacker techniques","Log the signals an investigation needs","Follow the incident plan during an incident"],
 S=["Write and tune detections; run a tabletop exercise","Lead containment and recovery in an incident","Design defence in depth for a product"],
 E=["Own the organisation's security operations and incident response","Run red, blue and purple team programmes","Build a security culture across teams"],
 topics=["MITRE ATT&CK tactics and techniques","Detection engineering","Incident response","Threat modelling","Responsible disclosure"],
 links=[("MITRE ATT&CK data on GitHub","https://github.com/mitre-attack/attack-stix-data","The ATT&CK knowledge base as STIX data"),
        ("OWASP Cheat Sheet Series","https://github.com/OWASP/CheatSheetSeries","Concise, practical security guidance")])

D["quantum"] = dict(
 F=["Explain qubits, superposition and entanglement in plain words","Say what quantum computers are and are not good for","Explain why Shor's algorithm threatens RSA and elliptic curves"],
 P=["Inventory where your systems use public-key cryptography","Keep crypto libraries current and follow their post-quantum options","Build and run a simple circuit on a simulator"],
 S=["Plan a post-quantum migration, long-lived secrets first","Design for crypto agility","Judge vendor quantum claims critically"],
 E=["Own the organisation's post-quantum roadmap","Advise on where quantum computing could genuinely help","Track standards and research and translate them for teams"],
 topics=["Qubits and measurement","Shor's and Grover's algorithms","Post-quantum cryptography (ML-KEM, ML-DSA, SLH-DSA)","Quantum error correction","Hybrid quantum-classical algorithms"],
 links=[("Open Quantum Safe (liboqs)","https://github.com/open-quantum-safe/liboqs","Open-source post-quantum algorithms, including the NIST standards"),
        ("Qiskit","https://github.com/Qiskit/qiskit","Open-source SDK for quantum circuits")])

D["kotlin"]=dict(
 F=["Read Kotlin code beside Java","Use null safety, data classes and when","Write and run a test with kotlin.test"],
 P=["Build a service in Kotlin with Spring Boot or Ktor","Handle Java interop and platform types safely","Use coroutines for asynchronous work"],
 S=["Design structured concurrency and cancellation","Mix Kotlin and Java in one codebase cleanly","Set style and lint rules for a team"],
 E=["Lead a Java-to-Kotlin migration","Share code across platforms with Kotlin Multiplatform","Teach idiomatic Kotlin and review for it"],
 topics=["Null safety and platform types","Sealed types and exhaustive when","Coroutines and structured concurrency","Gradle Kotlin DSL","Kotlin Multiplatform"],
 links=[("Kotlin documentation","https://kotlinlang.org/docs/home.html","The official docs, from JetBrains"),
        ("Coroutines overview","https://kotlinlang.org/docs/coroutines-overview.html","Asynchronous code in Kotlin"),
        ("kotlinx.coroutines","https://github.com/Kotlin/kotlinx.coroutines","The coroutines library's source and guide")])

D["go"]=dict(
 F=["Write and run a small Go program","Handle errors as values","Write a table-driven test"],
 P=["Build an HTTP service with the standard library","Use goroutines, channels and context safely","Run tests with the race detector and coverage"],
 S=["Design packages and interfaces for a large codebase","Profile and tune with pprof","Read and debug cloud tools written in Go"],
 E=["Set Go standards across teams","Build operators or platform tooling in Go","Teach Go's concurrency model and review for it"],
 topics=["Errors and wrapping","Goroutines, channels and context","Interfaces and composition","Modules and versioning","Profiling with pprof"],
 links=[("A Tour of Go","https://go.dev/tour/","Interactive introduction"),
        ("Effective Go","https://go.dev/doc/effective_go","How to write idiomatic Go"),
        ("The Go source","https://github.com/golang/go","The language, compiler and standard library")])

D["javascript"]=dict(
 F=["Use let, const, functions, arrays and objects","Explain closures and the event loop","Change a page with the DOM and events, no framework"],
 P=["Write async code with promises and async/await","Organise code in modules and build it","Check feature support with Baseline"],
 S=["Design state and reactivity without leaning on a framework","Keep the main thread free; use Web Workers","Adopt TypeScript and write typed APIs"],
 E=["Choose and migrate frameworks on evidence","Set JavaScript and TypeScript standards across teams","Follow and evaluate TC39 proposals"],
 topics=["Closures and scope","The event loop and promises","Modules","Immutability and copying methods","Web Components","TypeScript"],
 links=[("MDN JavaScript Guide","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide","A thorough, free guide to the language"),
        ("TC39 finished proposals","https://github.com/tc39/proposals/blob/main/finished-proposals.md","What each edition added"),
        ("The ECMAScript specification (latest draft)","https://tc39.es/ecma262/","The standard itself"),
        ("Baseline on web.dev","https://web.dev/baseline","Which features are safe to use everywhere")],
 sources=[("TC39 finished proposals (feature and expected publication year)","https://github.com/tc39/proposals/blob/main/finished-proposals.md"),
          ("TC39 process document (Stage 4 needs two compatible implementations passing Test262)","https://tc39.es/process-document/"),
          ("tc39/ecma262 tags (the es2026 edition)","https://github.com/tc39/ecma262/tags"),
          ("Wikipedia: ECMAScript version history (the ES2015 feature set)","https://en.wikipedia.org/wiki/ECMAScript_version_history"),
          ("MDN: Baseline compatibility","https://github.com/mdn/content/blob/main/files/en-us/glossary/baseline/compatibility/index.md"),
          ("MDN: Closures","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/closures/index.md"),
          ("MDN: JavaScript execution model (job queue, run to completion)","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/execution_model/index.md"),
          ("MDN: Modules","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/modules/index.md"),
          ("MDN: Inheritance and the prototype chain","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/inheritance_and_the_prototype_chain/index.md"),
          ("MDN: Using promises","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/using_promises/index.md"),
          ("MDN: Web Components","https://github.com/mdn/content/blob/main/files/en-us/web/api/web_components/index.md"),
          ("MDN: Number (IEEE 754 double precision)","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/number/index.md"),
          ("MDN: Equality (==) converts types","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/equality/index.md"),
          ("MDN: Nullish coalescing (??) and ||","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/nullish_coalescing/index.md"),
          ("MDN: Array.prototype.sort (in place)","https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/sort/index.md"),
          ("MDN: Web Workers API","https://github.com/mdn/content/blob/main/files/en-us/web/api/web_workers_api/index.md")])

D["banking"]=dict(
 F=["Explain how channels, core banking, schemes and the ledger fit together","Explain why every payment step must be idempotent","Read p50, p99 and p99.9 and say which one customers feel"],
 P=["Build a payment flow that meets an instant scheme's deadline","Map a message to and from ISO 20022","Load-test without coordinated omission"],
 S=["Design for 24/7 operation with no batch window","Set and enforce a latency budget per hop","Choose between in-memory, lock-free and conventional designs by requirement"],
 E=["Lead a core banking or scheme migration","Set resilience and latency standards across a bank","Design ultra-low-latency trading infrastructure"],
 topics=["Core banking and the general ledger","Instant payment schemes","ISO 20022","Tail latency and latency budgets","The LMAX architecture and the Disruptor","Kernel bypass and co-location"],
 links=[("The LMAX Architecture (Martin Fowler)","https://martinfowler.com/articles/lmax.html","In-memory, single-threaded, event-sourced trading"),
        ("wrk2 README: coordinated omission","https://github.com/giltene/wrk2","Why most load tests miss the slow periods"),
        ("HdrHistogram","https://github.com/HdrHistogram/HdrHistogram","Recording latency across a wide range"),
        ("JEP 439: Generational ZGC","https://openjdk.org/jeps/439","A low-pause collector for the JVM")],
 sources=[("Wikipedia: Challenger bank","https://en.wikipedia.org/wiki/Challenger_bank"),("Wikipedia: Monzo","https://en.wikipedia.org/wiki/Monzo"),("Wikipedia: Revolut","https://en.wikipedia.org/wiki/Revolut"),("Wikipedia: Starling Bank","https://en.wikipedia.org/wiki/Starling_Bank"),
          ("Wikipedia: Core banking","https://en.wikipedia.org/wiki/Core_banking"),("Wikipedia: Instant payment","https://en.wikipedia.org/wiki/Instant_payment"),
          ("Wikipedia: Single Euro Payments Area (SCT Inst)","https://en.wikipedia.org/wiki/Single_Euro_Payments_Area"),("Wikipedia: Faster Payment System (UK)","https://en.wikipedia.org/wiki/Faster_Payment_System_(United_Kingdom)"),
          ("Wikipedia: FedNow","https://en.wikipedia.org/wiki/FedNow"),("Wikipedia: ISO 20022","https://en.wikipedia.org/wiki/ISO_20022"),("Wikipedia: Mainframe computer","https://en.wikipedia.org/wiki/Mainframe_computer"),("Wikipedia: COBOL","https://en.wikipedia.org/wiki/COBOL"),
          ("Wikipedia: Low latency (capital markets)","https://en.wikipedia.org/wiki/Low_latency_(capital_markets)"),("Wikipedia: High-frequency trading (co-location)","https://en.wikipedia.org/wiki/High-frequency_trading"),
          ("Wikipedia: Optical fiber (refractive index)","https://en.wikipedia.org/wiki/Optical_fiber"),("Martin Fowler: The LMAX Architecture (2011)","https://martinfowler.com/articles/lmax.html"),
          ("OpenJDK JEP 333: ZGC, and JEP 439: Generational ZGC","https://openjdk.org/jeps/439"),("Wikipedia: Nagle's algorithm (TCP_NODELAY)","https://en.wikipedia.org/wiki/Nagle%27s_algorithm"),
          ("Wikipedia: Data Plane Development Kit","https://en.wikipedia.org/wiki/Data_Plane_Development_Kit"),("wrk2 README (coordinated omission)","https://github.com/giltene/wrk2")])

D["specs"]=dict(
 F=["Read MUST, SHOULD and MAY as RFC 2119 and RFC 8174 define them","Find the specification behind a format or protocol you use every day","Tell an RFC that is a standard from one that is informational"],
 P=["Settle a disagreement by quoting the section of a spec","Describe an API in OpenAPI, AsyncAPI, GraphQL or Protobuf","Check which RFCs a document obsoletes before you cite it"],
 S=["Choose an interface description by requirement","Write a specification other teams can build from","Track proposals that will change your stack (JEPs, PEPs, TC39 stages)"],
 E=["Represent your organisation in a standards body or working group","Set the interface and versioning standards across an organisation","Contribute to a specification or its conformance tests"],
 topics=["RFC 2119 key words","IETF, W3C, WHATWG, TC39 and ISO","HTTP, TLS, OAuth and JWT RFCs","JSON, CSV, Unicode and dates","OpenAPI, AsyncAPI, GraphQL, Protobuf and CloudEvents","Language specifications and enhancement proposals"],
 links=[("RFC 2119: key words for requirement levels","https://www.rfc-editor.org/rfc/rfc2119","MUST, SHOULD, MAY"),
        ("RFC 9110: HTTP Semantics","https://www.rfc-editor.org/rfc/rfc9110","The HTTP every version shares"),
        ("The OpenAPI Specification","https://github.com/OAI/OpenAPI-Specification","Describing HTTP APIs")],
 sources=[("RFC 2119","https://www.rfc-editor.org/rfc/rfc2119"),("RFC 8174","https://www.rfc-editor.org/rfc/rfc8174"),("RFC 9110","https://www.rfc-editor.org/rfc/rfc9110"),
          ("RFC 9457","https://www.rfc-editor.org/rfc/rfc9457"),("RFC 8259","https://www.rfc-editor.org/rfc/rfc8259"),("RFC 4180","https://www.rfc-editor.org/rfc/rfc4180"),
          ("RFC 3629","https://www.rfc-editor.org/rfc/rfc3629"),("RFC 3339","https://www.rfc-editor.org/rfc/rfc3339"),("RFC 8446","https://www.rfc-editor.org/rfc/rfc8446"),
          ("RFC 6749","https://www.rfc-editor.org/rfc/rfc6749"),("RFC 7636","https://www.rfc-editor.org/rfc/rfc7636"),("RFC 7519","https://www.rfc-editor.org/rfc/rfc7519"),
          ("Wikipedia: Request for Comments","https://en.wikipedia.org/wiki/Request_for_Comments"),("W3C standards","https://www.w3.org/standards/"),
          ("Wikipedia: World Wide Web Consortium","https://en.wikipedia.org/wiki/World_Wide_Web_Consortium"),("Wikipedia: WHATWG","https://en.wikipedia.org/wiki/WHATWG"),
          ("TC39 process document","https://github.com/tc39/process-document"),("ECMA-262 repository","https://github.com/tc39/ecma262"),
          ("JEP 1","https://openjdk.org/jeps/1"),("PEP 1","https://peps.python.org/pep-0001/"),("Java SE Specifications","https://docs.oracle.com/javase/specs/"),
          ("OpenAPI Specification README","https://github.com/OAI/OpenAPI-Specification"),("AsyncAPI specification","https://github.com/asyncapi/spec"),
          ("GraphQL specification","https://github.com/graphql/graphql-spec"),("Protocol Buffers overview","https://github.com/protocolbuffers/protocolbuffers.github.io"),
          ("Wikipedia: gRPC","https://en.wikipedia.org/wiki/GRPC"),("CloudEvents","https://github.com/cloudevents/spec"),
          ("OpenTelemetry specification","https://github.com/open-telemetry/opentelemetry-specification"),("OCI Image Format","https://github.com/opencontainers/image-spec"),
          ("Model Context Protocol repository","https://github.com/modelcontextprotocol/modelcontextprotocol"),("JSON Schema specification","https://json-schema.org/specification"),
          ("CommonMark","https://github.com/commonmark/commonmark-spec"),("TOML","https://github.com/toml-lang/toml"),("Apache Parquet format","https://github.com/apache/parquet-format"),
          ("Wikipedia: Apache Iceberg","https://en.wikipedia.org/wiki/Apache_Iceberg"),("Wikipedia: Unicode (UTF-8 on the web)","https://en.wikipedia.org/wiki/Unicode"),
          ("Wikipedia: ISO 8601","https://en.wikipedia.org/wiki/ISO_8601"),("Wikipedia: IEEE 754","https://en.wikipedia.org/wiki/IEEE_754"),
          ("Wikipedia: POSIX","https://en.wikipedia.org/wiki/POSIX"),("Wikipedia: SQL (ISO/IEC 9075)","https://en.wikipedia.org/wiki/SQL"),
          ("Wikipedia: OpenID (OpenID Connect)","https://en.wikipedia.org/wiki/OpenID"),("Semantic Versioning","https://semver.org/")])

D["retailcloud"]=dict(
 F=["Name the systems a retailer connects and what each one owns","Explain why a till must keep selling offline","Explain the difference between an event and an API call"],
 P=["Build store-and-forward with idempotent receivers","Map a retail flow onto AWS, Azure or Google Cloud services","Connect a data centre to a cloud over a private link"],
 S=["Decide what runs in the store, the data centre and the cloud, by requirement","Design one view of stock across channels","Price data transfer before splitting a system across clouds"],
 E=["Set a hybrid and multi-cloud strategy with named reasons","Lead the integration of an acquired company on another cloud","Keep an exit plan from a provider tested, not just written"],
 topics=["Point of sale and store systems","EDI with suppliers","Events, APIs and the outbox","Hybrid cloud and on-premises offerings","Multi-cloud and its costs","Switching charges under the EU Data Act"],
 links=[("What is AWS Outposts?","https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html","AWS infrastructure on your premises"),
        ("Azure Arc overview","https://learn.microsoft.com/en-us/azure/azure-arc/overview","Manage resources outside Azure"),
        ("Google Distributed Cloud connected overview","https://cloud.google.com/distributed-cloud/edge/latest/docs/overview","When to use it, and its limits")],
 sources=[("Wikipedia: Point of sale","https://en.wikipedia.org/wiki/Point_of_sale"),("Wikipedia: Electronic data interchange","https://en.wikipedia.org/wiki/Electronic_data_interchange"),
          ("Wikipedia: Cloud computing (hybrid cloud, cloud bursting)","https://en.wikipedia.org/wiki/Cloud_computing"),("Wikipedia: Multicloud","https://en.wikipedia.org/wiki/Multicloud"),
          ("Wikipedia: Data Act (European Union)","https://en.wikipedia.org/wiki/Data_Act_(European_Union)"),
          ("Amazon EventBridge: what is it","https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html"),("Azure Service Bus overview","https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview"),
          ("Pub/Sub overview","https://cloud.google.com/pubsub/docs/overview"),("AWS Direct Connect","https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html"),
          ("Azure ExpressRoute","https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction"),("Cloud Interconnect overview","https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview"),
          ("Cross-Cloud Interconnect overview","https://cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview"),
          ("What is AWS Outposts?","https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"),("What is Azure Local?","https://learn.microsoft.com/en-us/azure/azure-local/overview"),
          ("Google Distributed Cloud connected overview","https://cloud.google.com/distributed-cloud/edge/latest/docs/overview"),("Azure Arc overview","https://learn.microsoft.com/en-us/azure/azure-arc/overview"),
          ("GKE Multi-Cloud","https://cloud.google.com/kubernetes-engine/multi-cloud/docs"),("Azure API Management self-hosted gateway","https://learn.microsoft.com/en-us/azure/api-management/self-hosted-gateway-overview"),
          ("What is Apigee hybrid?","https://cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid"),("What is AWS IoT Greengrass?","https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html"),
          ("What is Amazon Personalize?","https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html"),("Google AI Commerce Search overview","https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/overview"),
          ("Google Cloud network pricing","https://cloud.google.com/vpc/network-pricing")])

D["rust"]=dict(
 F=["Explain ownership and borrowing","Use Result, Option and match","Build and test with Cargo"],
 P=["Write a CLI or service in Rust","Use traits, iterators and error types well","Keep Clippy clean and the code formatted"],
 S=["Design with lifetimes and generics","Write async Rust and choose a runtime","Wrap unsafe or foreign code behind safe interfaces"],
 E=["Lead Rust adoption where safety and speed matter","Write libraries other languages call","Teach Rust and review for soundness"],
 topics=["Ownership, borrowing and lifetimes","Traits and generics","Error handling with Result","Async Rust","Unsafe Rust and FFI"],
 links=[("The Rust Programming Language (the book)","https://doc.rust-lang.org/book/","The official book"),
        ("The book's source","https://github.com/rust-lang/book","Read and contribute on GitHub"),
        ("Rustlings","https://github.com/rust-lang/rustlings","Small exercises to learn by doing")])

D["buildtools"]=dict(
 F=["Run a Maven, Gradle and npm build from the wrapper or lockfile","Name the lifecycle phases or tasks a build runs","Add a dependency and read the dependency tree"],
 P=["Pin versions with a BOM, a version catalog or a lockfile","Explain why a transitive version won and override it","Make CI builds reproducible and cached"],
 S=["Design a multi-module or monorepo build","Use the Gradle build and configuration caches","Set an install-script and dependency-source policy"],
 E=["Set build standards across an organisation","Lead migrations between build tools","Secure the build supply chain end to end"],
 topics=["The Maven lifecycle and plugins","Gradle tasks, caches and version catalogs","Lockfiles and npm ci","pnpm's store and strict node_modules","Bundlers: webpack and Vite"],
 links=[("Introduction to the Maven build lifecycle","https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html","Phases and bindings"),
        ("Gradle User Manual","https://docs.gradle.org/current/userguide/userguide.html","Wrapper, Daemon, caches, catalogs"),
        ("npm Docs","https://docs.npmjs.com/","package.json, lockfiles, scripts"),
        ("pnpm: Motivation","https://pnpm.io/motivation","The store and the non-flat node_modules"),
        ("Vite guide","https://vite.dev/guide/","Dev server and production build")],
 sources=[("Maven: build lifecycle (source)","https://github.com/apache/maven-site/blob/master/content/markdown/guides/introduction/introduction-to-the-lifecycle.md"),
          ("Maven: dependency mechanism (source)","https://github.com/apache/maven-site/blob/master/content/markdown/guides/introduction/introduction-to-dependency-mechanism.md"),
          ("Maven Wrapper (source)","https://github.com/apache/maven-site/blob/master/content/markdown/tools/mavenwrapper.md"),
          ("Gradle user guide: build lifecycle, Wrapper, Daemon, build cache, configuration cache, version catalogs (source)","https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/docs/userguide"),
          ("Android: configure your build","https://developer.android.com/build"),
          ("npm ci","https://github.com/npm/cli/blob/latest/docs/lib/content/commands/npm-ci.md"),
          ("package-lock.json","https://github.com/npm/cli/blob/latest/docs/lib/content/configuring-npm/package-lock-json.md"),
          ("npm scripts","https://github.com/npm/cli/blob/latest/docs/lib/content/using-npm/scripts.md"),
          ("npm CHANGELOG (npm 12 breaking changes)","https://github.com/npm/cli/blob/latest/CHANGELOG.md"),
          ("npm config definitions (ignore-scripts, allow-git, allow-remote, allow-scripts)","https://github.com/npm/cli/blob/latest/workspaces/config/lib/definitions/definitions.js"),
          ("node-semver: caret and tilde ranges","https://github.com/npm/node-semver"),
          ("pnpm: Motivation (source)","https://github.com/pnpm/pnpm.io/blob/main/docs/motivation.md"),
          ("pnpm install (source)","https://github.com/pnpm/pnpm.io/blob/main/docs/cli/install.md"),
          ("Yarn: Plug'n'Play","https://yarnpkg.com/features/pnp"),
          ("yarn install","https://yarnpkg.com/cli/install"),
          ("Corepack README (bundled Node.js versions)","https://github.com/nodejs/node/blob/main/deps/corepack/README.md"),
          ("Vite guide (source)","https://github.com/vitejs/vite/blob/main/docs/guide/index.md"),
          ("Spring Boot Maven plugin: spring-boot-dependencies","https://docs.spring.io/spring-boot/maven-plugin/using.html"),
          ("Wikipedia: Make, Apache Ant, Apache Maven, Gradle, npm, webpack, Bazel, Yarn, pnpm, Vite","https://en.wikipedia.org/wiki/Build_automation")])

D["awsdata"]=dict(
 F=["Name the AWS service for each data stage","Land files in S3 and query them with Athena","Explain IAM roles for data jobs"],
 P=["Build a pipeline: S3 raw, Glue, curated Parquet or Iceberg, Athena","Use Lake Formation to grant table access","Model with dbt on Athena or Redshift"],
 S=["Choose between Athena and Redshift, Glue and EMR, Kinesis and MSK","Design a governed data lake with a catalog","Plan cost, regions and data residency"],
 E=["Own the organisation's AWS data architecture","Lead migrations between clouds or from on-premises","Set data platform standards across teams"],
 topics=["S3 Tables and Apache Iceberg","Glue jobs and crawlers","Lake Formation permissions","Redshift Serverless","Kinesis and MSK streaming"],
 links=[("AWS Glue documentation","https://docs.aws.amazon.com/glue/","ETL and the Data Catalog"),
        ("Amazon Athena documentation","https://docs.aws.amazon.com/athena/","SQL on S3"),
        ("Amazon Redshift documentation","https://docs.aws.amazon.com/redshift/","The data warehouse"),
        ("AWS Lake Formation documentation","https://docs.aws.amazon.com/lake-formation/","Fine-grained data access"),
        ("AWS SDK for pandas","https://github.com/aws/aws-sdk-pandas","Open-source pandas integration for S3, Athena, Glue and Redshift")])

D["azuredata"]=dict(
 F=["Name the Azure service for each data stage","Land files in Data Lake Storage and query them with SQL","Explain managed identities for data jobs"],
 P=["Build a pipeline: Data Lake Storage raw, Data Factory or Spark, curated Delta or Iceberg, SQL","Grant access with Azure roles and ACLs together","Run and monitor Data Factory pipelines from the CLI"],
 S=["Choose between Fabric and separate Azure services","Design a governed lake with Purview","Plan cost with access tiers, lifecycle policies and capacity"],
 E=["Own the organisation's Azure data architecture","Lead migrations between clouds or from on-premises","Set data platform standards across teams"],
 topics=["Data Lake Storage and the hierarchical namespace","Microsoft Fabric and OneLake","Data Factory and change data capture","Event Hubs and its Kafka endpoint","Azure roles, ACLs and Purview"],
 links=[("Azure Data Lake Storage introduction","https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction","The lake's storage"),
        ("What is Microsoft Fabric?","https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview","The analytics platform"),
        ("Azure Data Factory introduction","https://learn.microsoft.com/en-us/azure/data-factory/introduction","Pipelines and copy"),
        ("Access control model in Data Lake Storage","https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control-model","Roles, conditions and ACLs together")],
 sources=[("Data Lake Storage introduction","https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction"),("What is Event Hubs?","https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about"),
          ("Event Hubs for Apache Kafka","https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview"),("Data Factory introduction","https://learn.microsoft.com/en-us/azure/data-factory/introduction"),
          ("Change data capture in Data Factory","https://learn.microsoft.com/en-us/azure/data-factory/concepts-change-data-capture"),("What is Microsoft Fabric?","https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview"),
          ("OneLake overview","https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview"),("Fabric Data Warehouse","https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing"),
          ("What is Azure Synapse?","https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is"),("Synapse serverless SQL pool","https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/on-demand-workspace-overview"),
          ("What is Azure Databricks?","https://learn.microsoft.com/en-us/azure/databricks/introduction/"),("Azure Stream Analytics","https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction"),
          ("Apache Airflow jobs in Fabric","https://learn.microsoft.com/en-us/fabric/data-factory/apache-airflow-jobs-concepts"),("Azure Data Explorer","https://learn.microsoft.com/en-us/azure/data-explorer/data-explorer-overview"),
          ("Microsoft Purview","https://learn.microsoft.com/en-us/purview/purview"),("What is Power BI?","https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview"),
          ("Managed identities","https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview"),("Access control model in Data Lake Storage","https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control-model"),
          ("Blob access tiers","https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview"),("Blob lifecycle management","https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview"),
          ("Pause and resume a Fabric capacity","https://learn.microsoft.com/en-us/fabric/enterprise/pause-resume"),("Cost Management best practices","https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices"),
          ("Azure CLI help: storage","https://github.com/Azure/azure-cli/blob/dev/src/azure-cli/azure/cli/command_modules/storage/_help.py"),
          ("Azure CLI help: eventhubs","https://github.com/Azure/azure-cli/blob/dev/src/azure-cli/azure/cli/command_modules/eventhubs/_help.py"),
          ("Azure CLI help: role","https://github.com/Azure/azure-cli/blob/dev/src/azure-cli/azure/cli/command_modules/role/_help.py"),
          ("Azure CLI extension help: datafactory","https://github.com/Azure/azure-cli-extensions/blob/main/src/datafactory/azext_datafactory/generated/_help.py")])

D["atob"]=dict(
 F=["Tell business, solution and enterprise architecture apart","Say whether a piece of work is strategic, tactical or temporary","Draw today's system (A) and the target (B)"],
 P=["Plan transition states between A and B, each one deployable","Use strangler fig, parallel change or branch by abstraction for a real change","Write down the source of truth for each piece of data at each state"],
 S=["Design transitional architecture and plan its removal","Take on tactical debt deliberately, with an owner and an exit date","Lead a legacy displacement without a big bang"],
 E=["Set how an organisation plans and funds transitions, not only targets","Govern a portfolio of strategic, tactical and temporary work","Teach teams to engineer the route, not only the destination"],
 topics=["Baseline, transition and target states","Transitional architecture","Technical debt, prudent and deliberate","Patterns of legacy displacement","Feature toggles, dark launching and canary releases"],
 links=[("Patterns of Legacy Displacement (Cartwright, Horn, Lewis)","https://martinfowler.com/articles/patterns-legacy-displacement/","The whole catalogue"),
        ("Transitional Architecture","https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html","Building what you will remove"),
        ("Technical Debt Quadrant","https://martinfowler.com/bliki/TechnicalDebtQuadrant.html","Prudent, reckless, deliberate, inadvertent")],
 sources=[("Wikipedia: Solution architecture","https://en.wikipedia.org/wiki/Solution_architecture"),("Wikipedia: Business architecture","https://en.wikipedia.org/wiki/Business_architecture"),
          ("Wikipedia: Enterprise architecture","https://en.wikipedia.org/wiki/Enterprise_architecture"),("Wikipedia: The Open Group Architecture Framework (TOGAF domains)","https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework"),("Wikipedia: Technical debt","https://en.wikipedia.org/wiki/Technical_debt"),
          ("Cartwright, Horn, Lewis: Transitional Architecture","https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html"),("Cartwright, Horn, Lewis: Patterns of Legacy Displacement","https://martinfowler.com/articles/patterns-legacy-displacement/"),
          ("Fowler: Strangler Fig","https://martinfowler.com/bliki/StranglerFigApplication.html"),("Sato: Parallel Change","https://martinfowler.com/bliki/ParallelChange.html"),("Fowler: Branch By Abstraction","https://martinfowler.com/bliki/BranchByAbstraction.html"),
          ("Hodgson: Feature Toggles","https://martinfowler.com/articles/feature-toggles.html"),("Cartwright, Horn, Lewis: Legacy Mimic","https://martinfowler.com/articles/patterns-legacy-displacement/legacy-mimic.html"),
          ("Cartwright, Horn, Lewis: Event Interception","https://martinfowler.com/articles/patterns-legacy-displacement/event-interception.html"),("Fowler: Dark Launching","https://martinfowler.com/bliki/DarkLaunching.html"),
          ("Sato: Canary Release","https://martinfowler.com/bliki/CanaryRelease.html"),("Fowler: Technical Debt","https://martinfowler.com/bliki/TechnicalDebt.html"),("Fowler: Technical Debt Quadrant","https://martinfowler.com/bliki/TechnicalDebtQuadrant.html"),
          ("Fowler: Sacrificial Architecture","https://martinfowler.com/bliki/SacrificialArchitecture.html")])

D["realtime"]=dict(
 F=["Tell hard, firm and soft real time from near real time","Open an EventSource or a WebSocket and handle its messages","Explain why a browser cannot read a Kafka topic directly"],
 P=["Build a gateway that consumes Kafka and pushes to browsers","Resume after a reconnect with Last-Event-ID or a refetch","Authenticate and scope long-lived connections"],
 S=["Choose polling, SSE, WebSockets, GraphQL subscriptions or a managed service by requirement","Design fan-out across gateway instances","Set and measure a delivery target, such as p99 within two seconds"],
 E=["Set real-time standards across an organisation's products","Run connection-holding services at scale","Decide build or buy for real-time infrastructure"],
 topics=["Real-time and near-real-time deadlines","Server-sent events and EventSource","WebSockets and backpressure","GraphQL subscriptions over WebSocket or SSE","Kafka consumer groups and fan-out"],
 links=[("MDN: Using server-sent events","https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events","The event stream format and EventSource"),
        ("MDN: The WebSocket API","https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API","Two-way connections in the browser"),
        ("graphql-sse","https://github.com/enisdenjo/graphql-sse","GraphQL over server-sent events")],
 sources=[("Wikipedia: Real-time computing (hard, firm, soft; near real-time)","https://en.wikipedia.org/wiki/Real-time_computing"),("Wikipedia: Push technology (long polling)","https://en.wikipedia.org/wiki/Push_technology"),
          ("Wikipedia: Apache Kafka","https://en.wikipedia.org/wiki/Apache_Kafka"),("MDN: Using server-sent events","https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events"),("MDN: EventSource","https://developer.mozilla.org/en-US/docs/Web/API/EventSource"),
          ("WHATWG HTML: Server-sent events","https://html.spec.whatwg.org/multipage/server-sent-events.html"),("MDN: The WebSocket API","https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API"),("RFC 6455: The WebSocket Protocol","https://www.rfc-editor.org/rfc/rfc6455"),
          ("RFC 6202: Long polling and streaming","https://www.rfc-editor.org/rfc/rfc6202"),("MDN: WebTransport API","https://developer.mozilla.org/en-US/docs/Web/API/WebTransport_API"),("MDN: Push API","https://developer.mozilla.org/en-US/docs/Web/API/Push_API"),
          ("GraphQL specification: Execution","https://github.com/graphql/graphql-spec"),("graphql-ws protocol","https://github.com/enisdenjo/graphql-ws/blob/master/PROTOCOL.md"),("graphql-sse protocol","https://github.com/enisdenjo/graphql-sse/blob/master/PROTOCOL.md"),
          ("AWS AppSync: real-time data","https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html"),("API Gateway WebSocket APIs","https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html"),
          ("Azure Web PubSub","https://learn.microsoft.com/en-us/azure/azure-web-pubsub/overview"),("ASP.NET Core SignalR","https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction")])

D["patterns"]=dict(
 F=["Name the five SOLID principles and the smell each one fixes","Recognise Strategy, Observer, Decorator, Adapter and Builder in code you read","Explain why a subclass must keep its parent's promises"],
 P=["Refactor a growing switch into a strategy or a sealed type","Inject dependencies so logic is testable without infrastructure","Name a pattern in a code review, and say why it fits"],
 S=["Decide when a pattern earns its place and when it is speculative","Design module boundaries with dependency inversion","Keep an inheritance hierarchy honest, or replace it with composition"],
 E=["Set design standards a whole organisation can review against","Teach patterns as answers to problems, not as goals","Judge which principles change shape in functional code"],
 topics=["Single responsibility and open-closed","Liskov substitution and interface segregation","Dependency inversion and injection","The Gang of Four patterns","YAGNI and simple design"],
 links=[("Fowler: Inversion of Control Containers and the Dependency Injection pattern","https://martinfowler.com/articles/injection.html","Where the name comes from"),
        ("Fowler: Yagni","https://martinfowler.com/bliki/Yagni.html","Presumptive features"),
        ("Fowler: Beck Design Rules","https://martinfowler.com/bliki/BeckDesignRules.html","Four rules of simple design")],
 sources=[("Wikipedia: SOLID","https://en.wikipedia.org/wiki/SOLID"),
          ("Wikipedia: Single-responsibility principle","https://en.wikipedia.org/wiki/Single-responsibility_principle"),
          ("Wikipedia: Open–closed principle","https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle"),
          ("Wikipedia: Liskov substitution principle","https://en.wikipedia.org/wiki/Liskov_substitution_principle"),
          ("Wikipedia: Interface segregation principle","https://en.wikipedia.org/wiki/Interface_segregation_principle"),
          ("Wikipedia: Dependency inversion principle","https://en.wikipedia.org/wiki/Dependency_inversion_principle"),
          ("Wikipedia: Design Patterns","https://en.wikipedia.org/wiki/Design_Patterns"),
          ("Wikipedia: Strategy pattern","https://en.wikipedia.org/wiki/Strategy_pattern"),
          ("Wikipedia: Observer pattern","https://en.wikipedia.org/wiki/Observer_pattern"),
          ("Wikipedia: Decorator pattern","https://en.wikipedia.org/wiki/Decorator_pattern"),
          ("Wikipedia: Singleton pattern","https://en.wikipedia.org/wiki/Singleton_pattern"),
          ("Wikipedia: Template method pattern","https://en.wikipedia.org/wiki/Template_method_pattern"),
          ("Wikipedia: Proxy pattern","https://en.wikipedia.org/wiki/Proxy_pattern"),
          ("Wikipedia: Dependency injection","https://en.wikipedia.org/wiki/Dependency_injection"),
          ("Wikipedia: Anti-pattern","https://en.wikipedia.org/wiki/Anti-pattern"),
          ("Fowler: Inversion of Control Containers and the Dependency Injection pattern (2004)","https://martinfowler.com/articles/injection.html"),("Fowler: Yagni","https://martinfowler.com/bliki/Yagni.html"),("Fowler: Beck Design Rules","https://martinfowler.com/bliki/BeckDesignRules.html")])

D["pki"]=dict(
 F=["Explain a key pair: what the public key and the private key are each for","Read a certificate's subject, SAN, issuer and dates","Make an SSH key and add its public half to a server or GitHub"],
 P=["Make a CSR with the right SAN and check it before sending","Fix a missing intermediate, a hostname mismatch and an expired certificate","Sign Git commits with an SSH key and verify them"],
 S=["Run a private CA for internal services, and know its limits","Automate certificate renewal with ACME","Set up mTLS between services"],
 E=["Set an organisation's key and certificate policy","Plan certificate and key rotation without outages","Design trust for partners and devices that cannot automate"],
 topics=["Public-key cryptography","X.509 certificates and the chain of trust","CSRs (PKCS #10) and certificate authorities","ACME and Let's Encrypt","SSH keys, ssh-agent and known_hosts","Signed Git commits"],
 links=[("RFC 2986: PKCS #10 certification requests","https://www.rfc-editor.org/rfc/rfc2986","What a CSR contains"),
        ("RFC 5280: X.509 certificates","https://www.rfc-editor.org/rfc/rfc5280","The certificate format and path validation"),
        ("GitHub: Generating a new SSH key","https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent","Step by step")],
 sources=[("Wikipedia: Public-key cryptography","https://en.wikipedia.org/wiki/Public-key_cryptography"),("Wikipedia: Certificate authority","https://en.wikipedia.org/wiki/Certificate_authority"),
          ("Wikipedia: Certificate signing request","https://en.wikipedia.org/wiki/Certificate_signing_request"),("Wikipedia: Chain of trust","https://en.wikipedia.org/wiki/Chain_of_trust"),
          ("Wikipedia: Public key certificate","https://en.wikipedia.org/wiki/Public_key_certificate"),("RFC 2986","https://www.rfc-editor.org/rfc/rfc2986"),("RFC 5280","https://www.rfc-editor.org/rfc/rfc5280"),
          ("RFC 8555: ACME","https://www.rfc-editor.org/rfc/rfc8555"),("Let's Encrypt: How it works (source)","https://github.com/letsencrypt/website/blob/main/content/en/how-it-works.md"),("Let's Encrypt: FAQ (source)","https://github.com/letsencrypt/website/blob/main/content/en/docs/faq.md"),
          ("OpenSSL: openssl-req","https://github.com/openssl/openssl/blob/master/doc/man1/openssl-req.pod.in"),("OpenSSL: openssl-x509","https://github.com/openssl/openssl/blob/master/doc/man1/openssl-x509.pod.in"),("OpenSSL: openssl-verify","https://github.com/openssl/openssl/blob/master/doc/man1/openssl-verify.pod.in"),
          ("OpenSSH: ssh-keygen(1)","https://github.com/openssh/openssh-portable/blob/master/ssh-keygen.1"),("OpenSSH: ssh(1)","https://github.com/openssh/openssh-portable/blob/master/ssh.1"),("OpenSSH: sshd(8)","https://github.com/openssh/openssh-portable/blob/master/sshd.8"),("OpenSSH: ssh-agent(1)","https://github.com/openssh/openssh-portable/blob/master/ssh-agent.1"),
          ("Git: gpg configuration","https://github.com/git/git/blob/master/Documentation/config/gpg.adoc"),
          ("GitHub: Generating a new SSH key","https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"),
          ("GitHub: Adding a new SSH key to your account","https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account"),
          ("GitHub: Testing your SSH connection","https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection"),
          ("GitHub: About commit signature verification","https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification"),
          ("GitHub: Telling Git about your signing key","https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key")])

D["privacy"]=dict(
 F=["List where personal data ends up in a service architecture","Explain tokenisation, pseudonymisation and anonymisation","Name the rights a person has over their data"],
 P=["Keep a data catalogue of personal fields per service","Build an erasure event that every service handles idempotently","Test deletion end to end in CI"],
 S=["Design for erasure and legal retention together","Use crypto-shredding for backups and copies","Plan regional deployments for data residency"],
 E=["Set an organisation's personal-data architecture and standards","Work with legal and the data protection officer on retention rules","Audit and report on data subject requests across systems"],
 topics=["GDPR rights and principles","Data minimisation and tokenisation","Pseudonymisation and anonymisation","Erasure across services","Crypto-shredding","Data residency and transfers"],
 links=[("Wikipedia: General Data Protection Regulation","https://en.wikipedia.org/wiki/General_Data_Protection_Regulation","Rights, principles and transfers"),
        ("Wikipedia: Crypto-shredding","https://en.wikipedia.org/wiki/Crypto-shredding","Erasing by deleting keys"),
        ("Microsoft Learn: GDPR data subject requests for Azure","https://learn.microsoft.com/en-us/compliance/regulatory/gdpr-dsr-azure","How a cloud provider handles them")],
 sources=[("Wikipedia: General Data Protection Regulation","https://en.wikipedia.org/wiki/General_Data_Protection_Regulation"),("Wikipedia: Right to be forgotten","https://en.wikipedia.org/wiki/Right_to_be_forgotten"),
          ("Wikipedia: Tokenization (data security)","https://en.wikipedia.org/wiki/Tokenization_(data_security)"),("Wikipedia: Pseudonymization","https://en.wikipedia.org/wiki/Pseudonymization"),("Wikipedia: Data anonymization","https://en.wikipedia.org/wiki/Data_anonymization"),
          ("Wikipedia: Data minimization","https://en.wikipedia.org/wiki/Data_minimization"),("Wikipedia: Crypto-shredding","https://en.wikipedia.org/wiki/Crypto-shredding"),("Wikipedia: Data sovereignty (residency and localisation)","https://en.wikipedia.org/wiki/Data_sovereignty"),
          ("Microsoft Learn: GDPR data subject requests for Azure","https://learn.microsoft.com/en-us/compliance/regulatory/gdpr-dsr-azure")])

D["bitcoin"]=dict(
 F=["Explain hashes and how blocks link","Explain proof of work and why rewriting history is hard","Keep keys safe and recognise common scams"],
 P=["Build a toy chain and validate it","Explain Bitcoin's supply, halving and difficulty rules","Compare proof of work and proof of stake"],
 S=["Judge whether a problem needs a blockchain at all","Design key custody and recovery","Assess the security model of a chain or protocol"],
 E=["Advise an organisation on distributed-ledger strategy","Review consensus and cryptographic designs","Explain the technology to non-specialists without hype"],
 topics=["SHA-256 and Merkle trees","Proof of work and difficulty","Public-key cryptography and wallets","Proof of stake","Layer 2 payment channels"],
 links=[("Bitcoin: A Peer-to-Peer Electronic Cash System","https://bitcoin.org/bitcoin.pdf","Satoshi Nakamoto's white paper, nine pages"),
        ("Bitcoin protocol (Wikipedia)","https://en.wikipedia.org/wiki/Bitcoin_protocol","How mining, blocks and transactions work"),
        ("Bitcoin Core source","https://github.com/bitcoin/bitcoin","The reference implementation")])

D["robotics"]=dict(
 F=["Explain the sense-think-act loop","Tune a PID controller in simulation","Know why every robot has an emergency stop"],
 P=["Build a small robot or simulated one with ROS 2 nodes and topics","Read sensor data and filter its noise","Apply forward and inverse kinematics to an arm"],
 S=["Design localisation, mapping and path planning","Design for functional safety and failure modes","Move from simulation to hardware safely"],
 E=["Lead a robotics platform or product","Set safety and testing standards","Combine learned models with classical control responsibly"],
 topics=["PID control","Kinematics","SLAM","ROS 2 nodes, topics and services","Robot safety standards (ISO 10218)"],
 links=[("Robot Operating System (Wikipedia)","https://en.wikipedia.org/wiki/Robot_Operating_System","What ROS is and how it is organised"),
        ("ROS 2 source","https://github.com/ros2/ros2","The ROS 2 repositories and installation"),
        ("PID controller (Wikipedia)","https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller","The maths behind the example")])

D["k8sdr"]=dict(
 F=["Run workloads as Deployments with several replicas","Add readiness and liveness probes","Explain RPO and RTO"],
 P=["Add PodDisruptionBudgets and zone spreading","Schedule Velero or managed backups and restore one","Keep all manifests in Git so a cluster is replaceable"],
 S=["Choose a DR strategy against agreed RPO and RTO","Design multi-zone and multi-region clusters","Run restore drills and game days"],
 E=["Own platform resilience across clusters and regions","Set backup, restore and DR standards","Lead recovery during a major incident"],
 topics=["etcd snapshots","Velero backup and restore","Volume snapshots","Topology spread constraints","Disaster recovery strategies"],
 links=[("Operating etcd clusters for Kubernetes","https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/","Snapshots and restore, from the Kubernetes docs"),
        ("Disruptions and PodDisruptionBudgets","https://kubernetes.io/docs/concepts/workloads/pods/disruptions/","Voluntary and involuntary disruptions"),
        ("Velero: disaster recovery","https://velero.io/docs/main/disaster-case/","The DR flow with schedules and restores"),
        ("Disaster recovery options in the cloud","https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html","The four strategies, from AWS's whitepaper")])

# Sources each page's claims were checked against (rendered as "Checked against:")
D["linux"]["sources"]=[
 ("find(1)","https://man7.org/linux/man-pages/man1/find.1.html"),("sort(1)","https://man7.org/linux/man-pages/man1/sort.1.html"),
 ("xargs(1)","https://man7.org/linux/man-pages/man1/xargs.1.html"),("du(1)","https://man7.org/linux/man-pages/man1/du.1.html"),
 ("chmod(1)","https://man7.org/linux/man-pages/man1/chmod.1.html"),("sed(1)","https://man7.org/linux/man-pages/man1/sed.1.html"),
 ("less(1)","https://man7.org/linux/man-pages/man1/less.1.html"),("timeout(1)","https://man7.org/linux/man-pages/man1/timeout.1.html"),
 ("systemctl(1)","https://man7.org/linux/man-pages/man1/systemctl.1.html"),("journalctl(1)","https://man7.org/linux/man-pages/man1/journalctl.1.html"),
 ("systemd.service(5)","https://man7.org/linux/man-pages/man5/systemd.service.5.html"),("ssh(1)","https://man7.org/linux/man-pages/man1/ssh.1.html"),
 ("ssh-keygen(1)","https://man7.org/linux/man-pages/man1/ssh-keygen.1.html"),("tmux(1)","https://man7.org/linux/man-pages/man1/tmux.1.html"),
 ("RFC 5737 (documentation addresses)","https://www.rfc-editor.org/rfc/rfc5737"),
 ("exit codes 126, 127, 137 and 143, run in bash","https://man7.org/linux/man-pages/man1/bash.1.html")]
D["networking"]["sources"]=[
 ("RFC 1918 (private ranges)","https://www.rfc-editor.org/rfc/rfc1918"),("RFC 6598 (shared address space)","https://www.rfc-editor.org/rfc/rfc6598"),
 ("RFC 1912 (CNAME with other data)","https://www.rfc-editor.org/rfc/rfc1912"),("RFC 7766 (DNS over TCP)","https://www.rfc-editor.org/rfc/rfc7766"),
 ("RFC 2782 (SRV)","https://www.rfc-editor.org/rfc/rfc2782"),("RFC 8659 (CAA)","https://www.rfc-editor.org/rfc/rfc8659"),
 ("RFC 9110 (HTTP semantics)","https://www.rfc-editor.org/rfc/rfc9110"),("RFC 6585 (429)","https://www.rfc-editor.org/rfc/rfc6585"),
 ("RFC 9114 (HTTP/3)","https://www.rfc-editor.org/rfc/rfc9114"),("RFC 6066 (SNI)","https://www.rfc-editor.org/rfc/rfc6066"),
 ("Kubernetes ports and protocols","https://kubernetes.io/docs/reference/networking/ports-and-protocols/"),
 ("Google Cloud subnets","https://docs.cloud.google.com/vpc/docs/subnets"),("VPC firewall rules","https://docs.cloud.google.com/firewall/docs/firewalls"),
 ("Cloud Run container contract","https://docs.cloud.google.com/run/docs/container-contract"),("Cloud NAT overview","https://docs.cloud.google.com/nat/docs/overview"),
 ("ss(8)","https://man7.org/linux/man-pages/man8/ss.8.html"),("tcpdump(1)","https://man7.org/linux/man-pages/man1/tcpdump.1.html"),
 ("gcloud commands, checked with gcloud --help","https://docs.cloud.google.com/sdk/gcloud/reference")]
D["testing"].setdefault("sources",[]).extend([("The Practical Test Pyramid (martinfowler.com)","https://martinfowler.com/articles/practical-test-pyramid.html")])
D["java"].setdefault("sources",[]).extend([
 ("Thread (since 1.0)","https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html"),
 ("ExecutorService (since 1.5)","https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ExecutorService.html"),
 ("ForkJoinPool (since 1.7)","https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ForkJoinPool.html"),
 ("CompletableFuture (since 1.8)","https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html"),
 ("Flow (since 9)","https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Flow.html"),
 ("JEP 425","https://openjdk.org/jeps/425"),("JEP 444","https://openjdk.org/jeps/444"),("JEP 453","https://openjdk.org/jeps/453"),
 ("JEP 491","https://openjdk.org/jeps/491"),("JEP 505","https://openjdk.org/jeps/505"),("JEP 506","https://openjdk.org/jeps/506"),
 ("Green threads (Wikipedia)","https://en.wikipedia.org/wiki/Green_thread")])
D["web"].setdefault("sources",[]).extend([
 ("MDN: CORS","https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS"),("MDN: Set-Cookie","https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie"),
 ("MDN: URI fragment","https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment"),("MDN: script element","https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script"),
 ("RFC 9110 (HTTP semantics)","https://www.rfc-editor.org/rfc/rfc9110"),("RFC 9111 (HTTP caching)","https://www.rfc-editor.org/rfc/rfc9111"),
 ("RFC 8246 (immutable)","https://www.rfc-editor.org/rfc/rfc8246"),("RFC 6797 (HSTS)","https://www.rfc-editor.org/rfc/rfc6797"),
 ("web.dev: Web Vitals","https://web.dev/articles/vitals"),("WCAG 2.2 (contrast)","https://www.w3.org/TR/WCAG22/")])

D["apps"]=dict(
 F=["Explain native, cross-platform and web app options","Build and run a sample app on one platform","Know what an app store review involves"],
 P=["Ship a feature on one mobile platform, with tests","Share business logic across platforms","Build an installable, offline-capable web app"],
 S=["Choose an app architecture for a product and team","Design offline, sync and push notifications","Plan releases, versions and backwards compatibility"],
 E=["Own mobile and desktop strategy across products","Lead a move between app technologies","Set performance, accessibility and security standards for apps"],
 topics=["SwiftUI","Jetpack Compose","Kotlin Multiplatform","Flutter","React Native","Progressive web apps"],
 links=[("Jetpack Compose","https://developer.android.com/compose","Android's modern UI toolkit"),
        ("SwiftUI","https://developer.apple.com/swiftui/","Apple's declarative UI framework"),
        ("Kotlin Multiplatform","https://kotlinlang.org/docs/multiplatform.html","Share code across platforms"),
        ("Flutter documentation","https://docs.flutter.dev/","Multiplatform apps from a single codebase"),
        ("React Native","https://reactnative.dev/","React for native apps"),
        ("MDN: Progressive web apps","https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps","Installable, offline-capable web apps")],
 sources=[("Jetpack Compose","https://developer.android.com/compose"),("SwiftUI","https://developer.apple.com/swiftui/"),
          ("Flutter docs","https://docs.flutter.dev/"),("React Native","https://reactnative.dev/"),
          ("MDN: Progressive web apps","https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps"),
          ("Kotlin (Wikipedia): Google's preferred language, 7 May 2019","https://en.wikipedia.org/wiki/Kotlin"),
          ("Kotlin Multiplatform (Wikipedia): stable, November 2023","https://en.wikipedia.org/wiki/Kotlin_Multiplatform")])
D["kotlin"].setdefault("sources",[]).extend([("Kotlin (Wikipedia)","https://en.wikipedia.org/wiki/Kotlin"),("Scala (Wikipedia)","https://en.wikipedia.org/wiki/Scala_(programming_language)"),
 ("Java (Wikipedia)","https://en.wikipedia.org/wiki/Java_(programming_language)"),("New in Scala 3","https://docs.scala-lang.org/scala3/new-in-scala3.html")])
D["spring"].setdefault("sources",[]).extend([("JEP 444: Virtual Threads","https://openjdk.org/jeps/444")])

D["electronics"]=dict(
 F=["Explain voltage, current and how a transistor switches","Explain logic gates and how they add numbers","Explain what an instruction set is"],
 P=["Build a microcontroller project with sensors and motors","Write and simulate a small design in Verilog or VHDL","Run a design on an FPGA board"],
 S=["Design a simple processor or peripheral on an FPGA","Read datasheets and choose components for a product","Design hardware for repair and long life"],
 E=["Lead hardware and software co-design","Take a design towards silicon with an open process kit","Shape open hardware and sustainability practice"],
 topics=["Digital logic","Verilog and VHDL","FPGAs","RISC-V","Semiconductor manufacturing","E-waste and repair"],
 links=[("RISC-V (Wikipedia)","https://en.wikipedia.org/wiki/RISC-V","The open standard instruction set"),
        ("Field-programmable gate array (Wikipedia)","https://en.wikipedia.org/wiki/Field-programmable_gate_array","Reprogrammable chips for learning digital design"),
        ("Semiconductor device fabrication (Wikipedia)","https://en.wikipedia.org/wiki/Semiconductor_device_fabrication","How chips are made")],
 sources=[("Transistor","https://en.wikipedia.org/wiki/Transistor"),("Integrated circuit","https://en.wikipedia.org/wiki/Integrated_circuit"),
          ("Moore's law","https://en.wikipedia.org/wiki/Moore%27s_law"),("Field-programmable gate array","https://en.wikipedia.org/wiki/Field-programmable_gate_array"),
          ("Hardware description language","https://en.wikipedia.org/wiki/Hardware_description_language"),("RISC-V","https://en.wikipedia.org/wiki/RISC-V"),
          ("SkyWater Technology (SKY130 PDK)","https://en.wikipedia.org/wiki/SkyWater_Technology"),("TSMC (foundry share)","https://en.wikipedia.org/wiki/TSMC"),
          ("Electronic waste","https://en.wikipedia.org/wiki/Electronic_waste"),("Right to repair","https://en.wikipedia.org/wiki/Right_to_repair")])

D["hardware"]=dict(
 F=["Explain what an instruction set is, and RISC versus CISC","Explain firmware and device drivers","Explain why GPUs suit graphics and AI"],
 P=["Program a microcontroller to read a sensor and drive an output","Read a laptop or server spec sheet and know what each part does","Run a workload on a GPU and compare it with the CPU"],
 S=["Choose hardware for a workload: cores, memory, storage, accelerators","Profile where time goes between CPU, memory, disk and GPU","Plan for ARM and x86 in the same estate"],
 E=["Set hardware strategy for a platform or data centre","Co-design software with accelerators","Lead a move between processor architectures"],
 topics=["Instruction set architectures","Firmware and boot","Device drivers","Systems on a chip","GPU programming"],
 links=[("Reduced instruction set computer (Wikipedia)","https://en.wikipedia.org/wiki/Reduced_instruction_set_computer","RISC explained, with its history"),
        ("Graphics processing unit (Wikipedia)","https://en.wikipedia.org/wiki/Graphics_processing_unit","How GPUs work and how they developed"),
        ("CUDA (Wikipedia)","https://en.wikipedia.org/wiki/CUDA","General-purpose computing on GPUs")],
 sources=[(n,"https://en.wikipedia.org/wiki/"+u) for n,u in [
  ("Reduced instruction set computer","Reduced_instruction_set_computer"),("Complex instruction set computer","Complex_instruction_set_computer"),
  ("Intel 4004","Intel_4004"),("Intel 8086","Intel_8086"),("ARM architecture family","ARM_architecture_family"),("x86-64","X86-64"),
  ("Multi-core processor","Multi-core_processor"),("Apple M1","Apple_M1"),("System on a chip","System_on_a_chip"),
  ("Firmware","Firmware"),("Microcontroller","Microcontroller"),("Device driver","Device_driver"),("NVM Express","NVM_Express"),
  ("MIDI","MIDI"),("AdLib","AdLib"),("Sound Blaster","Sound_Blaster"),("Intel High Definition Audio","Intel_High_Definition_Audio"),
  ("3dfx Interactive","3dfx_Interactive"),("Graphics processing unit","Graphics_processing_unit"),("CUDA","CUDA"),
  ("AlexNet","AlexNet"),("Tensor Processing Unit","Tensor_Processing_Unit"),("Volta (microarchitecture)","Volta_(microarchitecture)")]])

D["internet"]=dict(
 F=["Explain that the internet is many networks connected together","Explain what DNS, a CDN and a cloud region are","List your service's outside dependencies"],
 P=["Trace a request's path with traceroute and DNS lookups","Explain BGP and why a bad route can take a company offline","Configure a CDN and DNS for a service"],
 S=["Design for the failure of a DNS provider, CDN or region","Plan multi-region and multi-provider set-ups","Run outage drills for shared dependencies"],
 E=["Own internet-facing architecture and its resilience","Negotiate peering and provider strategy","Lead response to large external outages"],
 topics=["Autonomous systems and BGP","Internet exchange points","Submarine cables","DNS root servers and anycast","Content delivery networks"],
 links=[("Border Gateway Protocol (Wikipedia)","https://en.wikipedia.org/wiki/Border_Gateway_Protocol","How networks share routes"),
        ("Internet exchange point (Wikipedia)","https://en.wikipedia.org/wiki/Internet_exchange_point","Where networks meet"),
        ("Root name server (Wikipedia)","https://en.wikipedia.org/wiki/Root_name_server","The top of DNS")],
 sources=[(n,"https://en.wikipedia.org/wiki/"+u) for n,u in [("Autonomous system","Autonomous_system_(Internet)"),("Border Gateway Protocol","Border_Gateway_Protocol"),
  ("Internet exchange point","Internet_exchange_point"),("Submarine communications cable","Submarine_communications_cable"),("Root name server","Root_name_server"),
  ("Content delivery network","Content_delivery_network"),("Akamai Technologies","Akamai_Technologies"),("Cloudflare (November 2025 outage)","Cloudflare"),
  ("2021 Facebook outage","2021_Facebook_outage"),("Timeline of AWS (20 October 2025 outage)","Timeline_of_Amazon_Web_Services")]])

# Sources from the full fact check (November 2026): rendered as "Checked against".
import json as _json
FACTCHECK_SOURCES=_json.loads(r"""{"docker": [["Dockerfile reference", "https://docs.docker.com/reference/dockerfile/"], ["Build secrets", "https://docs.docker.com/build/building/secrets/"], ["docker system prune", "https://docs.docker.com/reference/cli/docker/system/prune/"], ["SBOM attestations", "https://docs.docker.com/build/metadata/attestations/sbom/"], ["docker compose down", "https://docs.docker.com/reference/cli/docker/compose/down/"], ["Compose startup order", "https://docs.docker.com/compose/how-tos/startup-order/"], ["docker run exit status", "https://docs.docker.com/engine/containers/run/"], ["Distroless README (java21-debian13, nonroot, debug tags)", "https://raw.githubusercontent.com/GoogleContainerTools/distroless/main/README.md"], ["signal(7)", "https://man7.org/linux/man-pages/man7/signal.7.html"]], "sql": [["GoogleSQL query syntax (QUALIFY order, SELECT DISTINCT, set operators)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax"], ["GoogleSQL aggregate functions (ANY_VALUE HAVING, COUNTIF, NULL handling)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions"], ["GoogleSQL operators (IS NOT DISTINCT FROM, division result types)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/operators"], ["GoogleSQL window function calls (RANGE needs numeric key, UNIX_DATE tip)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls"], ["GoogleSQL date functions (default time zone UTC)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/date_functions"], ["GoogleSQL DML (MERGE must match at most one source row)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax"], ["BigQuery compute best practices (CTE evaluated multiple times, ORDER BY)", "https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute"], ["BigQuery cost best practices (dry run)", "https://docs.cloud.google.com/bigquery/docs/best-practices-costs"], ["Clustered tables (no accurate estimate before run)", "https://docs.cloud.google.com/bigquery/docs/clustered-tables"], ["BigQuery sandbox (no billing account)", "https://docs.cloud.google.com/bigquery/docs/sandbox"], ["PostgreSQL aggregate functions (no COUNTIF; FILTER clause)", "https://www.postgresql.org/docs/current/sql-expressions.html"]], "database": [["Multicolumn indexes (any subset; skip scan)", "https://www.postgresql.org/docs/current/indexes-multicolumn.html"], ["PostgreSQL 18 release notes (B-tree skip scan)", "https://www.postgresql.org/docs/18/release-18.html"], ["PostgreSQL 17 release notes (identity columns on partitioned tables)", "https://www.postgresql.org/docs/17/release-17.html"], ["Table partitioning (unique keys include partition key)", "https://www.postgresql.org/docs/current/ddl-partitioning.html"], ["CREATE INDEX (CONCURRENTLY leaves INVALID index)", "https://www.postgresql.org/docs/current/sql-createindex.html"], ["Operator classes (text_pattern_ops, C locale)", "https://www.postgresql.org/docs/current/indexes-opclass.html"], ["Constraints (FK referencing columns not auto-indexed)", "https://www.postgresql.org/docs/current/ddl-constraints.html"], ["Transaction isolation (Read Committed default, no phantoms in Repeatable Read)", "https://www.postgresql.org/docs/current/transaction-iso.html"], ["pg_stat_statements (mean_exec_time, total_exec_time)", "https://www.postgresql.org/docs/current/pgstatstatements.html"], ["SQL keywords (ORDER reserved)", "https://www.postgresql.org/docs/current/sql-keywords-appendix.html"], ["pgvector README (hnsw, vector_cosine_ops)", "https://raw.githubusercontent.com/pgvector/pgvector/master/README.md"], ["AlloyDB read pools (scale reads)", "https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create"]], "python": [["What's new in Python 3.15 (lazy imports, frozendict, sentinel, UTF-8 default, comprehension unpacking, profiling/Tachyon)", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.15.rst"], ["PEP 790: 3.15 release schedule (final 2026-10-09)", "https://raw.githubusercontent.com/python/peps/main/peps/pep-0790.rst"], ["What's new in Python 3.14", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.14.rst"], ["What's new in Python 3.13 (new REPL, free-threaded, JIT)", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.13.rst"], ["What's new in Python 3.12 (PEP 695, PEP 701, itertools.batched)", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.12.rst"], ["What's new in Python 3.11 (tomllib, except*, TaskGroup, Self)", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.11.rst"], ["What's new in Python 3.10 (zip strict)", "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.10.rst"], ["PEP 750 / 649 / 779 / 784 / 734 (3.14 features, Final)", "https://raw.githubusercontent.com/python/peps/main/peps/pep-0750.rst"], ["google-cloud-bigquery on PyPI (signatures checked locally)", "https://pypi.org/pypi/google-cloud-bigquery/json"], ["google-cloud-storage on PyPI (list_blobs match_glob, if_generation_match, copy_blob checked locally)", "https://pypi.org/pypi/google-cloud-storage/json"], ["Apache Beam BigQuery IO source (ReadFromBigQuery use_standard_sql)", "https://raw.githubusercontent.com/apache/beam/master/sdks/python/apache_beam/io/gcp/bigquery.py"], ["pytest on PyPI (-k, -x, --lf checked via pytest --help)", "https://pypi.org/pypi/pytest/json"]], "apis": [["RFC 9110 HTTP Semantics (safe/idempotent methods, status codes)", "https://www.rfc-editor.org/rfc/rfc9110.txt"], ["RFC 9457 Problem Details", "https://www.rfc-editor.org/rfc/rfc9457.txt"], ["RFC 5789 PATCH (neither safe nor idempotent)", "https://www.rfc-editor.org/rfc/rfc5789.txt"], ["RFC 8594 Sunset header", "https://www.rfc-editor.org/rfc/rfc8594.txt"], ["RFC 9745 Deprecation header", "https://www.rfc-editor.org/rfc/rfc9745.txt"], ["OpenAPI 3.1 specification", "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/versions/3.1.0.md"], ["Protocol Buffers proto3 guide (field numbers, reserved)", "https://raw.githubusercontent.com/protocolbuffers/protocolbuffers.github.io/main/content/programming-guides/proto3.md"]], "graphql": [["GraphQL spec: Response (errors, path, extensions)", "https://raw.githubusercontent.com/graphql/graphql-spec/main/spec/Section%207%20--%20Response.md"], ["Relay cursor connections spec", "https://raw.githubusercontent.com/facebook/relay/main/website/spec/Connections.md"], ["Spring for GraphQL: annotated controllers, @BatchMapping", "https://raw.githubusercontent.com/spring-projects/spring-graphql/main/spring-graphql-docs/modules/ROOT/pages/controllers.adoc"], ["Spring for GraphQL: GraphQlTester source (path, valueIsNull)", "https://raw.githubusercontent.com/spring-projects/spring-graphql/main/spring-graphql-test/src/main/java/org/springframework/graphql/test/tester/GraphQlTester.java"], ["Quarkus SmallRye GraphQL guide (@Source batching, /q/graphql-ui)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/smallrye-graphql.adoc"], ["Strawberry DataLoader guide", "https://raw.githubusercontent.com/strawberry-graphql/strawberry/main/docs/guides/dataloaders.md"], ["Strawberry public API (Info, Private, ID)", "https://raw.githubusercontent.com/strawberry-graphql/strawberry/main/strawberry/__init__.py"]], "kafka": [["Kafka 4.0 upgrade notes (ZooKeeper removed, KRaft only)", "https://raw.githubusercontent.com/apache/kafka/4.0.0/docs/upgrade.html"], ["Kafka 4.0 design docs (replication, ISR, compaction)", "https://raw.githubusercontent.com/apache/kafka/4.0.0/docs/design.html"], ["Kafka ProducerConfig (enable.idempotence defaults to true)", "https://raw.githubusercontent.com/apache/kafka/4.0.0/clients/src/main/java/org/apache/kafka/clients/producer/ProducerConfig.java"], ["kafka-consumer-groups options (--to-datetime format)", "https://raw.githubusercontent.com/apache/kafka/trunk/tools/src/main/java/org/apache/kafka/tools/consumer/group/ConsumerGroupCommandOptions.java"], ["kafka-console-producer options", "https://raw.githubusercontent.com/apache/kafka/trunk/tools/src/main/java/org/apache/kafka/tools/ConsoleProducer.java"], ["Spring Kafka JsonSerializer (deprecated since 4.0)", "https://raw.githubusercontent.com/spring-projects/spring-kafka/main/spring-kafka/src/main/java/org/springframework/kafka/support/serializer/JsonSerializer.java"], ["Spring Kafka JacksonJsonSerializer (since 4.0)", "https://raw.githubusercontent.com/spring-projects/spring-kafka/main/spring-kafka/src/main/java/org/springframework/kafka/support/serializer/JacksonJsonSerializer.java"], ["Spring Boot KafkaProperties (String (de)serializer defaults)", "https://raw.githubusercontent.com/spring-projects/spring-boot/3.5.x/spring-boot-project/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/kafka/KafkaProperties.java"], ["Quarkus Kafka guide (quarkus-messaging-kafka, merge)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/kafka.adoc"], ["Managed Kafka Connect connectors (BigQuery Sink)", "https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview"], ["Pub/Sub replay (seek to time or snapshot)", "https://docs.cloud.google.com/pubsub/docs/replay-overview"]], "payments": [["Wikipedia: Payment gateway (authorise, capture, settle)", "https://en.wikipedia.org/wiki/Payment_gateway?action=raw"], ["Wikipedia: Chargeback", "https://en.wikipedia.org/wiki/Chargeback?action=raw"], ["Wikipedia: Acquiring bank", "https://en.wikipedia.org/wiki/Acquiring_bank?action=raw"], ["Wikipedia: Unified Payments Interface (NPCI, PIN, AutoPay)", "https://en.wikipedia.org/wiki/Unified_Payments_Interface?action=raw"], ["Wikipedia: 3-D Secure", "https://en.wikipedia.org/wiki/3-D_Secure?action=raw"], ["Wikipedia: PCI DSS", "https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard?action=raw"], ["razorpay-python utility (order_id|payment_id HMAC-SHA256; webhook HMAC of body)", "https://raw.githubusercontent.com/razorpay/razorpay-python/master/razorpay/utility/utility.py"], ["stripe-python Webhook.construct_event", "https://raw.githubusercontent.com/stripe/stripe-python/master/stripe/_webhook.py"], ["stripe-python top-level SignatureVerificationError", "https://raw.githubusercontent.com/stripe/stripe-python/master/stripe/__init__.py"], ["stripe-python request options (idempotency_key)", "https://raw.githubusercontent.com/stripe/stripe-python/master/stripe/_request_options.py"]], "quarkus": [["Maven Central: quarkus-core versions (the newest is a release candidate, with no final release yet)", "https://repo1.maven.org/maven2/io/quarkus/quarkus-core/maven-metadata.xml"], ["Maven Central: quarkus-junit-mockito (first version", "https://repo1.maven.org/maven2/io/quarkus/quarkus-junit-mockito/maven-metadata.xml"], ["Quarkus Hibernate ORM guide (schema-management.strategy)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/hibernate-orm.adoc"], ["Quarkus Hibernate ORM skill notes (database.generation deprecated)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/extensions/hibernate-orm/deployment/src/main/resources/META-INF/quarkus-skill.md"], ["Quarkus testing guide (@TestProfile on the test class, @InjectMock)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/getting-started-testing.adoc"], ["Quarkus CLI guide (--installable)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/cli-tooling.adoc"], ["Quarkus Dev UI guide (d opens Dev UI)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/dev-ui.adoc"], ["Quarkus continuous testing (r re-runs tests)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/continuous-testing.adoc"], ["Quarkus getting started (fast-jar, ship quarkus-app/)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/getting-started.adoc"], ["Quarkus scheduler reference (timeZone, ConcurrentExecution.SKIP)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/scheduler-reference.adoc"], ["Quarkus SmallRye Health (/q/health/live, ready, started)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/smallrye-health.adoc"], ["Quarkus REST client config source (read-timeout)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/extensions/resteasy-classic/rest-client-config/runtime/src/main/java/io/quarkus/restclient/config/RestClientsConfig.java"], ["Quarkus Kubernetes guide (replicas, env.secrets, target/kubernetes)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/deploying-to-kubernetes.adoc"], ["Maven Central: Quarkiverse quarkus-google-cloud-bigquery", "https://repo1.maven.org/maven2/io/quarkiverse/googlecloudservices/quarkus-google-cloud-bigquery/maven-metadata.xml"]], "performance": [["Wikipedia: Little's law (L = \u03bbW)", "https://en.wikipedia.org/wiki/Little%27s_law?action=raw"], ["Wikipedia: Amdahl's law", "https://en.wikipedia.org/wiki/Amdahl%27s_law?action=raw"], ["jcmd manual, JDK 21 (JFR.start, GC.heap_info, Thread.print)", "https://docs.oracle.com/en/java/javase/21/docs/specs/man/jcmd.html"], ["java manual, JDK 21 (-XX:StartFlightRecording, MaxRAMPercentage)", "https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html"], ["async-profiler options (-d, -e cpu|alloc, -f)", "https://raw.githubusercontent.com/async-profiler/async-profiler/master/docs/ProfilerOptions.md"], ["py-spy README (top, record)", "https://raw.githubusercontent.com/benfred/py-spy/master/README.md"], ["CPython docs: -X importtime", "https://raw.githubusercontent.com/python/cpython/main/Doc/using/cmdline.rst"], ["memray run command (run as module)", "https://raw.githubusercontent.com/bloomberg/memray/main/src/memray/commands/run.py"]], "security": [["OWASP Top 10 2025 index (source repo)", "https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/index.md"], ["OWASP Top 10 2025 introduction (SSRF rolled into A01, A10 new)", "https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/0x00_2025-Introduction.md"], ["OWASP GenAI LLM Top 10 2026 list", "https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md"], ["OWASP LLM project README (2026 published August 4, 2026)", "https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/README.md"], ["OWASP Password Storage Cheat Sheet", "https://raw.githubusercontent.com/OWASP/CheatSheetSeries/master/cheatsheets/Password_Storage_Cheat_Sheet.md"], ["Kubernetes Pod Security Standards", "https://kubernetes.io/docs/concepts/security/pod-security-standards/"], ["Kubernetes Pod Security Admission (namespace labels)", "https://kubernetes.io/docs/concepts/security/pod-security-admission/"], ["Cloud Audit Logs (Admin Activity always written)", "https://docs.cloud.google.com/logging/docs/audit"], ["Spring Boot OAuth2ResourceServerProperties (issuer-uri, audiences)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/module/spring-boot-security-oauth2-resource-server/src/main/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/OAuth2ResourceServerProperties.java"], ["RFC 9700 OAuth 2.0 Security BCP", "https://www.rfc-editor.org/rfc/rfc9700.txt"]], "cyber": [["MITRE ATT&CK STIX index (latest Enterprise = 20.1)", "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/index.json"], ["Enterprise ATT&CK 20.1 bundle (matrix tactic_refs: 15 tactics incl. Stealth, Defense Impairment, in the page's order)", "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-20.1.json"], ["MITRE attack-stix-data README", "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/README.md"]], "oauth": [["RFC 6749 OAuth 2.0", "https://www.rfc-editor.org/rfc/rfc6749.txt"], ["RFC 7636 PKCE (code_challenge = BASE64URL(SHA256(verifier)))", "https://www.rfc-editor.org/rfc/rfc7636.txt"], ["RFC 9700 Security BCP (implicit SHOULD NOT, password grant MUST NOT, exact redirect matching)", "https://www.rfc-editor.org/rfc/rfc9700.txt"], ["RFC 7662 Token Introspection", "https://www.rfc-editor.org/rfc/rfc7662.txt"], ["RFC 8693 Token Exchange", "https://www.rfc-editor.org/rfc/rfc8693.txt"], ["RFC 8628 Device Authorization Grant", "https://www.rfc-editor.org/rfc/rfc8628.txt"], ["OAuth 2.1 still an Internet-Draft (draft-ietf-oauth-v2-1-17)", "https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/"], ["Wikipedia: OpenID Connect is an authentication layer on OAuth 2.0", "https://en.wikipedia.org/w/index.php?title=OpenID&action=raw"], ["Spring Boot resource server properties (issuerUri, audiences)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/module/spring-boot-security-oauth2-resource-server/src/main/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/OAuth2ResourceServerProperties.java"], ["Quarkus OIDC bearer token guide (quarkus.oidc.token.audience)", "https://raw.githubusercontent.com/quarkusio/quarkus/main/docs/src/main/asciidoc/security-oidc-bearer-token-authentication.adoc"]], "data": [["dbt incremental models (merge on a unique key, schema-change handling)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/docs/build/incremental-models.md"], ["dbt snapshots hard_deletes (SCD type 2)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-configs/hard-deletes.md"], ["Cloud Audit Logs (GCP docs host reachable)", "https://docs.cloud.google.com/logging/docs/audit"]], "datalibs": [["pandas on PyPI (snippet run with the current release)", "https://pypi.org/pypi/pandas/json"], ["Polars on PyPI (snippet run with the current release)", "https://pypi.org/pypi/polars/json"], ["PyArrow on PyPI (dataset + write_table snippet run)", "https://pypi.org/pypi/pyarrow/json"], ["DuckDB on PyPI (read_parquet hive_partitioning snippet run)", "https://pypi.org/pypi/duckdb/json"], ["pandera README (supports pandas and Polars)", "https://raw.githubusercontent.com/unionai-oss/pandera/main/README.md"], ["dbt-expectations README (package metaplane/dbt_expectations)", "https://raw.githubusercontent.com/metaplane/dbt-expectations/main/README.md"]], "dbt": [["dbt BigQuery configs (partition_by, granularity per data_type, insert_overwrite static/dynamic)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-configs/bigquery-configs.md"], ["dbt microbatch (batch_size hour|day|month|year, lookback, --event-time-start/end, dbt retry failed batches, upstream event_time filtering)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/docs/build/incremental-microbatch.md"], ["dbt severity, error_if, warn_if", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-configs/severity.md"], ["dbt hard_deletes (1.9: ignore|invalidate|new_record)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-configs/hard-deletes.md"], ["dbt unit tests (test_type:unit, exclude in prod)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/docs/build/unit-tests.md"], ["dbt target variables (target.project, target.dataset on BigQuery)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/dbt-jinja-functions/target.md"], ["dbt grants (BigQuery roles/bigquery.dataViewer)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-configs/grants.md"], ["dbt graph operators (@ selector)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/node-selection/graph-operators.md"], ["dbt incremental models (on_schema_change values)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/docs/build/incremental-models.md"], ["dbt data_tests property", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/resource-properties/data-tests.md"], ["BigQuery clustered tables (up to four clustering columns)", "https://docs.cloud.google.com/bigquery/docs/clustered-tables"], ["dbt-expectations README (metaplane/dbt_expectations)", "https://raw.githubusercontent.com/metaplane/dbt-expectations/main/README.md"]], "dags": [["Airflow release notes (Airflow 3: catchup_by_default False, create_cron_data_intervals False -> CronTriggerTimetable, schedule_interval/timetable removed, SubDAGs and SLAs removed, providers-standard)", "https://raw.githubusercontent.com/apache/airflow/main/RELEASE_NOTES.rst"], ["Upgrading to Airflow 3 (removed context keys tomorrow_ds/prev_ds/next_ds, no direct metadata DB access, ruff AIR301/302/311/312)", "https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/installation/upgrading_to_airflow3.rst"], ["Airflow models/__init__ (DagBag now from airflow.dag_processing.dagbag; absent before 3.2)", "https://raw.githubusercontent.com/apache/airflow/main/airflow-core/src/airflow/models/__init__.py"], ["Airflow templates reference (ds, ds_nodash, logical_date, var.value, conn)", "https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/templates-ref.rst"], ["Airflow CLI config (backfill create --dag-id/--from-date/--to-date, list-import-errors, --map-index)", "https://raw.githubusercontent.com/apache/airflow/main/airflow-core/src/airflow/cli/cli_config.py"], ["Airflow trigger timetables (CronTriggerTimetable interval= parameter)", "https://raw.githubusercontent.com/apache/airflow/main/airflow-core/src/airflow/timetables/trigger.py"], ["Task SDK macros (ds_add)", "https://raw.githubusercontent.com/apache/airflow/main/task-sdk/src/airflow/sdk/execution_time/macros.py"], ["Google provider GCS sensor (object, deferrable)", "https://raw.githubusercontent.com/apache/airflow/main/providers/google/src/airflow/providers/google/cloud/sensors/gcs.py"], ["Google provider BigQuery operators (BigQueryCheckOperator use_legacy_sql, BigQueryInsertJobOperator)", "https://raw.githubusercontent.com/apache/airflow/main/providers/google/src/airflow/providers/google/cloud/operators/bigquery.py"], ["Google provider GCSToBigQueryOperator", "https://raw.githubusercontent.com/apache/airflow/main/providers/google/src/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py"], ["Google provider CloudRunExecuteJobOperator", "https://raw.githubusercontent.com/apache/airflow/main/providers/google/src/airflow/providers/google/cloud/operators/cloud_run.py"]], "architecture": [["Wikipedia: CAP theorem", "https://en.wikipedia.org/wiki/CAP_theorem?action=raw"], ["Wikipedia: PACELC", "https://en.wikipedia.org/wiki/PACELC_design_principle?action=raw"], ["Wikipedia: Fallacies of distributed computing", "https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing?action=raw"], ["Fowler: CQRS", "https://martinfowler.com/bliki/CQRS.html"], ["Fowler: Event Sourcing", "https://martinfowler.com/eaaDev/EventSourcing.html"], ["Fowler: Strangler Fig", "https://martinfowler.com/bliki/StranglerFigApplication.html"], ["PostgreSQL: gen_random_uuid", "https://www.postgresql.org/docs/current/functions-uuid.html"], ["PostgreSQL: SELECT ... FOR UPDATE SKIP LOCKED", "https://www.postgresql.org/docs/current/sql-select.html"]], "microservices": [["Fowler & Lewis: Microservices", "https://martinfowler.com/articles/microservices.html"], ["Wikipedia: Conway's law", "https://en.wikipedia.org/wiki/Conway%27s_law?action=raw"], ["Resilience4j circuit breaker config properties (source)", "https://raw.githubusercontent.com/resilience4j/resilience4j/master/resilience4j-framework-common/src/main/java/io/github/resilience4j/common/circuitbreaker/configuration/CommonCircuitBreakerConfigurationProperties.java"], ["Resilience4j retry config properties (source)", "https://raw.githubusercontent.com/resilience4j/resilience4j/master/resilience4j-framework-common/src/main/java/io/github/resilience4j/common/retry/configuration/CommonRetryConfigurationProperties.java"], ["MicroProfile Fault Tolerance README", "https://raw.githubusercontent.com/microprofile/microprofile-fault-tolerance/main/README.adoc"], ["MicroProfile FT @Timeout", "https://raw.githubusercontent.com/microprofile/microprofile-fault-tolerance/main/api/src/main/java/org/eclipse/microprofile/faulttolerance/Timeout.java"], ["Cloud Run service-to-service auth (ID tokens)", "https://docs.cloud.google.com/run/docs/authenticating/service-to-service"]], "eventsourcing": [["Fowler: Event Sourcing", "https://martinfowler.com/eaaDev/EventSourcing.html"], ["Fowler: CQRS", "https://martinfowler.com/bliki/CQRS.html"], ["PostgreSQL: CREATE TABLE (identity columns)", "https://www.postgresql.org/docs/current/sql-createtable.html"], ["PostgreSQL: sequence functions (nextval not rolled back)", "https://www.postgresql.org/docs/current/functions-sequence.html"], ["KurrentDB README (EventStoreDB renamed)", "https://raw.githubusercontent.com/kurrent-io/KurrentDB/master/README.md"], ["BigQuery query syntax (QUALIFY)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax"]], "sysdesign": [["Wikipedia: CAP theorem", "https://en.wikipedia.org/wiki/CAP_theorem?action=raw"], ["RFC 9111 HTTP Caching", "https://www.rfc-editor.org/rfc/rfc9111.txt"], ["Wikipedia: Fallacies of distributed computing", "https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing?action=raw"], ["Redis SET (NX/EX)", "https://raw.githubusercontent.com/redis/docs/main/content/commands/set.md"]], "caching": [["RFC 9111 HTTP Caching (s3.5 Authorization)", "https://www.rfc-editor.org/rfc/rfc9111.txt"], ["MDN Cache-Control", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control"], ["BigQuery cached results (~24 h, not charged, non-deterministic skip)", "https://docs.cloud.google.com/bigquery/docs/cached-results"], ["BigQuery materialized views (incremental, smart tuning)", "https://docs.cloud.google.com/bigquery/docs/materialized-views-intro"], ["Apigee ResponseCache policy", "https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy"], ["Memorystore for Valkey", "https://docs.cloud.google.com/memorystore/docs/valkey"], ["Redis INFO (keyspace_hits/misses, evicted_keys)", "https://raw.githubusercontent.com/redis/docs/main/content/commands/info.md"], ["Redis eviction policies", "https://raw.githubusercontent.com/redis/docs/main/content/develop/reference/eviction/index.md"], ["Redis SET", "https://raw.githubusercontent.com/redis/docs/main/content/commands/set.md"], ["Spring Boot caching reference (source)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/documentation/spring-boot-docs/src/docs/antora/modules/reference/pages/io/caching.adoc"], ["Spring Boot CacheProperties (spring.cache.redis.time-to-live / key-prefix)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/module/spring-boot-cache/src/main/java/org/springframework/boot/cache/autoconfigure/CacheProperties.java"], ["Spring Boot DataRedisProperties (spring.data.redis.host/port)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/module/spring-boot-data-redis/src/main/java/org/springframework/boot/data/redis/autoconfigure/DataRedisProperties.java"], ["Caffeine Cache javadoc (compute at most once per key)", "https://raw.githubusercontent.com/ben-manes/caffeine/master/caffeine/src/main/java/com/github/benmanes/caffeine/cache/Cache.java"], ["cachetools cached() signature", "https://raw.githubusercontent.com/tkem/cachetools/master/src/cachetools/__init__.py"], ["redis-py set(ex=...)", "https://raw.githubusercontent.com/redis/redis-py/master/redis/commands/core.py"]], "devops": [["actions/checkout README (v7 current)", "https://raw.githubusercontent.com/actions/checkout/main/README.md"], ["actions/setup-java action.yml / README (v6)", "https://raw.githubusercontent.com/actions/setup-java/main/action.yml"], ["google-github-actions/auth action.yml + README (v3, id-token: write)", "https://raw.githubusercontent.com/google-github-actions/auth/main/README.md"], ["google-github-actions/deploy-cloudrun action.yml (v3, service/region/image)", "https://raw.githubusercontent.com/google-github-actions/deploy-cloudrun/main/action.yml"], ["google-github-actions/setup-gcloud README (v3)", "https://raw.githubusercontent.com/google-github-actions/setup-gcloud/main/README.md"], ["GitHub Actions workflow syntax (path filter leaves required checks Pending; concurrency)", "https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions"], ["Cloud Run rollouts, tags and traffic migration", "https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration"], ["git-log man page (-S)", "https://man7.org/linux/man-pages/man1/git-log.1.html"], ["git-bisect man page", "https://man7.org/linux/man-pages/man1/git-bisect.1.html"], ["Gateway API traffic-split example", "https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/main/examples/standard/traffic-splitting/traffic-split-2.yaml"], ["Fowler: BlueGreenDeployment", "https://martinfowler.com/bliki/BlueGreenDeployment.html"], ["Fowler: CanaryRelease", "https://martinfowler.com/bliki/CanaryRelease.html"], ["Twelve-Factor: disposability (SIGTERM)", "https://raw.githubusercontent.com/heroku/12factor/master/content/en/disposability.md"], ["Twelve-Factor: logs (stdout)", "https://raw.githubusercontent.com/heroku/12factor/master/content/en/logs.md"]], "kubernetes": [["kubectl autoscale reference", "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/"], ["kubectl debug reference", "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/"], ["Service (NodePort range)", "https://kubernetes.io/docs/concepts/services-networking/service/"], ["CronJob (timeZone)", "https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/"], ["Ingress NGINX retirement (Kubernetes blog)", "https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/"], ["GKE Ingress: ingress.class annotation", "https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress"], ["GKE Workload Identity", "https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity"], ["Kustomize images field", "https://raw.githubusercontent.com/kubernetes-sigs/cli-experimental/master/site/content/en/references/kustomize/kustomization/images/_index.md"], ["Kustomize image matching source", "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/api/internal/image/image.go"]], "helm": [["Helm 4 overview (flag renames)", "https://raw.githubusercontent.com/helm/helm-www/main/docs/overview.md"], ["helm upgrade reference", "https://raw.githubusercontent.com/helm/helm-www/main/docs/helm/helm_upgrade.md"], ["Chart hooks", "https://raw.githubusercontent.com/helm/helm-www/main/docs/topics/charts_hooks.md"], ["Chart tests", "https://raw.githubusercontent.com/helm/helm-www/main/docs/topics/chart_tests.md"]], "operators": [["Operator SDK capability levels", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/website/content/en/docs/overview/operator-capabilities.md"], ["Kubebuilder quick start", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/quick-start.md"], ["Java Operator SDK UpdateControl", "https://raw.githubusercontent.com/operator-framework/java-operator-sdk/main/operator-framework-core/src/main/java/io/javaoperatorsdk/operator/api/reconciler/UpdateControl.java"], ["Kopf results stored in status", "https://raw.githubusercontent.com/nolar/kopf/main/docs/results.rst"]], "servicemesh": [["Istio waypoint (--enroll-namespace)", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ambient/usage/waypoint/index.md"], ["Istio ambient: add workloads (no restart)", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ambient/usage/add-workloads/index.md"], ["Istio ambient install with istioctl", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ambient/install/istioctl/index.md"], ["Istio AuthorizationPolicy reference", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/reference/config/security/authorization-policy/index.html"], ["Istio network problems (response flags)", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ops/common-problems/network-issues/index.md"], ["istioctl reference", "https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/reference/commands/istioctl/index.html"], ["Envoy response flags", "https://raw.githubusercontent.com/envoyproxy/envoy/main/docs/root/configuration/advanced/substitution_formatter.rst"], ["linkerd2-proxy README (Rust)", "https://raw.githubusercontent.com/linkerd/linkerd2-proxy/main/README.md"]], "terraform": [["Terraform 1.1 changelog (moved)", "https://raw.githubusercontent.com/hashicorp/terraform/v1.1/CHANGELOG.md"], ["Terraform 1.2 changelog (replace_triggered_by)", "https://raw.githubusercontent.com/hashicorp/terraform/v1.2/CHANGELOG.md"], ["Terraform 1.5 changelog (import, check)", "https://raw.githubusercontent.com/hashicorp/terraform/v1.5/CHANGELOG.md"], ["Terraform 1.6 changelog (terraform test)", "https://raw.githubusercontent.com/hashicorp/terraform/v1.6/CHANGELOG.md"], ["Terraform 1.7 changelog (removed, mock_provider)", "https://raw.githubusercontent.com/hashicorp/terraform/v1.7/CHANGELOG.md"], ["Terraform tests (assertion references)", "https://raw.githubusercontent.com/hashicorp/web-unified-docs/main/content/terraform/v1.14.x/docs/language/tests/index.mdx"], ["Google provider changelog (8.x)", "https://raw.githubusercontent.com/hashicorp/terraform-provider-google/main/CHANGELOG.md"], ["google_bigquery_table", "https://raw.githubusercontent.com/hashicorp/terraform-provider-google/main/website/docs/r/bigquery_table.html.markdown"], ["google_storage_bucket", "https://raw.githubusercontent.com/hashicorp/terraform-provider-google/main/website/docs/r/storage_bucket.html.markdown"], ["google_cloud_run_v2_job", "https://raw.githubusercontent.com/hashicorp/terraform-provider-google/main/website/docs/r/cloud_run_v2_job.html.markdown"], ["google_cloud_scheduler_job", "https://raw.githubusercontent.com/hashicorp/terraform-provider-google/main/website/docs/r/cloud_scheduler_job.html.markdown"], ["Cloud Run: execute jobs on a schedule", "https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule"], ["Cloud Run: execute jobs (overrides need run.developer)", "https://docs.cloud.google.com/run/docs/execute/jobs"], ["cloud-storage module changelog (12.x)", "https://raw.githubusercontent.com/terraform-google-modules/terraform-google-cloud-storage/main/CHANGELOG.md"]], "observability": [["OTLP exporter config (ports, protocol)", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-specification/main/specification/protocol/exporter.md"], ["OTel SDK env vars (samplers)", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-specification/main/specification/configuration/sdk-environment-variables.md"], ["W3C Trace Context header", "https://raw.githubusercontent.com/w3c/trace-context/main/spec/20-http_request_header_format.md"], ["OTel Java agent README", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-java-instrumentation/main/README.md"], ["OTel Python instrumentation README", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-python-contrib/main/opentelemetry-instrumentation/README.rst"], ["Spring Boot tracing (Boot 4 OTLP property)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/documentation/spring-boot-docs/src/docs/antora/modules/reference/pages/actuator/tracing.adoc"], ["Spring Boot observability (annotations)", "https://raw.githubusercontent.com/spring-projects/spring-boot/main/documentation/spring-boot-docs/src/docs/antora/modules/reference/pages/actuator/observability.adoc"], ["Cloud Audit Logs", "https://docs.cloud.google.com/logging/docs/audit"], ["Cloud Logging structured logging", "https://docs.cloud.google.com/logging/docs/structured-logging"]], "sre": [["Cloud Monitoring: alerting on burn rate", "https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate"], ["Cloud Monitoring: SLO concepts (request- and windows-based)", "https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring"], ["Sloth: SRE Workbook window values (28 d)", "https://raw.githubusercontent.com/slok/sloth/main/internal/alert/windows/google-28d.yaml"], ["Site reliability engineering (Wikipedia)", "https://en.wikipedia.org/w/index.php?title=Site_reliability_engineering&action=raw"]], "cloudinside": [["Firecracker README", "https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md"], ["gVisor README", "https://raw.githubusercontent.com/google/gvisor/master/README.md"], ["Kubernetes README (Borg, paper link)", "https://raw.githubusercontent.com/kubernetes/kubernetes/master/README.md"], ["GCP regions and zones", "https://docs.cloud.google.com/compute/docs/regions-zones"], ["Cloud Run container contract (sandboxes, in-memory FS)", "https://docs.cloud.google.com/run/docs/container-contract"]], "cloudcompare": [["AWS App Runner (closed to new customers)", "https://aws.amazon.com/apprunner/"], ["Knowledge Catalog, formerly Dataplex", "https://docs.cloud.google.com/dataplex/docs/introduction"], ["Managed Service for Apache Spark rename", "https://docs.cloud.google.com/dataproc-serverless/docs/overview"], ["Lakehouse, formerly BigLake", "https://docs.cloud.google.com/biglake/docs/introduction"], ["Managed Service for Apache Airflow, formerly Cloud Composer", "https://docs.cloud.google.com/composer/docs"], ["Vertex AI name changes", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes"], ["Microsoft Foundry", "https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry"], ["AWS Quick (Quick Sight)", "https://docs.aws.amazon.com/quicksight/latest/user/welcome.html"], ["Azure Cache for Redis retirement", "https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview"], ["ADF Workflow Orchestration Manager", "https://learn.microsoft.com/en-us/azure/data-factory/concepts-workflow-orchestration-manager"], ["Azure regions list", "https://learn.microsoft.com/en-us/azure/reliability/regions-list"], ["AWS regions", "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html"], ["Aurora DSQL", "https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html"], ["EKS Auto Mode", "https://docs.aws.amazon.com/eks/latest/userguide/automode.html"], ["Fabric Data Engineer (DP-700)", "https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/"]], "gcpdata": [["gcloud pubsub subscriptions create --help (local)", "https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create"], ["Knowledge Catalog, formerly Dataplex", "https://docs.cloud.google.com/dataplex/docs/introduction"], ["Data lineage", "https://docs.cloud.google.com/dataplex/docs/about-data-lineage"], ["Managed Service for Apache Spark", "https://docs.cloud.google.com/dataproc-serverless/docs/overview"], ["Lakehouse, formerly BigLake", "https://docs.cloud.google.com/biglake/docs/introduction"], ["Managed Service for Apache Airflow", "https://docs.cloud.google.com/composer/docs"], ["Vertex AI name changes", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes"], ["BigQuery sharing (formerly Analytics Hub)", "https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction"], ["Datastream overview", "https://docs.cloud.google.com/datastream/docs/overview"], ["BigQuery Data Transfer Service", "https://docs.cloud.google.com/bigquery/docs/dts-introduction"], ["Professional Data Engineer", "https://cloud.google.com/learn/certification/data-engineer"]], "bigquery": [["Quotas and limits (10,000 partitions; DML)", "https://docs.cloud.google.com/bigquery/quotas"], ["Time travel (7 days default)", "https://docs.cloud.google.com/bigquery/docs/time-travel"], ["Other statements (EXPORT DATA)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/other-statements"], ["Pipe syntax", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/pipe-syntax"], ["JSON functions", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions"], ["DDL (partitioning, snapshots, external tables)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language"], ["Lakehouse, formerly BigLake", "https://docs.cloud.google.com/biglake/docs/introduction"], ["bq help (local CLI)", "https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference"]], "cloudrun": [["Container runtime contract", "https://docs.cloud.google.com/run/docs/container-contract"], ["Maximum concurrent requests", "https://docs.cloud.google.com/run/docs/about-concurrency"], ["Troubleshooting (404 ingress, 429)", "https://docs.cloud.google.com/run/docs/troubleshooting"], ["Execute jobs (per-execution overrides)", "https://docs.cloud.google.com/run/docs/execute/jobs"], ["Execute jobs on a schedule (v2 :run URI)", "https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule"], ["Billing settings", "https://docs.cloud.google.com/run/docs/configuring/billing-settings"], ["YAML reference", "https://docs.cloud.google.com/run/docs/reference/yaml/v1"], ["LogEntry severity DEFAULT", "https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry"], ["gcloud run deploy --help (local)", "https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy"]], "apigee": [["What is Apigee", "https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee"], ["Policy reference overview", "https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy"], ["Google authentication (GoogleIDToken)", "https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview"], ["VerifyAPIKey policy", "https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy"], ["SpikeArrest policy", "https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy"], ["Quota policy", "https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy"], ["About API Gateway", "https://docs.cloud.google.com/api-gateway/docs/about-api-gateway"]], "llm": [["Claude models overview (model IDs)", "https://platform.claude.com/docs/en/about-claude/models/overview.md"], ["Agent Platform release notes (Vertex AI renamed, 2026-04-22)", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes"], ["TGI README (maintenance mode)", "https://raw.githubusercontent.com/huggingface/text-generation-inference/main/README.md"], ["vLLM OpenAI-compatible server (port 8000, vllm serve)", "https://raw.githubusercontent.com/vllm-project/vllm/main/docs/getting_started/quickstart.md"], ["vLLM engine args (--max-model-len)", "https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/engine/arg_utils.py"], ["Ollama API (port 11434)", "https://raw.githubusercontent.com/ollama/ollama/main/docs/api.md"], ["llama.cpp server README (-m, --port)", "https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/server/README.md"], ["Claude Agent SDK / tool runner (via code.claude.com)", "https://code.claude.com/docs/en/overview.md"], ["Wikipedia: Large language model", "https://en.wikipedia.org/w/index.php?title=Large_language_model&action=raw"]], "ai": [["Claude models overview (claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5)", "https://platform.claude.com/docs/en/about-claude/models/overview.md"], ["Agent Platform release notes (Vertex AI rename)", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes"], ["BigQuery ML.GENERATE_TEXT (AI.GENERATE_TEXT recommended for new queries)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text"], ["BigQuery ML.GENERATE_EMBEDDING (output column, AI.GENERATE_EMBEDDING note)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding"], ["BigQuery VECTOR_SEARCH syntax", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions"], ["pgvector README (HNSW filtering, iterative scans in recent releases)", "https://raw.githubusercontent.com/pgvector/pgvector/master/README.md"], ["MCP connector / Claude API docs", "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector.md"], ["Wikipedia: Retrieval-augmented generation", "https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=raw"]], "rag": [["Agent Platform release notes (Vertex AI Vector Search renamed Vector Search)", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes"], ["BigQuery VECTOR_SEARCH (base table may be a subquery)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions"], ["BigQuery DDL: CREATE VECTOR INDEX (IVF, TREE_AH)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language"], ["BigQuery ML.GENERATE_EMBEDDING", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding"], ["pgvector README", "https://raw.githubusercontent.com/pgvector/pgvector/master/README.md"], ["Claude models overview", "https://platform.claude.com/docs/en/about-claude/models/overview.md"], ["Wikipedia: Retrieval-augmented generation", "https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=raw"]], "mcp": [["MCP spec 2025-11-25: transports (stdio, Streamable HTTP)", "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/docs/specification/2025-11-25/basic/transports.mdx"], ["MCP spec 2025-11-25: authorization (OAuth 2.1, optional)", "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/docs/specification/2025-11-25/basic/authorization.mdx"], ["MCP Python SDK README (MCPServer)", "https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md"], ["MCP Python SDK migration guide (FastMCP renamed, run(transport=...))", "https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/migration.md"], ["PyPI mcp (current 2.x)", "https://pypi.org/pypi/mcp/json"], ["Claude Code MCP docs", "https://code.claude.com/docs/en/mcp.md"], ["MCP connector (Claude API)", "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector.md"], ["MCP Inspector README and v1-to-v2 guide", "https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/v1-to-v2-migration.md"], ["MCP Toolbox README (repo badge names googleapis/mcp-toolbox)", "https://raw.githubusercontent.com/googleapis/genai-toolbox/main/README.md"]], "agentharness": [["Claude Agent SDK overview", "https://code.claude.com/docs/en/overview.md"], ["Claude Code hooks (deterministic gates)", "https://code.claude.com/docs/en/hooks.md"], ["Claude Code subagents", "https://code.claude.com/docs/en/sub-agents.md"], ["Penstock README (main)", "https://raw.githubusercontent.com/enrichmeai/penstock/main/README.md"]], "blueprints": [["Wikipedia: Inner-platform effect", "https://en.wikipedia.org/w/index.php?title=Inner-platform_effect&action=raw"], ["Wikipedia: Rule of three (computer programming)", "https://en.wikipedia.org/w/index.php?title=Rule_of_three_(computer_programming)&action=raw"], ["Claude Code skills (repo context files, skills)", "https://code.claude.com/docs/en/skills.md"]], "claudetools": [["Claude Code CLI reference (-c, -r, -p, --output-format)", "https://code.claude.com/docs/en/cli-reference.md"], ["Claude Code commands (/init, /memory, /agents, /mcp, /permissions, /compact, /clear)", "https://code.claude.com/docs/en/commands.md"], ["Claude Code interactive mode (Shift+Tab cycles modes)", "https://code.claude.com/docs/en/interactive-mode.md"], ["Claude Code permission modes", "https://code.claude.com/docs/en/permission-modes.md"], ["Claude Code permissions (Bash(x:*) equals Bash(x *))", "https://code.claude.com/docs/en/permissions.md"], ["Claude Code hooks (exit code 2 per event)", "https://code.claude.com/docs/en/hooks.md"], ["Claude Code skills (custom commands merged into skills)", "https://code.claude.com/docs/en/skills.md"], ["Claude Code subagents", "https://code.claude.com/docs/en/sub-agents.md"], ["Claude Code memory (CLAUDE.md locations)", "https://code.claude.com/docs/en/memory.md"], ["Claude Code overview (surfaces)", "https://code.claude.com/docs/en/overview.md"], ["Cowork overview", "https://claude.com/docs/cowork/overview.md"]], "copilot": [["About GitHub Copilot", "https://docs.github.com/api/article/body?pathname=/en/copilot/get-started/features"], ["Copilot on GitHub.com (cloud agent, Copilot in the cloud)", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/agents/coding-agent/about-coding-agent"], ["Copilot cloud agent how-tos", "https://docs.github.com/api/article/body?pathname=/en/copilot/how-tos/use-copilot-agents/cloud-agent"], ["Starting Copilot sessions (some entry points open a PR)", "https://docs.github.com/api/article/body?pathname=/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions"], ["Using cloud agent on GitHub (assign an issue)", "https://docs.github.com/api/article/body?pathname=/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github"], ["Custom instructions (copilot-instructions.md, .instructions.md, AGENTS.md/CLAUDE.md)", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/prompting/response-customization"], ["Your first prompt file (.github/prompts)", "https://docs.github.com/api/article/body?pathname=/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file"], ["Copilot CLI", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/agents/copilot-cli/about-copilot-cli"], ["Copilot code review", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/agents/code-review"], ["Content exclusion", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/content-exclusion"], ["Supported AI models (includes Claude)", "https://docs.github.com/api/article/body?pathname=/en/copilot/reference/ai-models/supported-models"]], "agentsgcp": [["Agent Platform release notes (Vertex AI renamed)", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes"], ["Cloud Run: execute jobs on a schedule (run.googleapis.com/v2 ...:run)", "https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule"], ["Cloud Run: rollouts, tags, tagged URL format", "https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration"], ["Cloud Run jobs", "https://docs.cloud.google.com/run/docs/create-jobs"], ["gcloud workstations configs create --help (local gcloud; --idle-timeout in seconds)", "https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create"], ["gcloud run jobs create / execute --help (local gcloud)", "https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/execute"]], "harness": [["GitHub Actions workflow syntax (jobs, services, matrix, on:)", "https://docs.github.com/api/article/body?pathname=/en/actions/writing-workflows/workflow-syntax-for-github-actions"], ["Harness open source repo (reachable; not the SaaS docs)", "https://raw.githubusercontent.com/harness/harness/main/README.md"], ["Cloud Run tags (for the GCP side)", "https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration"]], "opstools": [["Prometheus configuration (metrics_path, rule_files, alertmanagers)", "https://raw.githubusercontent.com/prometheus/prometheus/main/docs/configuration/configuration.md"], ["Prometheus alerting rules (for:)", "https://raw.githubusercontent.com/prometheus/prometheus/main/docs/configuration/alerting_rules.md"], ["Alertmanager configuration (matchers, group_wait, pagerduty routing_key_file)", "https://raw.githubusercontent.com/prometheus/alertmanager/main/docs/configuration.md"], ["Fluent Bit tail input (multiline.parser)", "https://raw.githubusercontent.com/fluent/fluent-bit-docs/master/pipeline/inputs/tail.md"], ["Fluent Bit multiline parsers (cri)", "https://raw.githubusercontent.com/fluent/fluent-bit-docs/master/pipeline/parsers/multiline-parsing.md"], ["Fluent Bit grep filter (Exclude KEY REGEX)", "https://raw.githubusercontent.com/fluent/fluent-bit-docs/master/pipeline/filters/grep.md"], ["Fluent Bit stackdriver output", "https://raw.githubusercontent.com/fluent/fluent-bit-docs/master/pipeline/outputs/stackdriver.md"], ["Fluentd in_tail (pos_file)", "https://raw.githubusercontent.com/fluent/fluentd-docs-gitbook/1.0/input/tail.md"], ["Fluentd record_transformer", "https://raw.githubusercontent.com/fluent/fluentd-docs-gitbook/1.0/filter/record_transformer.md"], ["Grafana provisioning (datasource YAML)", "https://raw.githubusercontent.com/grafana/grafana/main/docs/sources/administration/provisioning/index.md"]], "science": [["Wikipedia: Is-ought problem (Hume)", "https://en.wikipedia.org/wiki/Is%E2%80%93ought_problem?action=raw"], ["Wikipedia: Non-overlapping magisteria (Gould)", "https://en.wikipedia.org/wiki/Non-overlapping_magisteria?action=raw"], ["Wikipedia: Scientism", "https://en.wikipedia.org/wiki/Scientism?action=raw"], ["Wikipedia: Falsifiability (Popper)", "https://en.wikipedia.org/wiki/Falsifiability?action=raw"], ["Wikipedia: Accuracy and precision", "https://en.wikipedia.org/wiki/Accuracy_and_precision?action=raw"]], "philosophy": [["Wikipedia: Conway's law (Datamation, April 1968)", "https://en.wikipedia.org/wiki/Conway%27s_law?action=raw"], ["Wikipedia: The Innovator's Dilemma (1997)", "https://en.wikipedia.org/wiki/The_Innovator%27s_Dilemma?action=raw"], ["Wikipedia: Loss aversion (Kahneman and Tversky)", "https://en.wikipedia.org/wiki/Loss_aversion?action=raw"], ["Wikipedia: Goodhart's law", "https://en.wikipedia.org/wiki/Goodhart%27s_law?action=raw"], ["Wikipedia: Hanlon's razor", "https://en.wikipedia.org/wiki/Hanlon%27s_razor?action=raw"], ["Wikipedia: Abductive reasoning", "https://en.wikipedia.org/wiki/Abductive_reasoning?action=raw"], ["Wikipedia: Stoicism", "https://en.wikipedia.org/wiki/Stoicism?action=raw"], ["Wikipedia: Programming ethics (ACM code principles)", "https://en.wikipedia.org/wiki/Programming_ethics?action=raw"]], "goodhuman": [["Wikipedia: Occupational burnout (WHO 'occupational phenomenon')", "https://en.wikipedia.org/wiki/Occupational_burnout?action=raw"], ["Wikipedia: Psychological safety", "https://en.wikipedia.org/wiki/Psychological_safety?action=raw"], ["Wikipedia: Programming ethics (ACM code: avoid harm, be honest)", "https://en.wikipedia.org/wiki/Programming_ethics?action=raw"], ["W3C WCAG 2.2", "https://www.w3.org/TR/WCAG22/"]], "web3": [["Wikipedia: Web3 (term coined by Gavin Wood, 2014)", "https://en.wikipedia.org/wiki/Web3?action=raw"], ["Wikipedia: Semantic Web ('sometimes known as Web 3.0')", "https://en.wikipedia.org/wiki/Semantic_Web?action=raw"], ["Wikipedia: Ethereum (The Merge, proof of stake)", "https://en.wikipedia.org/wiki/Ethereum?action=raw"], ["ethereum.org: scaling and rollups", "https://raw.githubusercontent.com/ethereum/ethereum-org-website/dev/public/content/developers/docs/scaling/index.md"], ["ethereum.org: ERC-20", "https://raw.githubusercontent.com/ethereum/ethereum-org-website/dev/public/content/developers/docs/standards/tokens/erc-20/index.md"], ["ethereum.org: ERC-721", "https://raw.githubusercontent.com/ethereum/ethereum-org-website/dev/public/content/developers/docs/standards/tokens/erc-721/index.md"], ["Solidity docs: events", "https://raw.githubusercontent.com/ethereum/solidity/develop/docs/contracts/events.rst"], ["W3C RDF 1.1 Concepts", "https://www.w3.org/TR/rdf11-concepts/"], ["W3C SPARQL 1.1 Query", "https://www.w3.org/TR/sparql11-query/"], ["W3C JSON-LD 1.1", "https://www.w3.org/TR/json-ld11/"], ["schema.org vocabulary (sku, gtin13)", "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/schema.ttl"]], "solid": [["Solid Protocol (spec source)", "https://raw.githubusercontent.com/solid/specification/main/protocol.html"], ["Web Access Control (spec source)", "https://raw.githubusercontent.com/solid/web-access-control-spec/main/index.html"], ["Solid-OIDC (spec source, solid:oidcIssuer)", "https://raw.githubusercontent.com/solid/solid-oidc/main/index.bs"], ["Solid Notifications Protocol", "https://raw.githubusercontent.com/solid/notifications/main/protocol.html"], ["Wikipedia: Solid project (led by Tim Berners-Lee)", "https://en.wikipedia.org/wiki/Solid_project?action=raw"], ["Inrupt authn-browser: exported fetch/login/handleIncomingRedirect", "https://raw.githubusercontent.com/inrupt/solid-client-authn-js/main/packages/browser/src/defaultSession.ts"], ["Inrupt login options (oidcIssuer, redirectUrl, clientName)", "https://raw.githubusercontent.com/inrupt/solid-client-authn-js/main/packages/core/src/ILoginInputOptions.ts"], ["Community Solid Server README", "https://raw.githubusercontent.com/CommunitySolidServer/CommunitySolidServer/main/README.md"], ["Cistern README (open Solid pod server, Apache 2.0), read at its latest release tag in a local clone", "https://github.com/enrichmeai/cistern/blob/v0.3.1/README.md"]], "quantum": [["Wikipedia: Shor's algorithm", "https://en.wikipedia.org/wiki/Shor%27s_algorithm?action=raw"], ["Wikipedia: Post-quantum cryptography (FIPS 203/204/205)", "https://en.wikipedia.org/wiki/Post-quantum_cryptography?action=raw"], ["Qiskit README", "https://raw.githubusercontent.com/Qiskit/qiskit/main/README.md"], ["Open Quantum Safe liboqs README", "https://raw.githubusercontent.com/open-quantum-safe/liboqs/main/README.md"]], "robotics": [["Wikipedia: Robot Operating System", "https://en.wikipedia.org/wiki/Robot_Operating_System?action=raw"], ["Wikipedia: PID controller", "https://en.wikipedia.org/wiki/PID_controller?action=raw"], ["ROS 2 README", "https://raw.githubusercontent.com/ros2/ros2/rolling/README.md"]], "bitcoin": [["Wikipedia: Bitcoin (31 Oct 2008, 3 Jan 2009, halving every 210,000 blocks)", "https://en.wikipedia.org/wiki/Bitcoin?action=raw"], ["Wikipedia: Bitcoin protocol", "https://en.wikipedia.org/wiki/Bitcoin_protocol?action=raw"], ["Wikipedia: Ethereum (The Merge, 15 Sept 2022, >99% energy cut)", "https://en.wikipedia.org/wiki/Ethereum?action=raw"], ["Bitcoin Core README", "https://raw.githubusercontent.com/bitcoin/bitcoin/master/README.md"]], "go": [["Effective Go", "https://go.dev/doc/effective_go"], ["Go blog: Working with errors in Go 1.13 (%w, errors.Is)", "https://go.dev/blog/go1.13-errors"], ["Data race detector", "https://go.dev/doc/articles/race_detector"], ["Go blog: Go maps in action (nil map write panics)", "https://go.dev/blog/maps"]], "rust": [["The Rust book: Unsafe Rust", "https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html"], ["The Rust book: What is ownership?", "https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html"], ["The Rust book: Recoverable errors with Result", "https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html"]], "awsdata": [["Amazon S3 Tables", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html"], ["What is Lake Formation", "https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html"], ["Athena workgroup data usage controls", "https://docs.aws.amazon.com/athena/latest/ug/workgroups-setting-control-limits-cloudwatch.html"], ["Redshift Data API ExecuteStatement", "https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ExecuteStatement.html"], ["botocore Athena service definition", "https://raw.githubusercontent.com/boto/botocore/develop/botocore/data/athena/2017-05-18/service-2.json"]], "k8sdr": [["Operating etcd clusters for Kubernetes", "https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/"], ["Disruptions and PodDisruptionBudgets", "https://kubernetes.io/docs/concepts/workloads/pods/disruptions/"], ["Pod topology spread constraints", "https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/"], ["Configuration best practices", "https://kubernetes.io/docs/concepts/configuration/overview/"], ["Velero: disaster recovery", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/site/content/docs/main/disaster-case.md"], ["AWS whitepaper: DR options in the cloud", "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"]]}""")
FACTCHECK_PENDING=_json.loads(r"""{"docker": 2, "sql": 4, "database": 2, "python": 2, "apis": 2, "graphql": 2, "kafka": 2, "payments": 5, "quarkus": 2, "performance": 2, "security": 2, "oauth": 2, "data": 2, "datalibs": 2, "dbt": 2, "dags": 2, "architecture": 1, "microservices": 1, "eventsourcing": 2, "sysdesign": 2, "caching": 2, "devops": 3, "kubernetes": 1, "observability": 2, "sre": 4, "cloudinside": 1, "cloudcompare": 3, "gcpdata": 3, "bigquery": 2, "cloudrun": 2, "apigee": 3, "llm": 4, "ai": 4, "rag": 4, "mcp": 4, "agentharness": 3, "blueprints": 3, "claudetools": 3, "copilot": 3, "agentsgcp": 3, "harness": 6, "opstools": 4, "science": 2, "philosophy": 3, "goodhuman": 1, "web3": 2, "solid": 1, "robotics": 1}""")
for _t,_s in FACTCHECK_SOURCES.items():
    if _t in D:
        _have={u for _,u in D[_t].get("sources",[])}
        D[_t].setdefault("sources",[]).extend([[n,u] for n,u in _s if u not in _have])
        if FACTCHECK_PENDING.get(_t): D[_t]["pending"]=FACTCHECK_PENDING[_t]

D["culvert"].setdefault("sources",[]).extend([["Culvert repository","https://github.com/enrichmeai/culvert"],["Culvert on PyPI","https://pypi.org/project/culvert/"],["The Culvert page on this site, kept in step with Maven Central and PyPI by the release checker","https://enrichmeai.com/culvert/"]])

# Round two of the fact check: new sources, and which pages still have claims to confirm.
ROUND2_SOURCES=_json.loads(r"""{"payments": [["Razorpay: validate webhooks (X-Razorpay-Signature, x-razorpay-event-id)", "https://razorpay.com/docs/webhooks/validate-test/"], ["Razorpay: settlement FAQs (standard cycle T+2 working days)", "https://razorpay.com/docs/payments/settlements/faqs/"], ["RBI: Storage of Payment System Data", "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0"], ["RBI: Card-on-File Tokenisation", "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12159&Mode=0"], ["RBI: e-mandate on cards for recurring transactions", "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0"], ["Stripe: supported currencies and minor units", "https://docs.stripe.com/currencies"]], "apis": [["Enterprise Integration Patterns: integration styles", "https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html"], ["IETF draft: the Idempotency-Key HTTP header", "https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/"]], "graphql": [["Spring Boot reference: Spring for GraphQL", "https://docs.spring.io/spring-boot/reference/web/spring-graphql.html"], ["GraphQL over HTTP (working draft)", "https://github.com/graphql/graphql-over-http/blob/main/spec/GraphQLOverHTTP.md"]], "kafka": [["confluent-kafka Python API reference", "https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html"]], "eventsourcing": [["Apache Kafka: uses (event sourcing)", "https://kafka.apache.org/uses/"]], "quarkus": [["SmallRye Mutiny: retrying", "https://smallrye.io/smallrye-mutiny/latest/tutorials/retrying/"], ["SmallRye Mutiny: handling timeouts", "https://smallrye.io/smallrye-mutiny/latest/guides/handling-timeouts/"], ["Quarkus blog: new benchmarks (native trade-off)", "https://github.com/quarkusio/quarkusio.github.io/blob/a1d77b2bd0eae64e7492209262ecfa3ff60233e4/content/posts/2026/2026-03-02-new-benchmarks.adoc"]], "oauth": [["OpenID Connect Core", "https://openid.net/specs/openid-connect-core-1_0.html"]], "python": [["What's new in Python 3.15", "https://docs.python.org/3.15/whatsnew/3.15.html"], ["uv docs: environments", "https://github.com/astral-sh/uv/blob/main/docs/pip/environments.md"], ["Ruff docs: linter", "https://github.com/astral-sh/ruff/blob/main/docs/linter.md"]], "docker": [["Docker CLI: docker buildx build (--platform default)", "https://docs.docker.com/reference/cli/docker/buildx/build/"]], "sql": [["BigQuery: optimize query computation (ORDER BY)", "https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute"], ["BigQuery: approximate aggregate functions", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/approximate_aggregate_functions"], ["BigQuery: query syntax (QUALIFY)", "https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax"]], "database": [["Citus (distributed Postgres)", "https://github.com/citusdata/citus"], ["Vitess (sharded MySQL)", "https://github.com/vitessio/vitess"], ["Spanner: schema and data model (splits)", "https://docs.cloud.google.com/spanner/docs/schema-and-data-model"]], "devops": [["DORA metrics guide", "https://dora.dev/guides/dora-metrics-four-keys/"], ["SRE book: Monitoring distributed systems (golden signals)", "https://sre.google/sre-book/monitoring-distributed-systems/"], ["Argo Rollouts README", "https://raw.githubusercontent.com/argoproj/argo-rollouts/master/README.md"], ["Flagger README", "https://raw.githubusercontent.com/fluxcd/flagger/main/README.md"], ["Harness deployment strategies", "https://developer.harness.io/docs/continuous-delivery/manage-deployments/deployment-concepts/"]], "sre": [["SRE Workbook: Alerting on SLOs", "https://sre.google/workbook/alerting-on-slos/"], ["SRE book: Eliminating toil", "https://sre.google/sre-book/eliminating-toil/"], ["SRE Workbook: Example error budget policy", "https://sre.google/workbook/error-budget-policy/"], ["SRE book: Managing incidents", "https://sre.google/sre-book/managing-incidents/"]], "microservices": [["Spring Framework: REST clients (RestClient)", "https://docs.spring.io/spring-framework/reference/integration/rest-clients.html"], ["Resilience4j Spring Boot guide (annotations, fallback signature)", "https://resilience4j.readme.io/docs/getting-started-3"]], "caching": [["Spring Framework: cache annotations (proxy mode, self-invocation)", "https://docs.spring.io/spring-framework/reference/integration/cache/annotations.html"], ["Claude docs: prompt caching", "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"]], "security": [["gcloud secrets reference", "https://docs.cloud.google.com/sdk/gcloud/reference/secrets/create"], ["Spring Security: JWT resource server", "https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html"], ["Spring Security: session management (STATELESS)", "https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html"], ["Spring Framework: JdbcClient", "https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html"]], "architecture": [["PostgreSQL PREPARE (positional parameters)", "https://www.postgresql.org/docs/current/sql-prepare.html"]], "sysdesign": [["Latency numbers every programmer should know (Dean, collected by Bon\u00e9r)", "https://gist.github.com/jboner/2841832"]], "kubernetes": [["Bitnami Redis chart README", "https://raw.githubusercontent.com/bitnami/charts/main/bitnami/redis/README.md"]], "observability": [["OTel Collector googlecloud exporter", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector-contrib/main/exporter/googlecloudexporter/README.md"], ["OTel Collector googlemanagedprometheus exporter", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector-contrib/main/exporter/googlemanagedprometheusexporter/README.md"], ["gcloud logging metrics create", "https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/create"]], "performance": [["Python docs: profiling.tracing (cProfile)", "https://docs.python.org/3/library/profiling.tracing.html"], ["Python docs: pstats", "https://docs.python.org/3/library/pstats.html"]], "data": [["Datastream overview", "https://docs.cloud.google.com/datastream/docs/overview"], ["Managed Service for Apache Spark (formerly Dataproc)", "https://docs.cloud.google.com/dataproc/docs/concepts/overview"]], "datalibs": [["Kafka Streams introduction", "https://kafka.apache.org/42/streams/introduction/"], ["Apache Beam README (runners)", "https://raw.githubusercontent.com/apache/beam/master/README.md"], ["Spring Batch introduction", "https://docs.spring.io/spring-batch/reference/spring-batch-intro.html"], ["BigQuery DataFrames introduction", "https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction"]], "dbt": [["dbt show", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/commands/show.md"], ["dbt list", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/commands/list.md"], ["dbt run-operation", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/commands/run-operation.md"], ["dbt defer", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/node-selection/defer.md"], ["dbt deprecations (test arguments)", "https://raw.githubusercontent.com/dbt-labs/docs.getdbt.com/current/website/docs/reference/deprecations.md"]], "dags": [["Astronomer Cosmos example DAG (imports)", "https://raw.githubusercontent.com/astronomer/astronomer-cosmos/main/dev/dags/basic_cosmos_dag.py"]], "harness": [["Harness expressions reference (artifacts.primary.tag)", "https://developer.harness.io/harness-platform/use-harness-platform/variables-and-expressions/harness-expressions-reference.md"], ["Harness CI codebase variables (commitSha, shortCommitSha)", "https://developer.harness.io/continuous-integration/use-harness-ci/use-harness-ci/codebase-configuration/built-in-cie-codebase-variables-reference.md"], ["Harness approval stages (HarnessApproval YAML)", "https://developer.harness.io/harness-platform/use-harness-platform/approvals/adding-harness-approval-stages.md"], ["Harness Build and Push to GAR", "https://developer.harness.io/continuous-integration/use-harness-ci/use-harness-ci/build-and-upload-artifacts/build-and-push/build-and-push-to-gar.md"], ["Harness Cloud build infrastructure (runtime type Cloud)", "https://developer.harness.io/continuous-integration/use-harness-ci/use-harness-ci/set-up-build-infrastructure/use-harness-cloud-build-infrastructure.md"], ["Harness GCP connector (OIDC)", "https://developer.harness.io/harness-platform/use-harness-platform/connectors/cloud-providers/connect-to-google-cloud-platform-gcp/gcs-connector-settings-reference.md"], ["Harness Feature Flags to FME migration", "https://developer.harness.io/feature-flags/new-to-feature-flags/migrate-to-fme.md"]], "opstools": [["Dynatrace DQL data source commands (fetch)", "https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands"], ["Dynatrace Intelligence (formerly Davis)", "https://docs.dynatrace.com/docs/dynatrace-intelligence"], ["Dynatrace Grail", "https://docs.dynatrace.com/docs/platform/grail"], ["Prometheus recording rule naming", "https://raw.githubusercontent.com/prometheus/docs/main/docs/practices/rules.md"]], "blueprints": [["Backstage plugin directory (scorecard plugins)", "https://backstage.io/plugins/"]], "agentharness": [["Penstock README at", "https://github.com/enrichmeai/penstock/blob/v0.6.0/README.md"]], "llm": [["Ollama library: llama3.1", "https://ollama.com/library/llama3.1"], ["Cloud Run GPU support", "https://docs.cloud.google.com/run/docs/configuring/services/gpu"]], "rag": [["Claude citations", "https://platform.claude.com/docs/en/build-with-claude/citations.md"], ["pgvector hybrid search RRF example (k = 60)", "https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py"], ["Google Cloud ranking API (Agent Search)", "https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking"], ["PostgreSQL text search controls", "https://www.postgresql.org/docs/current/textsearch-controls.html"]], "mcp": [["BigQuery Python QueryJob reference", "https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob"]], "ai": [["Agent Platform IAM roles (aiplatform.user)", "https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform"], ["Claude models on Google Cloud: endpoints", "https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed.md"]], "claudetools": [["Get started with Claude Cowork", "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork"], ["Penstock README at", "https://github.com/enrichmeai/penstock/blob/v0.6.0/README.md"]], "copilot": [["Copilot usage metrics", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics"], ["Copilot code referencing (public code policy)", "https://docs.github.com/api/article/body?pathname=/en/copilot/concepts/completions/code-referencing"], ["Copilot Chat in GitHub Mobile", "https://docs.github.com/api/article/body?pathname=/en/copilot/how-tos/chat-with-copilot/chat-in-mobile"]], "agentsgcp": [["gcloud workstations configs create", "https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create"], ["gcloud run jobs create", "https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create"], ["Secret Manager audit logging", "https://docs.cloud.google.com/secret-manager/docs/audit-logging"], ["Penstock README at", "https://github.com/enrichmeai/penstock/blob/v0.6.0/README.md"]], "philosophy": [["Amazon 2015 letter to shareowners (SEC exhibit)", "https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm"], ["Amazon leadership principles", "https://www.aboutamazon.com/about-us/leadership-principles"], ["Wikipedia: G. K. Chesterton (Chesterton's fence)", "https://en.wikipedia.org/wiki/G._K._Chesterton?action=raw"]], "goodhuman": [["Google re:Work: Understand team effectiveness (Project Aristotle)", "https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness"]], "robotics": [["Wikipedia: ISO 10218", "https://en.wikipedia.org/wiki/ISO_10218?action=raw"]], "science": [["Wikipedia: Memory hierarchy (latency table)", "https://en.wikipedia.org/wiki/Memory_hierarchy?action=raw"], ["Wikipedia: Optical fiber (signal speed)", "https://en.wikipedia.org/wiki/Optical_fiber?action=raw"]], "web3": [["Wikipedia: WazirX (India's 2022 crypto tax)", "https://en.wikipedia.org/wiki/WazirX?action=raw"]], "solid": [["Solid CG minutes: Flanders use case", "https://github.com/solid/specification/blob/main/meetings/2023-06-14.md"], ["Solid CG minutes: UK GDS pilot", "https://github.com/solid/specification/blob/main/meetings/2022-10-19.md"]], "cloudcompare": [["Azure Front Door overview", "https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview"], ["AWS CLI reference", "https://docs.aws.amazon.com/cli/latest/reference/"], ["Azure CLI reference", "https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest"]], "cloudinside": [], "cloudrun": [["Cloud Run release notes", "https://docs.cloud.google.com/run/docs/release-notes"], ["Spring Boot: Dockerfiles", "https://docs.spring.io/spring-boot/reference/packaging/container-images/dockerfiles.html"]], "gcpdata": [["Dataflow: write to BigQuery", "https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery"], ["Knowledge Catalog: auto data quality", "https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview"]], "bigquery": [["BigQuery quotas and limits (DML)", "https://docs.cloud.google.com/bigquery/quotas"], ["BigQuery pricing", "https://cloud.google.com/bigquery/pricing"]], "apigee": [["Apigee organisation structure", "https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure"], ["Apigee pricing", "https://cloud.google.com/apigee/pricing"], ["API Gateway pricing", "https://cloud.google.com/api-gateway/pricing"], ["apigeecli", "https://github.com/apigee/apigeecli"], ["Apigee deploy Maven plugin", "https://github.com/apigee/apigee-deploy-maven-plugin"]]}""")
ROUND2_PENDING=_json.loads(r"""{"payments": 1, "apis": 0, "graphql": 0, "kafka": 0, "eventsourcing": 1, "quarkus": 1, "oauth": 1, "python": 1, "docker": 0, "sql": 0, "database": 0, "devops": 1, "sre": 0, "microservices": 0, "caching": 0, "security": 0, "architecture": 1, "sysdesign": 1, "kubernetes": 0, "observability": 0, "performance": 1, "data": 1, "datalibs": 1, "dbt": 0, "dags": 1, "harness": 2, "opstools": 2, "blueprints": 2, "agentharness": 0, "llm": 1, "rag": 1, "mcp": 1, "ai": 1, "claudetools": 1, "copilot": 0, "agentsgcp": 0, "philosophy": 0, "goodhuman": 0, "robotics": 1, "science": 1, "web3": 2, "solid": 0, "cloudcompare": 2, "cloudinside": 1, "cloudrun": 1, "gcpdata": 0, "bigquery": 1, "apigee": 1}""")
for _t,_s in ROUND2_SOURCES.items():
    if _t in D:
        _have={u for _,u in D[_t].get("sources",[])}
        D[_t].setdefault("sources",[]).extend([[n,u] for n,u in _s if u not in _have])
for _t,_n in ROUND2_PENDING.items():
    if _t in D:
        if _n: D[_t]["pending"]=_n
        else: D[_t].pop("pending",None)

# Monorepo cards on Microservices (2026-11-17)
D["microservices"].setdefault("sources",[]).extend([
 ("Wikipedia: Monorepo (advantages, limits, who runs one, scaling tools)","https://en.wikipedia.org/wiki/Monorepo"),
 ("Wikipedia: Conway's law","https://en.wikipedia.org/wiki/Conway%27s_law"),
 ("git sparse-checkout","https://git-scm.com/docs/git-sparse-checkout"),
 ("Git partial clone","https://git-scm.com/docs/partial-clone"),
 ("GitHub: About code owners","https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners"),
 ("GitHub: Troubleshooting required status checks (skipped but required checks)","https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks"),
 ("Nx README (runs only what is affected)","https://github.com/nrwl/nx"),
 ("Uber Technology Day: Monorepo to Multirepo and Back Again (talk, 2017, cited by Wikipedia)","https://www.youtube.com/watch?v=lV8-1S28ycM")])

D["testing"].setdefault("sources",[]).extend([
 ("Playwright README","https://github.com/microsoft/playwright"),("Playwright docs: auto-waiting (actionability)","https://playwright.dev/docs/actionability"),
 ("Playwright docs: locators","https://playwright.dev/docs/locators"),("Playwright docs: assertions","https://playwright.dev/docs/test-assertions"),
 ("Playwright docs: Trace Viewer","https://playwright.dev/docs/trace-viewer-intro"),("Playwright docs: API testing","https://playwright.dev/docs/api-testing"),
 ("Newman README","https://github.com/postmanlabs/newman"),("Postman sandbox (pm API)","https://github.com/postmanlabs/postman-sandbox"),("Wikipedia: Postman","https://en.wikipedia.org/wiki/Postman_(software)"),
 ("REST Assured","https://github.com/rest-assured/rest-assured"),("HTTPX","https://github.com/encode/httpx"),("Bruno README","https://github.com/usebruno/bruno"),
 ("k6 README","https://github.com/grafana/k6"),("Gatling README","https://github.com/gatling/gatling"),("Locust README","https://github.com/locustio/locust"),("Apache JMeter README","https://github.com/apache/jmeter")])
D["performance"].setdefault("sources",[]).extend([
 ("Oracle: Java 21 GC tuning, available collectors","https://docs.oracle.com/en/java/javase/21/gctuning/available-collectors.html"),
 ("Oracle: the java command (MaxRAMPercentage)","https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html")])

D["atob"]["sources"].extend([
 ("Wikipedia: Parallel running","https://en.wikipedia.org/wiki/Parallel_running"),("Wikipedia: Change data capture","https://en.wikipedia.org/wiki/Change_data_capture"),
 ("AWS Prescriptive Guidance: Anti-corruption layer pattern","https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html"),
 ("AWS Prescriptive Guidance: Branch by abstraction","https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html"),
 ("AWS Prescriptive Guidance: Transactional outbox (dual writes)","https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html"),
 ("AWS Prescriptive Guidance: Database-per-service","https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/database-per-service.html"),
 ("AWS Prescriptive Guidance: Shared-database-per-service","https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/shared-database.html"),
 ("Azure Architecture Center: Anti-corruption layer","https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer"),
 ("Debezium README","https://github.com/debezium/debezium")])
D["microservices"].setdefault("sources",[]).extend([
 ("Hystrix README (maintenance mode)","https://github.com/Netflix/Hystrix"),("Resilience4j README","https://github.com/resilience4j/resilience4j"),
 ("Fowler: CircuitBreaker","https://martinfowler.com/bliki/CircuitBreaker.html"),("Wikipedia: Circuit breaker design pattern","https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern"),
 ("Envoy: Circuit breaking","https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking"),("Envoy: Outlier detection","https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/outlier"),
 ("Istio: Circuit breaking task","https://istio.io/latest/docs/tasks/traffic-management/circuit-breaking/"),("Istio API: DestinationRule","https://github.com/istio/api/blob/master/networking/v1alpha3/destination_rule.proto"),
 ("MicroProfile Fault Tolerance","https://github.com/eclipse/microprofile-fault-tolerance")])

D["distsys"]=dict(
 F=["Name the fallacies of distributed computing and give an example of each","Explain CAP and PACELC, and what each letter means","Explain why a five-node cluster survives two failures"],
 P=["Read a database's consistency guarantees and say what they mean for your code","Design timeouts, retries and idempotency for partial failure","Explain Lamport timestamps, vector clocks and generation clocks"],
 S=["Explain how Raft elects a leader and replicates a log","Choose consistency per use case and design for its staleness","Plan chaos and client-history tests for a service"],
 E=["Design a replicated component and its failure handling","Build deterministic simulation testing into a system from the start","Set an organisation's standards for distributed correctness"],
 topics=["Fallacies of distributed computing","CAP and PACELC","Linearizability and eventual consistency","Logical clocks","Consensus: Raft and Paxos","Quorums, leases and split brain","Deterministic simulation testing"],
 links=[("Unmesh Joshi: Deterministic Simulation Testing","https://martinfowler.com/articles/deterministic-simulation-testing.html","The article this page's testing section draws on"),
        ("Unmesh Joshi: Patterns of Distributed Systems","https://martinfowler.com/articles/patterns-of-distributed-systems/","The catalogue of patterns"),
        ("Tickloom","https://github.com/unmeshjoshi/tickloom","A Java library for learning deterministic simulation"),
        ("TigerBeetle: Deterministic Simulation Testing","https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/internals/vopr.md","How the VOPR simulator works"),
        ("The Raft paper and visualisation","https://raft.github.io/","Raft explained by its authors")],
 sources=[("Unmesh Joshi: Deterministic Simulation Testing","https://martinfowler.com/articles/deterministic-simulation-testing.html"),
          ("Unmesh Joshi: Catalog of Patterns of Distributed Systems","https://martinfowler.com/articles/patterns-of-distributed-systems/"),
          ("Write-Ahead Log","https://martinfowler.com/articles/patterns-of-distributed-systems/write-ahead-log.html"),("HeartBeat","https://martinfowler.com/articles/patterns-of-distributed-systems/heartbeat.html"),
          ("Majority Quorum","https://martinfowler.com/articles/patterns-of-distributed-systems/majority-quorum.html"),("Generation Clock","https://martinfowler.com/articles/patterns-of-distributed-systems/generation-clock.html"),
          ("Lease","https://martinfowler.com/articles/patterns-of-distributed-systems/lease.html"),("Hybrid Clock","https://martinfowler.com/articles/patterns-of-distributed-systems/hybrid-clock.html"),
          ("TigerBeetle: VOPR (source)","https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/internals/vopr.md")]+[(n,"https://en.wikipedia.org/wiki/"+w) for n,w in [
          ("Wikipedia: Fallacies of distributed computing","Fallacies_of_distributed_computing"),("Wikipedia: CAP theorem","CAP_theorem"),("Wikipedia: PACELC design principle","PACELC_design_principle"),
          ("Wikipedia: Linearizability","Linearizability"),("Wikipedia: Eventual consistency","Eventual_consistency"),("Wikipedia: Lamport timestamp","Lamport_timestamp"),
          ("Wikipedia: Vector clock","Vector_clock"),("Wikipedia: Raft","Raft_(algorithm)"),("Wikipedia: Paxos","Paxos_(computer_science)"),("Wikipedia: etcd","Etcd"),
          ("Wikipedia: Quorum (distributed computing)","Quorum_(distributed_computing)"),("Wikipedia: Split-brain","Split-brain_(computing)"),
          ("Wikipedia: Two-phase commit","Two-phase_commit_protocol"),("Wikipedia: Byzantine fault","Byzantine_fault"),("Wikipedia: Chaos engineering","Chaos_engineering")]])
D["cyber"].setdefault("sources",[]).extend([
 ("Cloud Security Alliance (Wikipedia)","https://en.wikipedia.org/wiki/Cloud_Security_Alliance"),
 ("Microsoft Learn: CSA STAR Certification","https://learn.microsoft.com/en-us/compliance/regulatory/offering-csa-star-certification"),
 ("Microsoft Learn: CSA STAR Attestation","https://learn.microsoft.com/en-us/compliance/regulatory/offering-csa-star-attestation"),
 ("Microsoft Learn: CSA STAR self-assessment","https://learn.microsoft.com/en-us/compliance/regulatory/offering-csa-star-self-assessment"),
 ("Google Cloud: CSA STAR","https://cloud.google.com/security/compliance/csa-star"),
 ("AWS: CSA compliance","https://aws.amazon.com/compliance/csa/"),
])

D["agentsec"]=dict(
 F=["Explain direct and indirect prompt injection with an example","Name the three root causes of excessive agency","Treat model output as untrusted input"],
 P=["Give an agent only the tools and permissions its task needs","Add human approval for high-impact actions","Check an MCP server and its scopes before connecting it"],
 S=["Design agent actions to run as the user, with authorisation outside the model","Red-team an agent with injected documents and tool outputs","Sandbox agents that write or run code"],
 E=["Set an organisation's policy for agents, tools and approvals","Map agent risks to OWASP and MITRE ATLAS","Plan detection and response for attacks at machine speed"],
 topics=["Prompt injection","Excessive agency","OWASP Top 10 for LLM Applications","MCP security","Least privilege and complete mediation","AI-orchestrated attacks","MITRE ATLAS"],
 links=[("OWASP Top 10 for LLM Applications (repository)","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns","The 2025 entries, with mitigations"),
        ("MCP security best practices (source)","https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/tutorials/security/security_best_practices.mdx","From the protocol's maintainers"),
        ("MITRE ATLAS","https://atlas.mitre.org/","Adversary techniques against AI systems")],
 sources=[("OWASP LLM01:2025 Prompt Injection","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM01_PromptInjection.md"),("OWASP LLM05:2025 Improper Output Handling","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM05_ImproperOutputHandling.md"),
          ("OWASP LLM06:2025 Excessive Agency","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"),("OWASP LLM10:2025 Unbounded Consumption","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM10_UnboundedConsumption.md"),
          ("OWASP 2025 entries (list)","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns"),
          ("OWASP Agentic Top 10, first public draft","https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/initiatives/agent_security_initiative/agentic-top-10/Sprint%201-first-public-draft-expanded/README.md"),
          ("MCP security best practices (source)","https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/tutorials/security/security_best_practices.mdx"),
          ("MITRE ATLAS data (README)","https://github.com/mitre-atlas/atlas-data/blob/main/README.md"),
          ("Anthropic: Disrupting an AI-orchestrated cyber espionage campaign","https://www.anthropic.com/news/disrupting-AI-espionage"),
          ("Claude Code: Security","https://code.claude.com/docs/en/security"),
          ("Microsoft Learn: Prompt Shields","https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection"),
          ("Wikipedia: Confused deputy problem","https://en.wikipedia.org/wiki/Confused_deputy_problem")])

D["philosophy"].setdefault("sources",[]).extend([
 ("Wikipedia: Impermanence","https://en.wikipedia.org/wiki/Impermanence"),
 ("Wikipedia: Impermanence (Buddhism)","https://en.wikipedia.org/wiki/Impermanence_(Buddhism)"),
 ("Wikipedia: Duḥkha","https://en.wikipedia.org/wiki/Du%E1%B8%A5kha"),
 ("Wikipedia: Panta rhei (doctrine)","https://en.wikipedia.org/wiki/Panta_rhei_(doctrine)"),
 ("Wikipedia: Ecclesiastes","https://en.wikipedia.org/wiki/Ecclesiastes"),
 ("Wikipedia: Mono no aware","https://en.wikipedia.org/wiki/Mono_no_aware"),
 ("Wikipedia: Bhagavad Gita","https://en.wikipedia.org/wiki/Bhagavad_Gita"),
 ("Wikipedia: Hedonic treadmill","https://en.wikipedia.org/wiki/Hedonic_treadmill"),
 ("Wikipedia: The Prophet (book)","https://en.wikipedia.org/wiki/The_Prophet_(book)"),
 ("Wikipedia: Equanimity","https://en.wikipedia.org/wiki/Equanimity"),
 ("Wikipedia: Upekṣā","https://en.wikipedia.org/wiki/Upek%E1%B9%A3%C4%81"),
 ("Wikipedia: Enchiridion of Epictetus","https://en.wikipedia.org/wiki/Enchiridion_of_Epictetus"),
 ("Wikipedia: Serenity Prayer","https://en.wikipedia.org/wiki/Serenity_Prayer"),
 ("Wikipedia: Acceptance and commitment therapy","https://en.wikipedia.org/wiki/Acceptance_and_commitment_therapy"),
 ("Wikipedia: Amor fati","https://en.wikipedia.org/wiki/Amor_fati"),
 ("Wikipedia: Subjective well-being","https://en.wikipedia.org/wiki/Subjective_well-being"),
 ("Wikipedia: Happiness","https://en.wikipedia.org/wiki/Happiness"),
 ("Wikipedia: Sonja Lyubomirsky","https://en.wikipedia.org/wiki/Sonja_Lyubomirsky"),
 ("Wikipedia: Viktor Frankl","https://en.wikipedia.org/wiki/Viktor_Frankl"),
 ("Wikipedia: Toxic positivity","https://en.wikipedia.org/wiki/Toxic_positivity"),
 ("Wikipedia: Man's Search for Meaning","https://en.wikipedia.org/wiki/Man%27s_Search_for_Meaning"),
])

D["apihistory"]=dict(
 F=["Place RPC, CORBA, SOAP, REST, gRPC and GraphQL in order, and say what each changed","Explain why location transparency was criticised","Say what MCP and A2A are for"],
 P=["Choose an API style for a case by its requirements","Wrap a legacy SOAP service behind a gateway","Expose an existing REST API as MCP tools"],
 S=["Explain what an AI or agent gateway adds: token quotas, model routing, guardrails","Plan a move from an older API style without breaking clients","Design gateway policies for agent traffic"],
 E=["Set an organisation's API and agent-protocol strategy","Choose between extending an existing gateway and adding an agent gateway","Govern models, tools and agents in one place"],
 topics=["Remote procedure calls","CORBA and SOAP","REST and OpenAPI","GraphQL and gRPC","MCP and A2A","AI and agent gateways"],
 links=[("A2A protocol","https://github.com/a2aproject/A2A","The specification and SDKs"),
        ("Model Context Protocol (Wikipedia)","https://en.wikipedia.org/wiki/Model_Context_Protocol","History and adoption")],
 sources=[("Wikipedia: Remote procedure call","https://en.wikipedia.org/wiki/Remote_procedure_call"),
          ("Wikipedia: CORBA","https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture"),
          ("Wikipedia: DCOM","https://en.wikipedia.org/wiki/Distributed_Component_Object_Model"),
          ("Wikipedia: XML-RPC","https://en.wikipedia.org/wiki/XML-RPC"),
          ("Wikipedia: SOAP","https://en.wikipedia.org/wiki/SOAP"),
          ("Wikipedia: Service-oriented architecture","https://en.wikipedia.org/wiki/Service-oriented_architecture"),
          ("Wikipedia: Enterprise service bus","https://en.wikipedia.org/wiki/Enterprise_service_bus"),
          ("Wikipedia: REST","https://en.wikipedia.org/wiki/REST"),
          ("Wikipedia: JSON","https://en.wikipedia.org/wiki/JSON"),
          ("Wikipedia: OpenAPI Specification","https://en.wikipedia.org/wiki/OpenAPI_Specification"),
          ("Wikipedia: GraphQL","https://en.wikipedia.org/wiki/GraphQL"),
          ("Wikipedia: gRPC","https://en.wikipedia.org/wiki/GRPC"),
          ("Wikipedia: Model Context Protocol","https://en.wikipedia.org/wiki/Model_Context_Protocol"),
          ("A2A protocol (README)","https://github.com/a2aproject/A2A/blob/main/README.md"),
          ("Wikipedia: Agent2Agent","https://en.wikipedia.org/wiki/Agent2Agent"),("Wikipedia: WSDL","https://en.wikipedia.org/wiki/Web_Services_Description_Language"),("Wikipedia: API management","https://en.wikipedia.org/wiki/API_management"),
          ("Azure API Management: AI gateway","https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities"),
          ("Apigee: MCP overview","https://cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview"),
          ("Amazon Bedrock AgentCore Gateway","https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html"),
          ("agentgateway (README)","https://github.com/agentgateway/agentgateway/blob/main/README.md"),
          ("Agent Router, formerly Envoy AI Gateway (README)","https://github.com/envoyproxy/ai-gateway/blob/main/README.md"),
          ("Docker MCP Gateway (README)","https://github.com/docker/mcp-gateway/blob/main/README.md")])

D["graphdb"]=dict(
 F=["Explain nodes, edges and properties","Tell a labelled property graph from RDF triples","Say why GraphQL is not a graph database"],
 P=["Write MATCH queries for one and two hops","Model a small domain as a graph","Compare a graph query with the same query in SQL"],
 S=["Choose between a graph database, SQL/PGQ and recursive SQL for a case","Explain index-free adjacency and its trade-offs","Design a graph for fraud, permissions or dependencies"],
 E=["Decide whether a graph database earns its place in the estate","Plan a knowledge graph across sources","Set standards: GQL, openCypher or vendor extensions"],
 topics=["Graph theory basics","Property graphs and RDF","Cypher and GQL","Gremlin and SPARQL","Graphs vs relational","Knowledge graphs"],
 links=[("openCypher","https://github.com/opencypher/openCypher","The open Cypher project"),("Apache TinkerPop","https://tinkerpop.apache.org/","Gremlin and the graph computing framework")],
 sources=[("Wikipedia: Graph database","https://en.wikipedia.org/wiki/Graph_database"),
          ("Wikipedia: Graph theory","https://en.wikipedia.org/wiki/Graph_theory"),
          ("Wikipedia: Seven Bridges of Königsberg","https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg"),
          ("Wikipedia: Property graph","https://en.wikipedia.org/wiki/Property_graph"),
          ("Wikipedia: Resource Description Framework","https://en.wikipedia.org/wiki/Resource_Description_Framework"),
          ("Wikipedia: Triplestore","https://en.wikipedia.org/wiki/Triplestore"),
          ("Wikipedia: Cypher","https://en.wikipedia.org/wiki/Cypher_(query_language)"),
          ("Wikipedia: GQL","https://en.wikipedia.org/wiki/Graph_Query_Language"),
          ("Wikipedia: SQL:2023","https://en.wikipedia.org/wiki/SQL:2023"),
          ("Wikipedia: Gremlin","https://en.wikipedia.org/wiki/Gremlin_(query_language)"),
          ("Wikipedia: SPARQL","https://en.wikipedia.org/wiki/SPARQL"),
          ("Wikipedia: Neo4j","https://en.wikipedia.org/wiki/Neo4j"),
          ("Wikipedia: Amazon Neptune","https://en.wikipedia.org/wiki/Amazon_Neptune"),
          ("Wikipedia: JanusGraph","https://en.wikipedia.org/wiki/JanusGraph"),
          ("Wikipedia: Knowledge graph","https://en.wikipedia.org/wiki/Knowledge_graph"),
          ("Microsoft GraphRAG (README)","https://github.com/microsoft/graphrag/blob/main/README.md")])

D["neural"]=dict(
 F=["Explain a neuron: weights, bias, activation","Draw a network's input, hidden and output layers","Say what non-linear activations make possible"],
 P=["Compute a neuron's output by hand and in code","Explain loss, gradient descent and the learning rate","Recognise overfitting and hold back data to check for it"],
 S=["Explain backpropagation as the chain rule","Choose between feedforward, convolutional, recurrent and transformer networks","Decide between training, fine-tuning and using a pre-trained model"],
 E=["Set an organisation's approach to building versus buying models","Judge claims about model capability against how training works","Plan evaluation for models in production"],
 topics=["Artificial neurons","Layers and activation functions","Loss and gradient descent","Backpropagation","CNNs, RNNs and transformers","History of neural networks"],
 links=[("Neural network (Wikipedia)","https://en.wikipedia.org/wiki/Neural_network_(machine_learning)","Overview with a history section")],
 sources=[("Wikipedia: Neural network (machine learning)","https://en.wikipedia.org/wiki/Neural_network_(machine_learning)"),
          ("Wikipedia: Artificial neuron","https://en.wikipedia.org/wiki/Artificial_neuron"),
          ("Wikipedia: Perceptron","https://en.wikipedia.org/wiki/Perceptron"),
          ("Wikipedia: Perceptrons (book)","https://en.wikipedia.org/wiki/Perceptrons_(book)"),
          ("Wikipedia: Multilayer perceptron","https://en.wikipedia.org/wiki/Multilayer_perceptron"),
          ("Wikipedia: Universal approximation theorem","https://en.wikipedia.org/wiki/Universal_approximation_theorem"),
          ("Wikipedia: Activation function","https://en.wikipedia.org/wiki/Activation_function"),
          ("Wikipedia: Softmax function","https://en.wikipedia.org/wiki/Softmax_function"),
          ("Wikipedia: Loss function","https://en.wikipedia.org/wiki/Loss_function"),
          ("Wikipedia: Backpropagation","https://en.wikipedia.org/wiki/Backpropagation"),
          ("Wikipedia: Gradient descent","https://en.wikipedia.org/wiki/Gradient_descent"),
          ("Wikipedia: Stochastic gradient descent","https://en.wikipedia.org/wiki/Stochastic_gradient_descent"),
          ("Wikipedia: Overfitting","https://en.wikipedia.org/wiki/Overfitting"),
          ("Wikipedia: Convolutional neural network","https://en.wikipedia.org/wiki/Convolutional_neural_network"),
          ("Wikipedia: Recurrent neural network","https://en.wikipedia.org/wiki/Recurrent_neural_network"),
          ("Wikipedia: Long short-term memory","https://en.wikipedia.org/wiki/Long_short-term_memory"),
          ("Wikipedia: Attention Is All You Need","https://en.wikipedia.org/wiki/Attention_Is_All_You_Need"),
          ("Wikipedia: AlexNet","https://en.wikipedia.org/wiki/AlexNet")])

D["dsa"]=dict(
 F=["Read and compare O(1), O(log n), O(n), O(n log n) and O(n^2)","Explain arrays, lists, hash tables, stacks and queues","Write a binary search"],
 P=["Pick a structure for the most frequent operation","Spot an accidental O(n^2) loop and fix it","Use heaps, sets and sorted collections from the standard library"],
 S=["Explain B-tree indexes, tries and Bloom filters, and where systems use them","Choose graph algorithms: BFS, DFS, Dijkstra","Solve problems with dynamic programming"],
 E=["Design data layouts for scale and hardware (cache, disk)","Review designs for algorithmic risk","Teach and interview for these skills fairly"],
 topics=["Big O notation","Arrays, lists and hash tables","Trees, heaps and tries","Searching and sorting","Graph algorithms","Dynamic programming"],
 links=[("Python: bisect","https://docs.python.org/3/library/bisect.html","Binary search in the standard library"),("Python: heapq","https://docs.python.org/3/library/heapq.html","A heap in the standard library")],
 sources=[("Wikipedia: Big O notation","https://en.wikipedia.org/wiki/Big_O_notation"),
          ("Wikipedia: Time complexity","https://en.wikipedia.org/wiki/Time_complexity"),
          ("Wikipedia: Array","https://en.wikipedia.org/wiki/Array_(data_structure)"),
          ("Wikipedia: Dynamic array","https://en.wikipedia.org/wiki/Dynamic_array"),
          ("Wikipedia: Linked list","https://en.wikipedia.org/wiki/Linked_list"),
          ("Wikipedia: Stack","https://en.wikipedia.org/wiki/Stack_(abstract_data_type)"),
          ("Wikipedia: Queue","https://en.wikipedia.org/wiki/Queue_(abstract_data_type)"),
          ("Wikipedia: Hash table","https://en.wikipedia.org/wiki/Hash_table"),
          ("Wikipedia: Self-balancing binary search tree","https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree"),
          ("Wikipedia: B-tree","https://en.wikipedia.org/wiki/B-tree"),
          ("Wikipedia: Heap","https://en.wikipedia.org/wiki/Heap_(data_structure)"),
          ("Wikipedia: Trie","https://en.wikipedia.org/wiki/Trie"),
          ("Wikipedia: Bloom filter","https://en.wikipedia.org/wiki/Bloom_filter"),
          ("Wikipedia: Binary search","https://en.wikipedia.org/wiki/Binary_search"),
          ("Wikipedia: Merge sort","https://en.wikipedia.org/wiki/Merge_sort"),
          ("Wikipedia: Quicksort","https://en.wikipedia.org/wiki/Quicksort"),
          ("Wikipedia: Timsort","https://en.wikipedia.org/wiki/Timsort"),
          ("Wikipedia: Breadth-first search","https://en.wikipedia.org/wiki/Breadth-first_search"),
          ("Wikipedia: Depth-first search","https://en.wikipedia.org/wiki/Depth-first_search"),
          ("Wikipedia: Dijkstra's algorithm","https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"),
          ("Wikipedia: Dynamic programming","https://en.wikipedia.org/wiki/Dynamic_programming"),
          ("Python docs: bisect","https://docs.python.org/3/library/bisect.html")])

D["teststrat"]=dict(
 F=["Say which tests run locally and which need a real environment","Explain a contract test","Run a dependency in a container for a test"],
 P=["Write consumer contract tests and verify them in the provider's CI","Use an emulator and know its listed limitations","Add smoke tests to a deployment"],
 S=["Design a per-pull-request cloud environment","Plan canary releases with automatic evaluation","Decide test depth per component by risk"],
 E=["Set an organisation's test strategy across teams and environments","Balance test-environment cost against risk","Make production observability part of quality"],
 topics=["The test pyramid","Contract and consumer-driven contract tests","Testcontainers and emulators","Short-lived environments","Canarying and QA in production"],
 links=[("The Practical Test Pyramid","https://martinfowler.com/articles/practical-test-pyramid.html","Ham Vocke's walkthrough with contract tests"),("Canarying releases","https://sre.google/workbook/canarying-releases/","Google's SRE Workbook chapter")],
 sources=[("Ham Vocke: The Practical Test Pyramid","https://martinfowler.com/articles/practical-test-pyramid.html"),
          ("Martin Fowler: Contract Test","https://martinfowler.com/bliki/ContractTest.html"),
          ("Ian Robinson: Consumer-Driven Contracts","https://martinfowler.com/articles/consumerDrivenContracts.html"),
          ("Toby Clemson: Testing Strategies in a Microservice Architecture","https://martinfowler.com/articles/microservice-testing/"),
          ("Rouan Wilsenach: QA in Production","https://martinfowler.com/articles/qa-in-production.html"),
          ("Google SRE Workbook: Canarying releases","https://sre.google/workbook/canarying-releases/"),
          ("Testcontainers for Java (docs)","https://github.com/testcontainers/testcontainers-java/blob/main/docs/index.md"),
          ("kind (README)","https://github.com/kubernetes-sigs/kind/blob/main/README.md"),
          ("Kubernetes: Namespaces","https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/"),
          ("Google Cloud: Pub/Sub emulator","https://cloud.google.com/pubsub/docs/emulator"),
          ("Google Cloud: Firestore emulator","https://cloud.google.com/firestore/docs/emulator"),
          ("Microsoft Learn: Azurite","https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite"),
          ("LocalStack (README)","https://github.com/localstack/localstack/blob/main/README.md")])

D["apihistory"]["sources"].extend([
 ("Protocol Buffers: Overview (source)","https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/overview.md"),
 ("Protocol Buffers: proto3 language guide (source)","https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/programming-guides/proto3.md"),
 ("Protocol Buffers: Encoding (source)","https://github.com/protocolbuffers/protocolbuffers.github.io/blob/main/content/programming-guides/encoding.md"),
 ("Wikipedia: Protocol Buffers","https://en.wikipedia.org/wiki/Protocol_Buffers"),
])

D["fetoolchain"]=dict(
 F=["Say what TypeScript, JSX, a transpiler and a bundler each do","Run a TypeScript file and a plain ES module","Read a package.json and its build scripts"],
 P=["Set up TypeScript type-checking in CI","Decide whether an app needs a state library","Upgrade a toolchain dependency safely"],
 S=["Choose which layers a project needs, by requirement","Remove a layer that no longer earns its place","Plan a web and React Native codebase"],
 E=["Set an organisation's front-end platform and upgrade policy","Weigh frameworks against a smaller custom stack","Keep build complexity in check across teams"],
 topics=["TypeScript and JSX","Transpilers: Babel, esbuild, tsc","Bundlers: webpack, esbuild, Vite","React and React Native","State management: Redux, reducer and context","Native ES modules and import maps"],
 links=[("Redux: When should I use Redux?","https://redux.js.org/faq/general#when-should-i-use-redux","From Redux's own FAQ"),("MDN: JavaScript modules","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules","Modules in the browser, no bundler")],
 sources=[("Wikipedia: TypeScript","https://en.wikipedia.org/wiki/TypeScript"),
          ("Wikipedia: Babel","https://en.wikipedia.org/wiki/Babel_(transcompiler)"),
          ("Wikipedia: JSX","https://en.wikipedia.org/wiki/JSX_(programming)"),
          ("Wikipedia: Module bundler","https://en.wikipedia.org/wiki/Module_bundler"),
          ("Wikipedia: Webpack","https://en.wikipedia.org/wiki/Webpack"),
          ("Wikipedia: esbuild","https://en.wikipedia.org/wiki/Esbuild"),
          ("Wikipedia: Vite","https://en.wikipedia.org/wiki/Vite"),
          ("Wikipedia: React","https://en.wikipedia.org/wiki/React_(software)"),
          ("Wikipedia: React Native","https://en.wikipedia.org/wiki/React_Native"),
          ("Wikipedia: Redux","https://en.wikipedia.org/wiki/Redux_(software)"),
          ("Redux docs: When should I use Redux?","https://github.com/reduxjs/redux/blob/master/docs/faq/General.md"),
          ("Node.js docs: TypeScript (type stripping)","https://github.com/nodejs/node/blob/main/doc/api/typescript.md"),
          ("TC39 proposal: Type Annotations","https://github.com/tc39/proposal-type-annotations"),
          ("React docs: Scaling up with reducer and context","https://react.dev/learn/scaling-up-with-reducer-and-context"),
          ("MDN: JavaScript modules","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules"),
          ("MDN: Import maps","https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap")])

D["concurrency"]=dict(
 F=["Tell concurrency from parallelism","Explain a race condition with an example","Use a lock around shared state"],
 P=["Spot and fix a lost update","Explain the four conditions for deadlock and avoid one","Choose threads, async or processes for a task"],
 S=["Choose a concurrency model by requirement","Use optimistic concurrency in a database","Estimate parallel speed-up with Amdahl's law"],
 E=["Set concurrency standards for a platform","Review designs for shared mutable state","Diagnose timing bugs in production"],
 topics=["Concurrency and parallelism","Race conditions and deadlock","Locks, semaphores and atomics","Memory models","Threads, async, CSP and actors","Amdahl's law"],
 links=[("Python: threading","https://docs.python.org/3/library/threading.html","Threads, locks and barriers in the standard library")],
 sources=[("Wikipedia: Concurrent computing","https://en.wikipedia.org/wiki/Concurrent_computing"),
          ("Wikipedia: Race condition","https://en.wikipedia.org/wiki/Race_condition"),
          ("Wikipedia: Deadlock","https://en.wikipedia.org/wiki/Deadlock_(computer_science)"),
          ("Wikipedia: Mutual exclusion","https://en.wikipedia.org/wiki/Mutual_exclusion"),
          ("Wikipedia: Semaphore","https://en.wikipedia.org/wiki/Semaphore_(programming)"),
          ("Wikipedia: Compare-and-swap","https://en.wikipedia.org/wiki/Compare-and-swap"),
          ("Wikipedia: Optimistic concurrency control","https://en.wikipedia.org/wiki/Optimistic_concurrency_control"),
          ("Wikipedia: Java memory model","https://en.wikipedia.org/wiki/Java_memory_model"),
          ("Wikipedia: Green thread","https://en.wikipedia.org/wiki/Green_thread"),
          ("Wikipedia: Async/await","https://en.wikipedia.org/wiki/Async/await"),
          ("Wikipedia: Event loop","https://en.wikipedia.org/wiki/Event_loop"),
          ("Wikipedia: Communicating sequential processes","https://en.wikipedia.org/wiki/Communicating_sequential_processes"),
          ("Wikipedia: Actor model","https://en.wikipedia.org/wiki/Actor_model"),
          ("Wikipedia: Global interpreter lock","https://en.wikipedia.org/wiki/Global_interpreter_lock"),
          ("Wikipedia: Amdahl's law","https://en.wikipedia.org/wiki/Amdahl%27s_law"),
          ("Python docs: threading","https://docs.python.org/3/library/threading.html")])

D["datastore"]=dict(
 F=["Name the main families of data store","Say what ACID transactions guarantee","Tell row storage (OLTP) from column storage (OLAP)"],
 P=["Choose between a table, a JSON column and a document store","Add a search index or cache fed from the main store","Explain why a store suits a workload"],
 S=["Choose stores for a system by requirement","Keep several stores consistent (outbox, change data capture)","Weigh the cost of each extra store"],
 E=["Set an organisation's approved data stores and when to add one","Plan migrations between stores","Balance fit against operational risk"],
 topics=["Relational databases and ACID","Document, key-value and wide-column stores","Search engines and vector indexes","Time series and columnar warehouses","Object storage","Polyglot persistence"],
 links=[("Polyglot Persistence","https://martinfowler.com/bliki/PolyglotPersistence.html","Martin Fowler, 2011")],
 sources=[("Wikipedia: Relational database","https://en.wikipedia.org/wiki/Relational_database"),
          ("Wikipedia: ACID","https://en.wikipedia.org/wiki/ACID"),
          ("Wikipedia: NoSQL","https://en.wikipedia.org/wiki/NoSQL"),
          ("Wikipedia: Document-oriented database","https://en.wikipedia.org/wiki/Document-oriented_database"),
          ("Wikipedia: Key–value database","https://en.wikipedia.org/wiki/Key%E2%80%93value_database"),
          ("Wikipedia: Wide-column store","https://en.wikipedia.org/wiki/Wide-column_store"),
          ("Wikipedia: Time series database","https://en.wikipedia.org/wiki/Time_series_database"),
          ("Wikipedia: Vector database","https://en.wikipedia.org/wiki/Vector_database"),
          ("Wikipedia: Data orientation (row vs column)","https://en.wikipedia.org/wiki/Data_orientation"),
          ("Wikipedia: Object storage","https://en.wikipedia.org/wiki/Object_storage"),
          ("Wikipedia: In-memory database","https://en.wikipedia.org/wiki/In-memory_database"),
          ("Wikipedia: Multi-model database","https://en.wikipedia.org/wiki/Multi-model_database"),
          ("Wikipedia: PostgreSQL","https://en.wikipedia.org/wiki/PostgreSQL"),
          ("Wikipedia: MongoDB","https://en.wikipedia.org/wiki/MongoDB"),
          ("Wikipedia: Redis","https://en.wikipedia.org/wiki/Redis"),
          ("Wikipedia: Apache Cassandra","https://en.wikipedia.org/wiki/Apache_Cassandra"),
          ("Wikipedia: Elasticsearch","https://en.wikipedia.org/wiki/Elasticsearch"),
          ("Martin Fowler: Polyglot Persistence","https://martinfowler.com/bliki/PolyglotPersistence.html")])

D["datastore"]["sources"].append(("Wikipedia: Data warehouse","https://en.wikipedia.org/wiki/Data_warehouse"))
D["review"]=dict(
 F=["Write a commit message with a short summary line and a reason","Describe a pull request so a reviewer knows what and why","Read review comments as being about the code, not you"],
 P=["Review others' changes within a day, labelling comments by importance","Keep changes small enough to review well","Write an architecture decision record"],
 S=["Write a design proposal others can build from","Set a team's review and writing conventions","Place documentation in the right one of four kinds"],
 E=["Shape how an organisation records decisions","Balance review effort against automated checks","Mentor others through review"],
 topics=["Bottom line up front and plain language","Commit messages and Conventional Commits","Pull request descriptions","Design proposals and ADRs","Diátaxis: four kinds of documentation","Code review: purpose, standard, size, speed and comments"],
 links=[("Google Engineering Practices: code review","https://google.github.io/eng-practices/review/","Google's published guide"),
        ("Diátaxis","https://diataxis.fr/","Daniele Procida")],
 sources=[("Google eng-practices: The Standard of Code Review","https://github.com/google/eng-practices/blob/master/review/reviewer/standard.md"),
          ("Google eng-practices: Speed of Code Reviews","https://github.com/google/eng-practices/blob/master/review/reviewer/speed.md"),
          ("Google eng-practices: How to write code review comments","https://github.com/google/eng-practices/blob/master/review/reviewer/comments.md"),
          ("Google eng-practices: Small CLs","https://github.com/google/eng-practices/blob/master/review/developer/small-cls.md"),
          ("Google eng-practices: Writing good CL descriptions","https://github.com/google/eng-practices/blob/master/review/developer/cl-descriptions.md"),
          ("Git documentation: git-commit, Discussion","https://git-scm.com/docs/git-commit#_discussion"),
          ("Conventional Commits specification","https://www.conventionalcommits.org/en/v1.0.0/"),
          ("PEP 1: PEP Purpose and Guidelines","https://peps.python.org/pep-0001/"),
          ("Architecture decision record (Joel Parker Henderson)","https://github.com/joelparkerhenderson/architecture-decision-record"),
          ("Diátaxis source (Daniele Procida)","https://github.com/evildmp/diataxis-documentation-framework"),
          ("Wikipedia: Code review","https://en.wikipedia.org/wiki/Code_review"),
          ("Wikipedia: Fagan inspection","https://en.wikipedia.org/wiki/Fagan_inspection"),
          ("Wikipedia: BLUF (communication)","https://en.wikipedia.org/wiki/BLUF_(communication)"),
          ("Wikipedia: Plain language","https://en.wikipedia.org/wiki/Plain_language")])
D["cloudcost"]=dict(
 F=["Read a cloud bill and name its biggest lines","Tag or label what you create","Switch off what you are not using"],
 P=["Right-size and autoscale a service","Set budgets and alerts, knowing alerts-only budgets do not cap spend","Pick a storage class by how often data is read"],
 S=["Decide on commitments from measured base load","Use spot capacity for interruptible work","Design data placement to limit transfer costs"],
 E=["Build a FinOps practice across engineering and finance","Measure cost per unit of business output","Weigh cost against reliability and security"],
 topics=["FinOps","On demand, commitments and spot capacity","Storage classes and minimum durations","Data transfer charges","Tags, labels and budgets","FOCUS cost data"],
 links=[("Google Cloud Well-Architected: cost optimization","https://cloud.google.com/architecture/framework/cost-optimization","Google's principles"),
        ("Azure Well-Architected: cost optimization principles","https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles","Usage and rate optimization")],
 sources=[("Google Cloud: What is FinOps?","https://cloud.google.com/learn/what-is-finops"),
          ("Google Cloud Well-Architected Framework: cost optimization","https://cloud.google.com/architecture/framework/cost-optimization"),
          ("AWS Well-Architected cost optimization pillar: design principles","https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/design-principles.html"),
          ("Azure Well-Architected: cost optimization design principles","https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles"),
          ("Google Cloud: committed use discounts","https://cloud.google.com/docs/cuds"),
          ("AWS: What are Savings Plans?","https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html"),
          ("Azure: save costs with reservations","https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations"),
          ("Google Cloud: Spot VMs","https://cloud.google.com/compute/docs/instances/spot"),
          ("AWS: Spot Instance interruption notices","https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html"),
          ("Azure: Spot Virtual Machines","https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms"),
          ("Google Cloud Storage: storage classes","https://cloud.google.com/storage/docs/storage-classes"),
          ("Google Cloud: network pricing","https://cloud.google.com/vpc/network-pricing"),
          ("AWS: cost allocation tags","https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"),
          ("Google Cloud: labels overview","https://cloud.google.com/resource-manager/docs/labels-overview"),
          ("Google Cloud: create budgets","https://cloud.google.com/billing/docs/how-to/budgets"),
          ("FOCUS specification","https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec")])
D["faded"]=dict(
 F=["Say what convention over configuration means","Name what each of Rails, Grails and Flex introduced","Check whether a framework is still releasing"],
 P=["Read a framework's maintenance policy before upgrading","Upgrade a framework one major version at a time","Recognise a dependency on a runtime one vendor controls"],
 S=["Decide whether to keep, upgrade or replace an older application","Plan a gradual migration behind the same interface","Weigh staffing risk against rewrite risk"],
 E=["Set an organisation's policy for ageing stacks","Spot single-vendor runtime risk early","Carry good ideas from older frameworks into new ones"],
 topics=["Ruby on Rails and convention over configuration","Grails, Groovy and the JVM","Adobe Flex, MXML and the Flash runtime","Flash end of life","Why technologies fade","Keep, upgrade or replace"],
 links=[("Ruby on Rails repository","https://github.com/rails/rails","Releases and tags"),
        ("Apache Grails repository","https://github.com/apache/grails-core","Releases and tags")],
 sources=[("Wikipedia: Ruby on Rails","https://en.wikipedia.org/wiki/Ruby_on_Rails"),
          ("Wikipedia: Convention over configuration","https://en.wikipedia.org/wiki/Convention_over_configuration"),
          ("Wikipedia: Grails (framework)","https://en.wikipedia.org/wiki/Grails_(framework)"),
          ("Wikipedia: Apache Flex","https://en.wikipedia.org/wiki/Apache_Flex"),
          ("Wikipedia: Adobe Flash","https://en.wikipedia.org/wiki/Adobe_Flash"),
          ("rails/rails tags on GitHub","https://github.com/rails/rails/tags"),
          ("apache/grails-core on GitHub","https://github.com/apache/grails-core")])
D["casestudies"]=dict(
 F=["Retell one company's engineering change and what caused it","Say what a single point of failure is, with an example","Find a company's own account of a change"],
 P=["Explain why Netflix tests failure in production","Explain how GitHub drew boundaries inside one application","Separate what a case study shows from what it suggests"],
 S=["Judge whether a company's approach fits your organisation's size and needs","Plan a change that keeps one thing stable","Spot survivorship bias in success stories"],
 E=["Use case studies to argue for or against an architecture change","Write your own organisation's case study honestly","Learn from failures as well as successes"],
 topics=["Yahoo: a directory, then search, then Hadoop","eBay: partitioning by function and by key, no distributed transactions","Facebook: HipHop, HHVM and Hack","Amazon: service-oriented architecture to AWS","Netflix: the 2008 outage and the move to AWS","Chaos engineering and the Simian Army","GitHub: a Rails monolith at scale","Schema domains and database partitioning","Weekly framework upgrades","Shopify: sharding and Packwerk","Stack Overflow: Dapper, and a change in demand"],
 links=[("GitHub Engineering blog","https://github.blog/engineering/","GitHub's own engineering posts"),
        ("Netflix Chaos Monkey","https://github.com/Netflix/chaosmonkey","Netflix's repository")],
 sources=[("Wikipedia: Yahoo","https://en.wikipedia.org/wiki/Yahoo"),
          ("Wikipedia: Apache Hadoop","https://en.wikipedia.org/wiki/Apache_Hadoop"),
          ("Wikipedia: eBay","https://en.wikipedia.org/wiki/EBay"),
          ("Randy Shoup, Scalability Best Practices: Lessons from eBay (InfoQ, 2008)","https://www.infoq.com/articles/ebay-scalability-best-practices/"),
          ("InfoQ interview with Randy Shoup (2008)","https://www.infoq.com/news/2008/06/interview-shoup-ebay/"),
          ("InfoQ: Managing Complex Dependencies with Distributed Architecture at eBay (2022)","https://www.infoq.com/news/2022/04/distributed-arch-ebay/"),
          ("Wikipedia: Facebook","https://en.wikipedia.org/wiki/Facebook"),
          ("Wikipedia: HipHop for PHP","https://en.wikipedia.org/wiki/HipHop_for_PHP"),
          ("Wikipedia: HHVM","https://en.wikipedia.org/wiki/HHVM"),
          ("Wikipedia: Hack","https://en.wikipedia.org/wiki/Hack_(programming_language)"),
          ("Engineering at Meta: Hack, a new programming language for HHVM (2014)","https://engineering.fb.com/2014/03/20/developer-tools/hack-a-new-programming-language-for-hhvm/"),
          ("Wikipedia: Apache Cassandra","https://en.wikipedia.org/wiki/Apache_Cassandra"),
          ("Wikipedia: React","https://en.wikipedia.org/wiki/React_(software)"),
          ("Wikipedia: Amazon Web Services","https://en.wikipedia.org/wiki/Amazon_Web_Services"),
          ("Wikipedia: Netflix","https://en.wikipedia.org/wiki/Netflix"),
          ("Wikipedia: Chaos engineering","https://en.wikipedia.org/wiki/Chaos_engineering"),
          ("Netflix/chaosmonkey README","https://github.com/Netflix/chaosmonkey"),
          ("Netflix/Hystrix README","https://github.com/Netflix/Hystrix"),
          ("GitHub blog: Upgrading GitHub from Rails 3.2 to 5.2","https://github.blog/2018-09-28-upgrading-github-from-rails-3-2-to-5-2/"),
          ("GitHub blog: Partitioning GitHub's relational databases to handle scale","https://github.blog/2021-09-27-partitioning-githubs-relational-databases-scale/"),
          ("GitHub blog: Building GitHub with Ruby and Rails","https://github.blog/2023-04-06-building-github-with-ruby-and-rails/"),
          ("Wikipedia: Shopify","https://en.wikipedia.org/wiki/Shopify"),
          ("Shopify/packwerk README","https://github.com/Shopify/packwerk"),
          ("Wikipedia: Stack Overflow","https://en.wikipedia.org/wiki/Stack_Overflow"),
          ("Wikipedia: Dapper ORM","https://en.wikipedia.org/wiki/Dapper_ORM"),
          ("Dapper README","https://github.com/DapperLib/Dapper")])
D["body"].setdefault("sources",[]).extend([('Microsoft WorkLab: Research Proves Your Brain Needs Breaks (2021)', 'https://www.microsoft.com/en-us/worklab/work-trend-index/brain-research'), ('Wikipedia: Task switching', 'https://en.wikipedia.org/wiki/Task_switching_(psychology)'), ('Wikipedia: Zoom fatigue', 'https://en.wikipedia.org/wiki/Zoom_fatigue'), ('Wikipedia: Flow (psychology)', 'https://en.wikipedia.org/wiki/Flow_(psychology)'), ('Wikipedia: Ego depletion', 'https://en.wikipedia.org/wiki/Ego_depletion')])
D["cyber"].setdefault("sources",[]).extend([('Wikipedia: Morris worm', 'https://en.wikipedia.org/wiki/Morris_worm'), ('Wikipedia: ILOVEYOU', 'https://en.wikipedia.org/wiki/ILOVEYOU'), ('Wikipedia: SQL Slammer', 'https://en.wikipedia.org/wiki/SQL_Slammer'), ('Wikipedia: Stuxnet', 'https://en.wikipedia.org/wiki/Stuxnet'), ('Wikipedia: Heartbleed', 'https://en.wikipedia.org/wiki/Heartbleed'), ('Wikipedia: WannaCry', 'https://en.wikipedia.org/wiki/WannaCry_ransomware_attack'), ('Wikipedia: Equifax', 'https://en.wikipedia.org/wiki/2017_Equifax_data_breach'), ('Wikipedia: SolarWinds', 'https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach'), ('Wikipedia: Colonial Pipeline', 'https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack'), ('Wikipedia: Log4Shell', 'https://en.wikipedia.org/wiki/Log4Shell'), ('Wikipedia: XZ Utils backdoor', 'https://en.wikipedia.org/wiki/XZ_Utils_backdoor'), ('Wikipedia: Multi-factor authentication', 'https://en.wikipedia.org/wiki/Multi-factor_authentication'), ('Wikipedia: Phishing', 'https://en.wikipedia.org/wiki/Phishing'), ('Wikipedia: Ransomware', 'https://en.wikipedia.org/wiki/Ransomware')])
D["sysdesign"].setdefault("sources",[]).extend([('Wikipedia: Load balancing (computing)', 'https://en.wikipedia.org/wiki/Load_balancing_(computing)'), ('Wikipedia: Service discovery', 'https://en.wikipedia.org/wiki/Service_discovery'), ('Wikipedia: Scalability (horizontal and vertical scaling)', 'https://en.wikipedia.org/wiki/Scalability'), ('Wikipedia: Consistent hashing', 'https://en.wikipedia.org/wiki/Consistent_hashing')])
D["docker"].setdefault("sources",[]).extend([('Docker docs: Dockerfile reference, how ARG and FROM interact', 'https://docs.docker.com/reference/dockerfile/'), ('Docker docs: Building best practices (pin base images, Dependabot, rebuild often)', 'https://docs.docker.com/build/building/best-practices/'), ('Spring Boot docs: Dockerfiles (layered extraction)', 'https://docs.spring.io/spring-boot/reference/packaging/container-images/dockerfiles.html'), ('Spring Boot Maven plugin: Packaging OCI images', 'https://docs.spring.io/spring-boot/maven-plugin/build-image.html'), ('Quarkus docs: Container images (source on GitHub)', 'https://github.com/quarkusio/quarkus/blob/main/docs/src/main/asciidoc/container-image.adoc'), ('Google Cloud: Configure Flex Templates (custom container images)', 'https://cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates'), ('Google Cloud: Build custom container images for Dataflow', 'https://cloud.google.com/dataflow/docs/guides/build-container-image'), ('Maven: Introduction to the POM, project inheritance (source on GitHub)', 'https://github.com/apache/maven-site/blob/master/content/markdown/guides/introduction/introduction-to-the-pom.md')])
D["distsys"].setdefault("sources",[]).extend([('Wikipedia: Consistency model (session guarantees)', 'https://en.wikipedia.org/wiki/Consistency_model'), ('Wikipedia: Conflict-free replicated data type', 'https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type'), ('Wikipedia: Fencing (computing)', 'https://en.wikipedia.org/wiki/Fencing_(computing)')])
D["sysdesign"].setdefault("sources",[]).extend([('Wikipedia: Apache Hadoop (data locality)', 'https://en.wikipedia.org/wiki/Apache_Hadoop'), ('Origins: CAP theorem', 'https://en.wikipedia.org/wiki/CAP_theorem'), ('Origins: PACELC', 'https://en.wikipedia.org/wiki/PACELC_design_principle'), ('Origins: Linearizability', 'https://en.wikipedia.org/wiki/Linearizability'), ('Origins: Logical clocks and event ordering', 'https://en.wikipedia.org/wiki/Lamport_timestamp'), ('Origins: Paxos consensus', 'https://en.wikipedia.org/wiki/Paxos_(computer_science)'), ('Origins: Raft consensus', 'https://raft.github.io/raft.pdf'), ('Origins: Leader election (the bully algorithm)', 'https://en.wikipedia.org/wiki/Bully_algorithm'), ('Origins: Sagas', 'https://en.wikipedia.org/wiki/Long-running_transaction'), ('Origins: Session guarantees', 'https://www.cs.cornell.edu/courses/cs734/2000FA/cached%20papers/SessionGuaranteesPDIS_1.html'), ('Origins: Consistent hashing', 'https://en.wikipedia.org/wiki/Consistent_hashing'), ('Origins: Dynamo: eventual consistency at scale', 'https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf'), ('Origins: CRDTs', 'https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type'), ('Origins: Circuit breaker', 'https://martinfowler.com/bliki/CircuitBreaker.html'), ('Origins: Microservices (the definition most cited)', 'https://martinfowler.com/articles/microservices.html'), ('Origins: Monolith first', 'https://martinfowler.com/bliki/MonolithFirst.html')])
D["caching"].setdefault("sources",[]).extend([('Wikipedia: Cache (computing), write policies', 'https://en.wikipedia.org/wiki/Cache_(computing)')])
D["linux"].setdefault("sources",[]).extend([('Wikipedia: Unix', 'https://en.wikipedia.org/wiki/Unix'), ('Wikipedia: History of Unix', 'https://en.wikipedia.org/wiki/History_of_Unix'), ('Wikipedia: Berkeley Software Distribution', 'https://en.wikipedia.org/wiki/Berkeley_Software_Distribution'), ('Wikipedia: GNU Project', 'https://en.wikipedia.org/wiki/GNU_Project'), ('Wikipedia: POSIX', 'https://en.wikipedia.org/wiki/POSIX'), ('Wikipedia: Linux', 'https://en.wikipedia.org/wiki/Linux'), ('Wikipedia: Oracle Solaris', 'https://en.wikipedia.org/wiki/Oracle_Solaris'), ('Wikipedia: OpenSolaris', 'https://en.wikipedia.org/wiki/OpenSolaris'), ('Wikipedia: illumos', 'https://en.wikipedia.org/wiki/Illumos'), ('Wikipedia: Single UNIX Specification', 'https://en.wikipedia.org/wiki/Single_UNIX_Specification')])
