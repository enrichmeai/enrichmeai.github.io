# Rebuild the nav, the level and Explore cards, and Start here's tables in guide.html.in from the lists
# below and levels_data.py. Safe to run again: it changes nothing when nothing changed. See README.md.
import re, sys, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from levels_data import D
p=os.path.join(HERE, 'guide.html.in'); s=open(p).read()

groups=[("",["start","aiworry"]),
 ("Foundations",["electronics","hardware","linux","networking","internet","web","docker","dsa","sql","database","graphdb","homelab"]),
 ("Languages",["java","kotlin","python","javascript","go","rust","buildtools"]),
 ("Building services",["apis","apihistory","graphql","realtime","kafka","payments","banking","spring","quarkus"]),
 ("User interfaces",["designux","accessibility","apps","uihistory"]),
 ("Quality",["testing","performance"]),
 ("Security",["security","pki","privacy","cyber","agentsec","oauth"]),
 ("Data",["data","datalibs","dbt","dags"]),
 ("Architecture &amp; design",["patterns","architecture","atob","distsys","microservices","eventsourcing","sysdesign","specs","caching"]),
 ("Platform &amp; operations",["devops","kubernetes","k8sdr","helm","operators","servicemesh","terraform","observability","sre"]),
 ("Cloud providers",["cloudinside","cloudcompare","retailcloud","gcpdata","bigquery","cloudrun","apigee","awsdata","azuredata"]),
 ("AI",["neural","llm","ai","rag","mcp","agentharness","humanagents","blueprints"]),
 ("Tools",["claudetools","copilot","agentsgcp","harness","opstools"]),
 ("Thinking &amp; character",["behaviours","ways","mathematics","science","everydayscience","philosophy","goodhuman","body"]),
 ("Frontiers",["quantum","robotics","bitcoin","web3","solid"]),
 ("About this guide",["why","history","reading"]),
 ("EnrichMeAI open source",["opensource","culvert"])]
NARRATIVE=("humanagents","ways","designux","accessibility","everydayscience","reading","uihistory","start","why","aiworry","history","behaviours","homelab","opensource")
# what each group is for, and where its running code lives (only folders that exist and run)
GH="https://github.com/enrichmeai/"
SITE="enrichmeai.github.io"
from urllib.parse import quote
blurb={
 "Foundations":"How computers work from the chip up, networks and the web, and the data underneath. Everything else stands on this.",
 "Languages":"Java and Python learned properly first, then Kotlin, Go and Rust: how each runs, tests and fails.",
 "Building services":"APIs, messaging and the frameworks that turn code into services.",
 "User interfaces":"Designing for people: design thinking, UX, accessibility, and apps on phones, desktops and the web.",
 "Quality":"Proving it works, and that it stays fast under load.",
 "Security":"Building it safely, and thinking like a defender.",
 "Data":"Moving, shaping and trusting data, from a file to a warehouse, on any platform.",
 "Architecture &amp; design":"Choosing boundaries and trade-offs you can explain.",
 "Cloud providers":"What the cloud is made of, and the same jobs done on Google Cloud and AWS, side by side.",
 "Platform &amp; operations":"Shipping safely, running containers, seeing what is happening, and keeping it up.",
 "AI":"Using AI with judgement: how it works, where it helps, and the guard rails.",
 "Tools":"Specific products and services, kept apart so the concepts above stay neutral.",
 "Thinking &amp; character":"How to think clearly and live well. The part no tool replaces.",
 "Frontiers":"Ideas to understand now that may matter more later.",
}
code={
 "linux":("well-rounded-engineer-fundamentals","linux"),"networking":("well-rounded-engineer-fundamentals","networking"),
 "web":("well-rounded-engineer-fundamentals","web"),"docker":("well-rounded-engineer-fundamentals","docker"),
 "java":("well-rounded-engineer-code","java"),"python":("well-rounded-engineer-code","python"),
 "testing":("well-rounded-engineer-code","testing"),"architecture":("well-rounded-engineer-code","patterns"),
 "sql":("well-rounded-engineer-data","sql"),"datalibs":("well-rounded-engineer-data","datalibs"),
 "dbt":("well-rounded-engineer-data","dbt"),"dags":("well-rounded-engineer-data","airflow"),
}
def coderef(t):
    r,f=code[t]; return f'{GH}{r}/tree/main/{f}'
