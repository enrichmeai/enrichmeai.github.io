# Well Rounded Engineer: claims still to confirm at source

From the full fact check of November 2026. Each page lists what it was checked against; the claims below could not be
confirmed at an official source from the checking environment (the site was blocked, a book was not reachable, or a
command could not be run). Pages that have entries here show "A few claims could not be confirmed at their official
source from here and are being re-checked." Remove an entry once it is confirmed or the page is corrected.

## agentharness

- Penstock claims (headless, CI/Slack/webhooks, Copilot/Anthropic/OpenAI/Ollama, audit log with database storage, Apache 2.0) match Penstock's README on main, not checked at its latest release tag.
- LangGraph docs link (langchain-ai.github.io/langgraph) not checked for a move.
- The rest of the tab is design advice, not factual claims.

## agentsgcp

- gcloud flags were verified with the locally installed gcloud --help (offline), not the web reference pages listed; all flags used exist.
- Cloud Workstations, Workflows, Eventarc, Secret Manager product descriptions not re-fetched.
- Penstock 'can run as a container' not checked at its release tag.

## ai

- 'service accounts with Vertex AI User': the IAM role's display name after the Agent Platform rename was not checked (role ID roles/aiplatform.user likely unchanged).
- SDK snippets (messages.parse with output_format=Model, @beta_tool + client.beta.messages.tool_runner, stop_reason 'refusal') match the bundled Claude API skill reference (cached 2026-11-03) rather than a live SDK fetch; consistent, but not re-fetched from the SDK repo.
- 'some models run only in global or specific regions' not re-checked for current model list.
- Chunk sizes, eval set sizes and the cost-ratio example are advice, not facts; not checked.

## apigee

- Apigee vs API Gateway cost characterisation ('significant' vs 'low, per call') not checked against pricing pages.
- apigeecli, Maven plugin and apigeelint repos not opened.
- Organisation-to-project, environment group and Apigee X/hybrid/Edge descriptions not checked line by line.

## apis

- Idempotency-Key header for POST: an IETF draft (httpapi-idempotency-key-header), not an RFC; not fetched, so the page's wording ('use an Idempotency-Key header') is advice, not checked as a standard.
- 'Integration styles (oldest to newest)': the four styles match Enterprise Integration Patterns, but the chronological ordering was not checked against the book (enterpriseintegrationpatterns.com not reachable here).

## architecture

- Outbox/idempotent-consumer SQL uses $event_id/$account placeholders (pseudocode, not valid Postgres parameter syntax) and the processed_events block runs the UPDATE unconditionally; the comment carries the 'skip if 0 rows' logic. Not wrong as illustration, so no fix proposed.

## bigquery

- SQL snippets were checked against reference syntax by reading, not executed (no BigQuery project available).
- 'DML quotas and costs are per statement': DML statements per day are unlimited; per-table concurrency limits apply. Wording is loose but not clearly false, left as is.

## blueprints

- 'Scorecards (e.g. in a Backstage catalogue)': scorecards come from Backstage plugins rather than core Backstage; backstage.io not fetched.
- Cost model numbers are explicitly illustrative (arithmetic checks: 15 x 3 = 45).
- Explore links (CNCF white paper, Backstage, OpenRewrite, Renovate, semver.org, Team Topologies) not fetched.

## caching

- @Cacheable self-invocation bypass (proxy-based) not re-read from Spring Framework docs (docs.spring.io blocked here); it is standard Spring AOP proxy behaviour.
- 'Model API prompt caching: any change in the prefix invalidates it' not checked against a provider's docs.

## claudetools

- Cowork 'from the Claude desktop app': the Cowork overview says it runs within Claude Desktop, but Claude Code's hooks docs also mention 'a Cowork cloud session'; whether Cowork now also runs in the cloud was not confirmed.
- Persona claims (Penstock memory as plain files, works with Claude Code over MCP, persona planned) not checked against the Penstock release tag.
- claude-code-action and Agent SDK surface rows not fetched beyond the overview page.

## cloudcompare

