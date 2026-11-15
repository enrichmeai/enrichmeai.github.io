# Well Rounded Engineer: claims still to confirm at source

Two rounds of fact checking (November 2026). Every page lists what it was checked against. The claims below still
could not be confirmed at an official source from the checking environment; their pages say so. Remove an entry once
it is confirmed or the page is corrected.

## ai

- Chunk sizes, eval set sizes and the cost-ratio example are advice, not facts.

## apigee

- Policy XML snippets read against the policy reference, not deployed

## architecture

- The 'skip if 0 rows inserted' branch lives in a comment (the application decides); the UPDATE shown is itself idempotent, so the illustration holds. No source needed.

## bigquery

- SQL snippets read against the reference syntax, not executed (no BigQuery project here)

## blueprints

- Links to tag-app-delivery.cncf.io, docs.openrewrite.org, docs.renovatebot.com and teamtopologies.com: connection fails from here, so not checked for moves.
- Cost model numbers are explicitly illustrative (15 x 3 = 45 checks).

## claudetools

- 'The persona that speaks from it is planned': a planned item, so it is not checkable at a tag; the v0.6.0 README describes memory, not a persona.

## cloudcompare

- The remaining AWS and Azure mapping rows (beyond those listed) are still checked by name only; no row was found wrong
- aws and az CLI lines read against the reference, not run (no aws/az CLI here)

## cloudinside

- No primary breach statistic fetched; softened instead

## cloudrun

- Dockerfiles not built: docker CLI is present but no daemon is running here

## dags

- Whether Deadline Alerts are still experimental in 3.3 or 3.4: those notes do not say either way.

## data

- The exact stage order in Reis and Housley's book (publisher site unreachable); softened to 'adapted from'.

## datalibs

- The bigframes snippet was not executed against BigQuery (no project here); only the API names were checked.

## devops

- RED (rate, errors, duration) and USE (utilisation, saturation, errors) expansions: brendangregg.com and grafana.com are still unreachable from here; Wikipedia confirms Gregg is known for the USE method but not the letters. Standard terminology, left as is.

## eventsourcing

- Absence of per-entity reads and per-stream optimistic concurrency in Kafka: an absence claim, not stated in one sentence anywhere (KIP-27 'Conditional Publish' is on cwiki.apache.org, which this environment refuses).

## harness

- Deploy stage YAML 'type: Deployment': not found in the CD pages fetched (they show infrastructure definitions only); the card already says it shows the structure only and to copy YAML from the editor.
- GitHub Actions to Harness mapping: the Harness side is consistent with the CI docs read (stages, steps, plugins, background steps, looping strategies not individually opened).

## llm

- GPU memory (8B at 16-bit ~16 GB, 4-bit ~5 GB): arithmetic (8e9 x 2 bytes; 8e9 x 0.5 bytes plus overhead), labelled approximate; no source needed.

## mcp

- Whether a spec revision newer than 2025-11-25 exists: modelcontextprotocol.io connection fails and the GitHub API returns 403 from here.

## oauth

- PyJWT snippet not run against a live JWKS (API matches the docs and the installed package).

## opstools

- ServiceNow Table API (sysparm_query, sysparm_limit, sysparm_fields, POST fields) and change types standard/normal/emergency: servicenow.com and developer.servicenow.com still unreachable (connection fails) from here.
- Cloud Run 'built-in logging agent': Cloud Run logging page reachable but not read for an agent claim; GKE side confirmed.

## payments

- UPI collect flow 'being phased down': www.npci.org.in returns 403 Access Denied (Akamai) from this environment; the page already hedges with 'check current NPCI rules', so no change proposed.

## performance

- 'Plan for 60–70% utilisation at peak' is a rule of thumb framed as advice; queueing theory supports the shape but no single source gives the number. Left as is.

## python

- docs.astral.sh itself is refused from here; the uv and ruff commands were confirmed in the docs sources in their GitHub repositories instead.

## quarkus

- quarkus.io guides are refused by this environment's proxy; the native startup figure was replaced rather than confirmed.

## rag

- The HNSW-index note from round 1 (ROW_NUMBER in the vec CTE): not a claim on the page, and pgvector's own example uses the same shape, so no change proposed.

## robotics

- iso.org itself still returns 403 from this environment; confirmed through Wikipedia's ISO 10218 page, which cites the iso.org standard pages

## science

- Keshav's three passes: the paper's official copy (ccr.sigcomm.org, dl.acm.org) is still unreachable from here. A full transcription on GitHub (raw.githubusercontent.com/NicholasSynovic/skills/HEAD/paper-review/references/keshav_how-to-read-a-paper.md) gives first pass five to ten minutes, second pass up to an hour, third pass four or five hours for beginners and about an hour for experienced readers, which matches the page; it is not an official source, so no change proposed.

## sysdesign

- Indexed DB lookup ~1 ms, Redis get ~1 ms, intra-continent 10–50 ms, per-instance throughput rows: rules of thumb with no single authoritative source; worded as rough orders of magnitude, left as is.

## web3

- No Indian government source is reachable (incometaxindia.gov.in is refused by the proxy; the Wikipedia page 'Cryptocurrency in India' gave a Wikimedia error / does not resolve); confirmed through Wikipedia's WazirX page, which is secondary
- SPARQL and JSON-LD snippets read against the specs, not executed