order=[t for _,ts in groups for t in ts]
labels=dict(re.findall(r'<a href="#([a-z0-9]+)" data-tab="\1">([^<]+)</a>',s))
labels.update(dsa="Data Structures &amp; Algorithms",neural="Neural Networks",graphdb="Graph Databases",apihistory="How APIs Evolved",agentsec="Agentic AI Security",distsys="Distributed Systems",pki="Keys, Certificates &amp; SSH",patterns="SOLID &amp; Design Patterns",realtime="Real-time to the Browser",atob="Solution Architecture: A to B",azuredata="Data on Azure",specs="Specifications",retailcloud="Retail &amp; Hybrid Cloud",banking="Banking &amp; Low Latency",humanagents="Humans &amp; Agents",javascript="JavaScript",buildtools="Build Tools",ways="Ways of Working",designux="Design Thinking &amp; UX",accessibility="Accessibility",internet="How the Internet Is Tied Together",everydayscience="Everyday Science",hardware="How Computers Are Built",electronics="Electronics &amp; Chips",reading="Reading List",apps="Apps: Native or Cross-platform",uihistory="UI History",k8sdr="Kubernetes DR &amp; Best Practices",bitcoin="Bitcoin &amp; Blockchain",robotics="Robotics",kotlin="Kotlin",go="Go",rust="Rust",awsdata="Data on AWS",opensource="Our open source",aiworry="Worried about AI?",cyber="Cybersecurity",quantum="Quantum Computing",cloudinside="How the cloud is built",agentsgcp="Agents on GCP",history="A brief history",why="Why this guide exists",body="Body, Mind &amp; Nature",mathematics="Mathematics",science="Science &amp; Method",philosophy="Philosophy",goodhuman="Being a Good Human",homelab="Home Lab",behaviours="Behaviours",servicemesh="Service Mesh &amp; Istio",helm="Helm Charts",operators="Operators",claudetools="Claude Code &amp; Cowork",copilot="GitHub Copilot",agentharness="Agent Harness",web3="Web 3.0",solid="Solid",datalibs="Data Libraries",culvert="Culvert",cloudcompare="GCP vs AWS vs Azure",opstools="Ops Tooling",blueprints="Frameworks vs AI",payments="Payment Gateways",performance="Performance",caching="Caching",observability="Observability",sre="SRE",ai="AI for Engineers",llm="LLMs",rag="RAG",mcp="MCP",microservices="Microservices",eventsourcing="Event Sourcing",web="Web Fundamentals",graphql="GraphQL",gcpdata="Data on GCP",apis="APIs &amp; Integration",kafka="Kafka",apigee="Apigee",oauth="OAuth &amp; OIDC",harness="Harness")
labels.update(privacy="Personal Data Across Services",pki="Keys, Certificates &amp; SSH",patterns="SOLID &amp; Design Patterns",realtime="Real-time to the Browser",atob="Solution Architecture: A to B",azuredata="Data on Azure",specs="Specifications",retailcloud="Retail &amp; Hybrid Cloud",banking="Banking &amp; Low Latency",humanagents="Humans &amp; Agents",javascript="JavaScript",buildtools="Build Tools",ways="Ways of Working",designux="Design Thinking &amp; UX",accessibility="Accessibility",internet="How the Internet Is Tied Together",everydayscience="Everyday Science",hardware="How Computers Are Built",electronics="Electronics &amp; Chips",reading="Reading List",apps="Apps: Native or Cross-platform",uihistory="UI History",k8sdr="Kubernetes DR &amp; Best Practices",bitcoin="Bitcoin &amp; Blockchain",robotics="Robotics",kotlin="Kotlin",go="Go",rust="Rust",awsdata="Data on AWS",opensource="Our open source",aiworry="Worried about AI?",cyber="Cybersecurity",quantum="Quantum Computing",cloudinside="How the cloud is built",agentsgcp="Agents on GCP",history="A brief history",why="Why this guide exists",body="Body, Mind &amp; Nature",mathematics="Mathematics",science="Science &amp; Method",philosophy="Philosophy",goodhuman="Being a Good Human",homelab="Home Lab",behaviours="Behaviours",servicemesh="Service Mesh &amp; Istio",helm="Helm Charts",operators="Operators",claudetools="Claude Code &amp; Cowork",copilot="GitHub Copilot",agentharness="Agent Harness",web3="Web 3.0",solid="Solid",datalibs="Data Libraries",culvert="Culvert",cloudcompare="GCP vs AWS vs Azure",opstools="Ops Tooling",blueprints="Frameworks vs AI",payments="Payment Gateways",performance="Performance",caching="Caching",observability="Observability",sre="SRE",ai="AI for Engineers",llm="LLMs",rag="RAG",mcp="MCP",microservices="Microservices",eventsourcing="Event Sourcing",web="Web Fundamentals",graphql="GraphQL",gcpdata="Data on GCP",apis="APIs &amp; Integration",kafka="Kafka",apigee="Apigee",oauth="OAuth &amp; OIDC",harness="Harness")
missing=set(order)-set(labels); assert not missing, missing