- Most service-mapping rows were checked only by name against provider docs (all GCP rows fetched; AWS/Azure rows not individually fetched beyond those listed). Rows like Azure Synapse, HDInsight, Stream Analytics, Front Door as CDN, X-Ray/Application Signals were not opened.
- Azure city names for Central/South/West India confirmed in the regions list; 'plus newer regions' matches India South Central (Hyderabad).
- CLI equivalents (aws, az) not run locally (no aws/az CLI); gcloud lines confirmed with --help.

## cloudinside

- Most cloud breaches are a setting someone left open: stated as fact, no primary source fetched (widely reported by provider and industry reports, but not checked here).

## cloudrun

- Worker pool availability by region not checked (docs fetched mark parts as Preview).
- Dockerfiles and Python/Java token snippets read, not built or run.

## copilot

- Not wrong, but worth knowing: Copilot now reads CLAUDE.md, AGENTS.md and GEMINI.md as agent instructions where supported, so the 'one source of truth' note could point at that.
- 'Usage metrics for adoption and acceptance rates' and 'Public code filter' policy names were not checked on their own pages.
- Copilot Chat on mobile is documented (GitHub Mobile); the newer 'Copilot in the cloud' experience is paid-plan only from 2026-10-28.

## dags

- astronomer-cosmos import (from cosmos import DbtDag, ProjectConfig, ProfileConfig) was not checked; the Cosmos docs host is not on the allowed list.
- "Deadline alerts" as the SLA replacement: the 3.0.0 notes say they were planned after 3.0; that they shipped in a later 3.x was not confirmed in this pass.

## data

- "This stage model follows Fundamentals of Data Engineering by Reis and Housley": the publisher page (oreilly.com) is not reachable here. From memory the book orders the stages generation, storage, ingestion, transformation, serving, while the table puts Ingestion before Storage; not confirmed, so no fix proposed.
- The page is mostly concepts and advice with few checkable product claims; the GCP service names (Storage Transfer Service, Datastream, Dataflow, Dataproc) were not checked page by page.

## database

- Citus, Vitess, Spanner, CockroachDB described as sharding/distributed options: not checked against their docs.
- "a change that takes 30 s on 10k rows can take hours on 20M": illustrative, no source.

## datalibs

- PySpark and BigQuery DataFrames (bigframes) snippets were not executed (no Spark runtime or BigQuery project here).
- The landscape table's descriptive rows (Ray, Flink, Kafka Streams, Beam runner list, Spring Batch, FastCSV, parquet-java) were not checked against each project's docs.

## dbt

- Generic test arguments are written at the top level (relationships: {to, field}, accepted_values: {values}). The current dbt docs nest them under `arguments:` (available since 1.10.5) and keep the older form for earlier versions. It still works and the page says 1.8+, so no fix proposed; worth a later note.
- CLI commands (dbt show --limit, dbt ls --resource-type, dbt run-operation --args, --defer --state, result:error+) are from the dbt reference as I know it; only retry, microbatch flags and selectors were fetched page by page.

## devops

- DORA metric names 'Failed deployment recovery time (formerly time to restore)' and 'Deployment rework rate': dora.dev is blocked from this environment (DNS refused) and Wikipedia's DORA article still lists MTTR. Secondary sources (web search) agree with the page's wording, but the official source was not read.
- Golden signals (latency, traffic, errors, saturation) and RED/USE: sre.google is not reachable from here; standard terminology, not verified against the SRE book.
- Argo Rollouts / Flagger / Harness blue-green and canary support not checked against their docs (hosts not in the allowed list).

## docker

- "Apple Silicon builds arm64 by default": consistent with Docker's multi-platform docs (builds target the host platform), but no sentence stating it for Apple Silicon was found.
- nicolaka/netshoot image and trivy command: third-party tools, not checked against their docs.

## eventsourcing

- Java aggregate and given/when/then tests were compiled and run with javac 21 locally (replay, upgrade, 'not active' rejection all behave as described) — verified by execution, no URL.
- Kafka as 'a weak event store' (no per-entity stream reads, no per-stream optimistic concurrency) is a reasonable characterisation but was not checked against Kafka docs (kafka.apache.org not in the allowed hosts).

## gcpdata