nav=['    <nav aria-label="Sections">']
for g,ts in groups:
    if g: nav.append(f'      <span class="navgrp">{g}</span>')
    nav += [f'      <a href="#{t}" data-tab="{t}">{labels[t]}</a>' for t in ts]
nav.append('    </nav>')
s=re.sub(r'    <nav aria-label="Sections">.*?</nav>','\n'.join(nav),s,flags=re.S)
s=re.sub(r'const tabs = \[[^\]]*\];','const tabs = ['+','.join(f'"{t}"' for t in order)+'];',s)

# 2. reorder sections
mstart=s.index('<main class="wrap">')+len('<main class="wrap">'); mend=s.index('<p class="empty" id="empty"')
blocks={m.group(1):m.group(0) for m in re.finditer(r'(?:<!-- =+ [^>]*=+ -->\s*)?<section class="panel" id="p-([a-z0-9]+)".*?</section>',s[mstart:mend],flags=re.S)}
assert set(blocks)==set(order), set(blocks)^set(order)

# 3. inject levels + explore cards
NAMES=[("F","1","Foundation"),("P","2","Practitioner"),("S","3","Senior"),("E","4","Expert")]
def cards(t):
    d=D[t]
    lv=''.join(f'<div class="lvl"><h4><span class="lvtag">{n}</span> {name}</h4><ul>'+''.join(f'<li>{x}</li>' for x in d[k])+'</ul></div>' for k,n,name in NAMES)
    tp=''.join(f'<li>{x}</li>' for x in d["topics"])
    ln=''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{ti}</a><span class="lnote"> {no}</span></li>' for ti,u,no in d["links"])
    repo=code[t][0] if t in code else SITE
    ask=f'<a href="{GH}{repo}/issues/new?title={quote("["+html.unescape(labels[t])+"] ")}" target="_blank" rel="noopener">open an issue on GitHub</a>'
    src=(('<p class="sources"><b>Checked against:</b> '+'; '.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in d["sources"])+'.'+(' A few claims could not be confirmed at their official source from here and are being re-checked.' if d.get("pending") else '')+'</p>') if d.get("sources") else '')
    run=(f'<p class="runcode"><b>Run the code:</b> <a href="{coderef(t)}" target="_blank" rel="noopener">{code[t][0]}/{code[t][1]}</a>, with a README that says how to run it and what it shows. Stuck, or found a mistake? {ask}.</p>' if t in code
         else f'<p class="runcode">A question, or found a mistake? {ask}. Nothing here is tracked and there are no comments to store: questions live in the open, where the next learner can find the answer.</p>')
    return (f'\n  <!-- levels -->\n  <article class="card wide"><h3>Levels: what to expect</h3><div class="levels">{lv}</div>'
            f'<p class="note">Each level includes the ones before it. See <a href="#start">Start here</a> for what the levels mean.</p></article>\n'
            f'  <article class="card wide"><h3>Explore further</h3><div class="explore"><div><h4>Study next</h4><ul>{tp}</ul></div>'
            f'<div><h4>Official docs and good reading</h4><ul class="links">{ln}</ul></div></div>{src}{run}</article>\n')
for t in order:
    if t in NARRATIVE: continue
    b=blocks[t]
    b=re.sub(r'\n  <!-- levels -->.*?</article>\n  <article class="card wide"><h3>Explore further</h3>.*?</article>\n','',b,flags=re.S)
    k=b.rindex('  </div>\n</section>')
    blocks[t]=b[:k].rstrip()+'\n'+cards(t)+'\n'+b[k:]
s=s[:mstart]+'\n\n'+'\n\n'.join(blocks[t] for t in order)+'\n\n'+s[mend:]

# 4. Start here: level scale card, new table rows, suggested order
scale='''  <article class="card wide" id="levels-scale"><h3>The four levels used on every tab</h3>
    <div class="levels">
      <div class="lvl"><h4><span class="lvtag">1</span> Foundation</h4><p>Can use it with examples and guidance. Reads it, runs it, makes small changes safely, and knows when to ask.</p></div>
      <div class="lvl"><h4><span class="lvtag">2</span> Practitioner</h4><p>Works independently. Builds and ships features with it, tests them, debugs ordinary problems, follows the team's standards.</p></div>
      <div class="lvl"><h4><span class="lvtag">3</span> Senior</h4><p>Designs with it. Makes trade-offs, reviews others' work, handles the hard incidents, and mentors.</p></div>
      <div class="lvl"><h4><span class="lvtag">4</span> Expert</h4><p>Sets direction across teams. Knows the internals, writes the standards and blueprints, and leads migrations and decisions.</p></div>
    </div>
    <p><b>Where a Y-shaped engineer aims:</b> Senior in their own arm (data or platform); Practitioner in the foundations, testing, security and the other arm; at least Foundation everywhere else. Expert in one or two areas comes with time and is not expected of everyone.</p>
    <p class="note">Each tab ends with its own level expectations and an "Explore further" card of official docs, books and topics to study next.</p>
  </article>

'''
if 'id="levels-scale"' not in s:
    i=s.index('  <article class="card wide"><h3>How much of each tab you need</h3>'); s=s[:i]+scale+s[i:]