- 'exactly-once into BigQuery' for Dataflow not opened against Dataflow streaming docs.
- Dataplex/Knowledge Catalog data quality results 'in BigQuery' (export option) not opened.
- Explore-further link labels still say Dataproc/Dataplex; URLs not re-checked for redirects.

## goodhuman

- Project Aristotle found psychological safety 'the most important factor in team effectiveness': Google re:Work was not reachable. Wikipedia (Organizational network analysis, Collective intelligence) only confirms that Project Aristotle exists and studied teams.

## graphql

- Default Spring for GraphQL schema location (src/main/resources/graphql/*.graphqls): the Boot property lives in the Spring Boot reference, which was not fetched.
- 'Usually 200 with an errors array': true for execution errors under application/json; the GraphQL-over-HTTP draft (application/graphql-response+json) uses 4xx for request errors. Draft not fetched, so left as is.

## harness

- VERIFY GATE DID NOT RUN for most of this tab: developer.harness.io is blocked by this environment's proxy, and raw.githubusercontent.com/harness/developer-hub returns 404 (repo not reachable).
- Module list, especially 'Feature Flags': Harness may now market this as Feature Management & Experimentation; not confirmed.
- Pipeline YAML shapes (stage types CI/Approval/Deployment, Run step shell: Sh, HarnessApproval approvers.userGroups/minimumCount, BuildAndPushGAR fields, runtime type Cloud) not checked.
- Expressions (<+pipeline.sequenceId>, <+codebase.commitSha>, <+codebase.shortCommitSha>, <+artifact.tag>, <+env.name>, <+secrets.getValue()>) not checked; <+artifact.tag> may have been superseded by <+artifacts.primary.tag>.
- CI features (Test Intelligence, Cache Intelligence, Background step, Drone/GitHub Actions plugins), CD deployment types and GCP connector OIDC support not checked.
- GitHub Actions to Harness mapping: the GitHub Actions side is correct; the Harness side is unverified.

## homelab

- HashiCorp's "Get started with Docker" Terraform tutorial: developer.hashicorp.com is not reachable from this environment.
- Airflow official Docker Compose quick start and chaos-mesh: not checked (airflow.apache.org and chaos-mesh.org not reachable).
- "new Google Cloud accounts get free-trial credit": not re-read in this pass (the BigQuery sandbox part was checked on the sql tab).
- kube-prometheus-stack Grafana service name monitoring-grafana on port 80 for release name 'monitoring': follows the Grafana subchart's defaults, not checked in the chart values.

## kafka

- confluent-kafka Python API (produce(callback=...), commit(message=..., asynchronous=False)): docs.confluent.io is not on this environment's allowed hosts; not checked.
- Not a fix, a note: from Kafka 4.2 the console producer's --property is deprecated in favour of --reader-property, and the console consumer's in favour of --formatter-property (ConsoleProducer.java / ConsoleConsumerOptions.java on trunk). The page's commands still work.

## kubernetes

- helm install from oci://registry-1.docker.io/bitnamicharts/redis: whether Bitnami still publishes that chart at that path was not checked (the page already says to check the chart's README).

## llm

- `ollama run llama3.1`: ollama.com (the model library) is blocked from this environment; the current Ollama README examples use a newer model, so the llama3.1 tag could not be confirmed as still listed.
- GPU memory figures (8B at 16-bit ~16 GB, 4-bit ~5 GB) are arithmetic, not checked against a source; they are consistent with parameters x bytes plus overhead.
- 'Cloud Run with GPUs' as a self-hosting target was not re-checked this run.
- Explore links to cloud.google.com/vertex-ai/... still resolve, but redirect to gemini-enterprise-agent-platform pages; link text says 'Vertex AI Model Garden'.

## mcp

- MCP connector beta: mcp-client-2025-11-20 is still accepted, but a newer mcp-client-2026-09-15 (adds tool-list pinning) exists; the page already says to check the current beta name, so no fix proposed.
- Whether a spec revision newer than 2025-11-25 exists could not be listed (GitHub API blocked); claims checked against 2025-11-25.
- BigQuery Python client calls in the guarded query tool (referenced_tables, maximum_bytes_billed, result(max_results=...)) were not re-fetched from the client docs.
- Note: MCP authorisation is OPTIONAL in the spec; the transport table's 'authorisation with OAuth' reads as if required, but is not false.

## microservices

- Spring RestClient fluent call chain and @CircuitBreaker/@Retry fallback signature not checked against Spring/Resilience4j docs (docs.spring.io and resilience4j.readme.io blocked from this environment); the property names in the YAML were verified from Resilience4j source.

## oauth

- OIDC specifics (nonce for ID-token replay protection, ID token is a JWT, sub+iss as the stable key): openid.net was unreachable from this environment; Wikipedia confirms only that OIDC is an authentication layer on OAuth 2.0.
- PyJWT snippet was checked by installing PyJWT from PyPI and inspecting the API (PyJWKClient.get_signing_key_from_jwt, jwt.decode audience/issuer/algorithms all exist); not run against a live JWKS.

## observability

- googlecloud and googlemanagedprometheus Collector exporter names: not fetched from the collector-contrib repo.
- gcloud logging metrics create --description/--log-filter: confirmed only against the local gcloud --help, not an online page.

## opstools

- Dynatrace (OneAgent, Smartscape, PurePath, Davis, Grail, DQL syntax `fetch logs, from:now()-1h | ... by:{...}`): docs.dynatrace.com is blocked from this environment.
- ServiceNow Table API (sysparm_query, sysparm_limit, sysparm_fields, POST body fields) and change types: servicenow.com docs blocked.
- Recording rule naming convention (level:metric:operations) page could not be fetched; the rule itself is valid syntax.
- GKE/Cloud Run built-in logging agents and Managed Service for Prometheus not re-fetched.

## payments

- Header names X-Razorpay-Signature and X-Razorpay-Event-Id: razorpay.com is blocked by this environment's network policy; the SDK confirms the HMAC scheme but not the header names.
- RBI rules (card tokenisation, payment data localisation, e-mandate pre-debit notice and limits): rbi.org.in not reachable; not checked. The page already says to check the current rules.
- UPI collect flow 'being phased down': not confirmed from a reachable source (npci.org.in not reachable; Wikipedia does not cover it). The page already hedges.
- Settlement 'usually T+1 or T+2': Wikipedia's Payment gateway article says authorisation to funding 'typically takes 2-3 days'; gateway-specific settlement cycles not checked.
- Stripe amount 50000 with currency inr = ₹500.00 (two-decimal currency): docs.stripe.com not reachable; not checked.

## performance

- Python commands were checked by running them locally (python3 -m cProfile -o out.prof -m loader; the pstats one-liner; -X importtime) and 1 - 0.99^100 = 0.634 computed locally; the importtime fix is sourced from the CPython docs source (Doc/using/cmdline.rst).
- 'Plan for 60-70% utilisation at peak' is a rule of thumb, not a sourced fact; left as is.

## philosophy

- Amazon's 2015 shareholder letter naming one-way and two-way doors: aboutamazon.com and sec.gov were not reachable from this environment, and no Wikipedia page carried the claim.
- Amazon's 'disagree and commit': the Amazon leadership principles page was not reachable.
- Chesterton's fence: the Wikipedia page is a redirect to a G. K. Chesterton section that was not fetched (the principle as stated is standard).

## python

- uv commands (uv venv, uv pip install -e, uv add, uv run) and ruff/mypy invocations: docs.astral.sh not fetched; not checked.
- Version-map years all match the release-schedule PEPs (569, 596, 619, 664, 693, 719, 745, 790); listed here only because 3.15 shipped weeks ago (2026-10-09), so its row should be re-read against the final what's-new page when docs.python.org is reachable.

## quarkus

- Mutiny chain (.onFailure().retry().atMost(3).ifNoItem().after(...).fail()) and Multi transformToUniAndMerge: smallrye.io not fetched; the method names match what I know, but they were not checked against a fetched source.
- 'Native images start in tens of milliseconds': no measured figure fetched; left as is.

## rag

- 'Vertex AI ranking' (reranking API): its name after the Agent Platform rename was not found in the part of the rename table read.
- Citations document block shape (source type text, title, citations.enabled) follows the bundled Claude API skill reference; the citations doc page was not fetched separately.
- RRF k = 60 is the commonly used constant from the original paper; not fetched.
- Postgres websearch_to_tsquery / ts_rank_cd usage not re-fetched from postgresql.org (standard functions). Note: the ROW_NUMBER() window in the vec CTE likely stops the HNSW index being used (exact scan); results are still correct.

## robotics

- ISO 10218 as the industrial robot safety standard: the Wikipedia page returned an error this run and iso.org is not an allowed host (verified earlier this week). The PID snippet was re-run and prints exactly 80.0 / 100.1 / 100.1.

## science

- Keshav's three passes (minutes / about an hour / hours): the paper itself was not fetched; only Wikipedia's Srinivasan Keshav search snippet naming the three-pass method was seen.
- Memory hierarchy 'each step roughly 10-1,000 times slower' and 'a round trip across a continent cannot be faster than tens of milliseconds' were checked by arithmetic only (about 8,000 km round trip at roughly 200,000 km/s in fibre gives about 40 ms), not against a fetched source.

## security

- gcloud secrets commands were checked against local `gcloud ... --help` output (create --data-file, versions destroy VERSION --secret, add-iam-policy-binding --member/--role), not a fetched web page.
- Spring Security snippet (HttpSecurity lambda DSL, oauth2ResourceServer jwt, STATELESS) and the Spring JdbcClient .sql().param() call were not checked against the Spring reference docs (docs.spring.io not on the allowed host list).

## solid

- 'Some governments are piloting or running Solid-based services': not checked against a fetched source (the Wikipedia Solid project page was fetched but this claim was not located in it).

## sql

- "A global sort runs on one worker at the end" (ORDER BY without LIMIT): the current best-practice page says to put ORDER BY in the outermost query and add LIMIT for very large results, but does not say the sort runs on a single worker.
- "If BigQuery complains that QUALIFY needs a WHERE, GROUP BY or HAVING clause, add WHERE TRUE": the current QUALIFY docs no longer state that requirement (only that a window function must appear in QUALIFY or SELECT). The note is conditional, so it was left; it may be dated.
- bigquery-public-data.stackoverflow.posts_questions and bigquery-public-data.new_york_taxi_trips exist: could not check (no BigQuery credentials in this environment).
- "APPROX_COUNT_DISTINCT has a small, documented error and is far cheaper": not re-read in this pass.

## sre

- sre.google is blocked from this environment, so the SRE Workbook could not be read directly. The burn-rate table (14.4/1 h/5 min/2%, 6/6 h/30 min/5%, 1/3 d/6 h/10%) matches Sloth's copy of the Workbook's values and checks out arithmetically against a 30-day window; it was not read in the Workbook itself.
- Toil capped at under 50% of an SRE's time (SRE book, Eliminating Toil): not read at the source.
- Example error budget policy: a postmortem when one incident uses more than 20% of the budget (SRE Workbook): not read at the source.
- Incident roles (commander, operations, communications, scribe): a common pattern (Google's own list has a planning lead; scribe comes from PagerDuty's guide); not checked against either source.

## sysdesign

- Arithmetic checked by hand and correct: 86,400 s/day; 1 M/day ≈ 11.6/s; availability table (99% = 3.65 d / 7.3 h, 99.9% = 8.76 h / 43.8 min, 99.95% = 4.38 h / 21.9 min, 99.99% = 52.6 min / 4.38 min, 99.999% = 5.26 min / 26 s); 0.999^3 ≈ 99.7%; 62^7 ≈ 3.52 trillion; 100 M/yr ≈ 3.2/s; 100 M × 500 B = 50 GB; 20 M × 2 KB = 40 GB, × 7 KB = 140 GB.
- Latency table and per-instance throughput figures are rules of thumb with no single authoritative source; they match commonly cited orders of magnitude but were not verified.

## web3

- India 'taxes crypto transfers': the Wikipedia page Cryptocurrency in India returned a Wikimedia error (rate limit) on every attempt; no government source in the allowed hosts.
- Solidity snippet: compiled cleanly with solcjs 0.8.24 locally (no source URL needed); the SPARQL and JSON-LD snippets were read against the specs, not executed.