newrows={
 "internet":("How the Internet Is Tied Together","Explain autonomous systems, BGP, exchange points, CDNs and DNS roots.","Design around shared internet dependencies: DNS, CDN and region failures."),
 "hardware":("How Computers Are Built","Explain RISC vs CISC, firmware and drivers, and why GPUs suit AI.","Choose hardware for a workload; reason about cores, memory, storage and accelerators."),
 "electronics":("Electronics &amp; Chips","Explain transistors, logic gates and what an instruction set is.","Digital design with an HDL and FPGAs; open hardware such as RISC-V; design for repair."),
 "apps":("Apps: Native or Cross-platform","Explain native, shared-logic, cross-platform and web options.","Choose an app architecture for a product and team, and plan how it evolves."),
 "k8sdr":("Kubernetes DR &amp; Best Practices","Use replicas, probes, PDBs and zone spreading; know your RPO and RTO.","Backup and restore with etcd snapshots and Velero, DR strategies, restore drills."),
 "bitcoin":("Bitcoin &amp; Blockchain","Explain hashes, linked blocks, proof of work and keys.","Consensus trade-offs, key custody, and when a blockchain is the wrong tool."),
 "robotics":("Robotics","Explain sense-think-act and tune a PID loop in simulation.","Kinematics, SLAM and planning on ROS 2, with safety designed in."),
 "kotlin":("Kotlin","Read and write Kotlin beside Java; use null safety and data classes.","Coroutines, Java interop at scale, multiplatform and Android or server architecture."),
 "go":("Go","Write a small service with errors as values and a table-driven test.","Concurrency with goroutines and context, profiling, and reading cloud tools' source."),
 "buildtools":("Build Tools","Run a Maven, Gradle or npm build; read a lockfile and a dependency tree.","Build caches, version catalogs and BOMs, install-script policy, and CI build speed."),
 "javascript":("JavaScript","Explain closures, the event loop and promises; change a page with no framework.","Language patterns under any framework, Baseline support, TypeScript, and performance on the main thread."),
 "specs":("Specifications","Read RFC 2119 key words; find the spec behind a format you use daily.","Choose an interface description by requirement; write specs others build from."),
 "retailcloud":("Retail &amp; Hybrid Cloud","Name the systems a retailer connects, and the events and APIs between them.","When on premises and a second cloud pay off, by requirement, with their costs."),
 "banking":("Banking &amp; Low Latency","Explain how a bank's systems fit together, and what instant payments changed.","Latency budgets, in-memory and lock-free designs, kernel bypass, and measuring without coordinated omission."),
 "rust":("Rust","Explain ownership and borrowing; use Result, Option and match.","Lifetimes, traits and async; safe interfaces around unsafe code; performance work."),
 "distsys":("Distributed Systems","Explain the fallacies, CAP and quorums, and read a database's guarantees.","Reason about clocks, consensus and split brain; test with seeded simulation."),
 "privacy":("Personal Data Across Services","Say where personal data spreads in a system, and what tokenisation and pseudonymisation do.","Design erasure across services, crypto-shredding, retention conflicts and data residency."),
 "agentsec":("Agentic AI Security","Explain prompt injection and excessive agency; name the OWASP risks.","Design agent tools with least privilege, approvals and sandboxing; test with attacks."),
 "apihistory":("How APIs Evolved","Place RPC, CORBA, SOAP, REST, gRPC, GraphQL, MCP and A2A on a timeline.","Explain what an AI or agent gateway adds to an API gateway, and choose a style by requirement."),
 "graphdb":("Graph Databases","Explain nodes, edges and properties, and property graphs vs RDF.","Write graph queries, compare a graph with a relational database, and choose by requirement."),
 "neural":("Neural Networks","Explain a neuron, layers, weights and activation functions.","Explain loss, backpropagation and gradient descent, and choose an architecture by requirement."),
 "dsa":("Data Structures &amp; Algorithms","Read Big O; know arrays, lists, hash tables, trees, heaps and graphs.","Pick a structure for the most frequent operation; reason about sorting, search and graph algorithms."),
 "pki":("Keys, Certificates &amp; SSH","Explain key pairs, certificates and CAs; make a CSR and an SSH key.","Read and fix chain, name and expiry errors; automate renewal; sign commits."),
 "patterns":("SOLID &amp; Design Patterns","Name the five SOLID principles and spot the smell each one fixes.","Choose a pattern by the problem in front of you, and know when not to."),
 "realtime":("Real-time to the Browser","Explain real time versus near real time; use SSE or a WebSocket from a browser.","Kafka-to-browser fan-out, reconnect and replay, and choosing a transport by requirement."),
 "atob":("Solution Architecture: A to B","Tell business, solution and enterprise architecture apart; label work strategic, tactical or temporary.","Plan baseline, transition and target states; transitional patterns and their removal."),
 "azuredata":("Data on Azure","Name the Azure service for each data stage; land files in Data Lake Storage.","Fabric or separate services, roles and ACLs together, tiers and cost."),
 "awsdata":("Data on AWS","Name the AWS service for each data stage; query S3 data with Athena.","Lake design with Glue, Lake Formation, Redshift and streaming; IAM and cost."),
  "cloudinside":("How the cloud is built","Explain zones, regions, VMs, containers and the control plane.","Failure domains, isolation, shared responsibility and cost from first principles."),
 "oauth":('OAuth &amp; OIDC','Protect an API with JWT validation; use the code flow with PKCE through a library.','Identity architecture, flow choice per client, token lifetimes, advanced specs.'),
 "apis":('APIs &amp; Integration','Explain REST and status codes; read an OpenAPI spec; tell sync from async.','Choosing API styles, gateway and mesh design, versioning and API governance.'),
 "web":("Web Fundamentals","Explain a page load end to end; read headers in DevTools; know cookies and CORS.","Caching, rendering models, web security headers, performance and accessibility."),
 "microservices":("Microservices","Explain when to split and why services own data; work within one service.","Service boundaries, resilience, sagas and read models, monolith migration."),
 "eventsourcing":("Event Sourcing","Explain events, aggregates, projections and CQRS.","Event modelling and versioning, projections, snapshots, when to use it."),
 "llm":("LLMs","Explain how LLMs work and their limits; make a structured call.","Runtimes, self-hosting, agent harnesses, model strategy."),
 "rag":("RAG","Explain the RAG phases; run a vector search; prompt with citations.","Chunking, hybrid search, reranking, evaluation and security for retrieval."),
 "mcp":("MCP","Add an MCP server to Claude Code; explain tools and resources.","Building and deploying MCP servers; MCP around data pipelines."),
 "observability":("Observability","Find logs and errors for a request; read a dashboard; log with IDs.","OpenTelemetry, metrics design, tracing, alerting and telemetry cost."),
 "sre":("SRE","Explain SLOs and error budgets; follow a runbook during an incident.","SLO design, burn-rate alerting, incident command, postmortems, toil."),
 "performance":("Performance","Read latency percentiles; spot N+1 queries and missing indexes.","Profiling, load testing, capacity planning and cost-performance trade-offs."),
 "caching":("Caching","Explain cache-aside, TTLs and hit ratio; read HTTP cache headers.","Multi-layer caching, invalidation, stampedes, what never to cache."),
 "payments":("Payment Gateways","Explain the payment lifecycle and the server-verified checkout flow.","Idempotency, webhooks, ledgers, reconciliation, subscriptions and compliance."),
 "opstools":("Ops Tooling","Read Grafana or Dynatrace dashboards; work a ServiceNow incident.","PromQL and alert rules, log shipping, alert-to-incident and change automation."),
 "blueprints":("Frameworks vs AI","Use team blueprints; explain why owning generated code is the real cost.","Design and run frameworks; codemods; build-vs-generate decisions."),
 "cloudcompare":("GCP vs AWS vs Azure","Map common services across the three clouds; know their account structures.","Provider choice, portability, IAM and networking differences, data residency."),
 "datalibs":("Data Libraries","Process a file with pandas or Polars; read Parquet; match library to data size.","Engine choice, pushdown and file layout, distributed and streaming processing."),
 "culvert":("Culvert","Explain contracts and adapters; install and use an adapter.","Cloud-neutral pipeline design, adapters, job control and orchestration gates."),
 "claudetools":("Claude Code &amp; Cowork","Run Claude Code in a repo; write a CLAUDE.md; review its changes.","Hooks, skills, subagents, gated agent workflows, Cowork plugins."),
 "copilot":("GitHub Copilot","Use completions and chat; follow repo instructions.","Instructions, coding agent, policies, consistency with other agents."),
 "agentsgcp":("Agents on GCP","Run one agent task as a Cloud Run job with its own service account.","Workspaces, triggers, approvals and guard rails for agents in your own project."),
 "agentharness":("Agent Harness","Explain the parts of a harness; configure a ready-made one.","Building bounded, gated, evaluated harnesses."),
 "web3":("Web 3.0","Tell Web3 from the Semantic Web; know when a blockchain is not needed.","Smart contracts, linked data, knowledge graphs, product data standards."),
 "solid":("Solid","Explain Pods, WebIDs and app–data separation.","Solid apps, access control, consent-based data sharing."),
 "helm":("Helm Charts","Install, upgrade and roll back a release; read a chart's values.","Chart design, library charts, hooks, testing, GitOps delivery."),
 "operators":("Operators","Explain CRDs, controllers and reconcile; use well-known operators.","Building idempotent controllers, CRD versioning, operator testing."),
 "servicemesh":("Service Mesh &amp; Istio","Explain what a mesh does; read Istio routing and policy resources.","mTLS rollout, authorisation, traffic shifting, ambient vs sidecar, mesh operations."),
 "mathematics":("Mathematics","Read Big-O; use percentiles over averages; know why floats are wrong for money.","Complexity, probability, statistics and linear algebra applied with rigour."),
 "quantum":("Quantum Computing","Explain qubits, superposition and why Shor's algorithm threatens RSA.","Post-quantum migration: inventory, crypto agility, ML-KEM and ML-DSA."),
 "cyber":("Cybersecurity","Know how attacks unfold (MITRE ATT&amp;CK) and report incidents fast.","Detection engineering, incident response and red/blue/purple teaming."),
 "science":("Science &amp; Method","Reproduce, change one thing, measure before and after.","Falsifiable hypotheses, controlled experiments, reading research critically."),
 "philosophy":("Philosophy","Ask how we know; spot fallacies; know the codes of ethics.","Systems thinking, ethical trade-offs, wise judgement under uncertainty."),
 "body":("Body, Mind &amp; Nature","Sleep, move and take breaks; notice stress in your body.","Sustainable pace for a team; humane on-call; greener systems."),
 "goodhuman":("Being a Good Human","Honesty, kindness, gratitude; look after your health.","Psychological safety, mentoring, integrity under pressure."),
 "graphql":("GraphQL","Read a schema and write queries with variables; explain resolvers.","Batching, federation, schema evolution, GraphQL security."),
  "kafka":('Kafka','Explain partitions, offsets and consumer groups; read consumer lag.','Topic and key design, delivery guarantees, Connect and stream processing.'),
 "gcpdata":('Data on GCP','Name the service for each data stage; load and query data on GCP.','Platform design across Dataflow, Pub/Sub, Datastream, Dataplex; cost and governance.'),
 "apigee":('Apigee','Explain proxies, policies and products; call an API through Apigee.','Proxy and product design, shared flows, edge security, Apigee in CI and Terraform.'),
 "harness":('Harness','Run a pipeline, read its logs, approve or roll back.','Org-wide templates and policies, verified progressive delivery.'),
}
for t,(name,k,d) in newrows.items():
    if f'<tr><td><a href="#{t}">' not in s:
        row=f'      <tr><td><a href="#{t}">{name}</a></td><td>{k}</td><td>{d}</td></tr>\n'
        i=s.index('      <tr><td><a href="#linux">'); s=s[:i]+row+s[i:]
rows=dict((m.group(2),m.group(1)) for m in re.finditer(r'(      <tr><td><a href="#([a-z0-9]+)">.*?</tr>\n)',s,flags=re.S))
assert set(rows)==set(order)-set(NARRATIVE), set(rows)^(set(order)-set(NARRATIVE))
first=min(s.index(r) for r in rows.values()); last=max(s.index(r)+len(r) for r in rows.values())
s=s[:first]+''.join(rows[t] for t in order if t in rows)+s[last:]
# the map: one card per group, first thing on Start here (replaces the old "Suggested order" list)
s=re.sub(r'  <article class="card"><h3>Suggested order for a newcomer</h3>.*?</article>\n\n?','',s,count=1,flags=re.S)
# one plain stroke icon per group on the map (decorative: aria-hidden)
ICON={"Foundations":"M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3M6 6h12v12H6z",
 "Languages":"M8 7l-5 5 5 5M16 7l5 5-5 5",
 "Building services":"M4 4h16v6H4zM4 14h16v6H4zM8 7h.01M8 17h.01",
 "User interfaces":"M3 4h18v16H3zM3 9h18M9 9v11",
 "Quality":"M4 12l5 5L20 6",
 "Security":"M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z",
 "Data":"M4 6c0-1.7 3.6-3 8-3s8 1.3 8 3-3.6 3-8 3-8-1.3-8-3zM4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3",
 "Architecture &amp; design":"M3 3h8v8H3zM13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8z",
 "Platform &amp; operations":"M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1",
 "Cloud providers":"M7 18h10a4 4 0 0 0 0-8 6 6 0 0 0-11.6 1.5A3.5 3.5 0 0 0 7 18z",
 "AI":"M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6",
 "Tools":"M14 6a4 4 0 0 0 5 5l-9 9a2 2 0 0 1-3-3l9-9a4 4 0 0 0-2-2z",
 "Thinking &amp; character":"M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21c1-4 4-6 8-6s7 2 8 6",
 "Frontiers":"M5 15c-1 2-1 4-1 4s2 0 4-1M9 15l-3-3c2-5 6-9 13-9 0 7-4 11-9 13zM14 10h.01"}
def icon(g):
    d=ICON.get(g)
    return f'<span class="gmap-ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></svg></span>' if d else ''
def gcard(g,ts):
    pages=', '.join(f'<a href="#{t}">{labels[t]}</a>' for t in ts)
    repos=[]
    for t in ts:
        if t in code and code[t][0] not in repos: repos.append(code[t][0])
    run=''.join(f'<p class="gmap-run"><a href="{GH}{r}" target="_blank" rel="noopener">Run the code: {r}</a></p>' for r in repos)
    return f'<div class="gmap-card"><h4>{icon(g)}<span class="gmap-n">{n}</span> {g}</h4><p>{blurb[g]}</p><p class="gmap-pages">{pages}</p>{run}</div>'
cs=[]
for n,(g,ts) in enumerate([x for x in groups if x[0] in blurb],1):
    cs.append(gcard(g,ts))
gmap=('  <article class="card wide" id="guide-map"><h3>The map: the groups, in the order to learn them</h3>\n'
      '    <p>Start with Foundations and work down; come back to Thinking &amp; character often. Each page ends with its levels, what to study next, code you can run where it exists, and a link to ask a question on GitHub. The story behind the guide and EnrichMeAI&rsquo;s own open-source projects sit apart, at the end of the list.</p>\n'
      '    <div class="gmap">'+''.join(cs)+'</div>\n  </article>\n\n')
s=re.sub(r'  <article class="card wide" id="guide-map">.*?</article>\n\n','',s,flags=re.S)
i=s.index('<section class="panel" id="p-start"'); j=s.index('  <div class="grid">\n',i)+len('  <div class="grid">\n')
s=s[:j]+gmap+s[j:]

# 5. CSS
if '.levels{' not in s:
    s=s.replace('details{border','.levels{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:10px;margin:6px 0}\n.lvl{border:1px solid var(--line);border-radius:6px;padding:8px 10px;background:var(--bg);min-width:0}\n.lvl h4,.explore h4{margin:0 0 4px;font:700 14px var(--f-display)}\n.lvl ul{margin:0;padding-left:16px}.lvl p{margin:0}\n.lvtag{display:inline-block;min-width:20px;text-align:center;border-radius:4px;background:var(--accent-soft);color:var(--accent);font:700 12px var(--f-body);padding:1px 5px;margin-right:4px}\n.explore{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}\n.explore ul{padding-left:18px;margin:4px 0}\n.links li{margin:5px 0}.links a{color:var(--accent);font-weight:700}\n.lnote{color:var(--muted);font-size:13.5px}\ndetails{border',1)
open(p,'w').write(s)
print(len(order),"tabs")
