# Standards as Guardrails: the example

The code behind <https://enrichmeai.com/well-rounded-engineer/guardrails/>. Java 21, Maven,
Spring Boot 4.2.0, ArchUnit 1.5.1, H2 in memory. Every result the page states can be re-run
from this folder.

| Folder | What it is |
|---|---|
| `paved-road/platform-starter` | The shared starter: one error format (`PlatformErrors`, `DomainException`) and the architecture rules (`PlatformRules`) |
| `paved-road/stock-service` | The stock reservation service built on the starter, its spec, its tests, a Claude Code hook, Dependabot files, a deploy workflow that calls the platform's, and an AsyncAPI contract |
| `paved-road/platform-templates` | The platform's reusable deploy workflow and a Kubernetes ValidatingAdmissionPolicy |
| `off-road` | Two controllers a model might write, which break the rules |

## Re-run the results

**The service passes: 10 tests, 0 failures** (9 spec tests + the platform rules).

```bash
cd paved-road && mvn -B install
```

**The off-road code fails the build: 14 violations across all five rules.**

```bash
cp ../off-road/*.java stock-service/src/main/java/com/example/stock/
mvn -B install -pl stock-service -am -Dtest=PlatformRulesTest -Dsurefire.failIfNoSpecifiedTests=false
rm stock-service/src/main/java/com/example/stock/{Shortcut,Bypass}Controller.java
```

**The hook blocks template-owned files and allows the rest.**

```bash
cd stock-service
for f in /repo/svc/Dockerfile /repo/svc/Dockerfile.prod .github/workflows/deploy.yml /repo/svc/k8s/deployment.yaml \
         /repo/svc/.claude/settings.json /repo/svc/docs/Dockerfile-notes.md /repo/svc/service.yaml; do
  echo "{\"tool_name\":\"Write\",\"tool_input\":{\"file_path\":\"$f\"}}" | .claude/hooks/paved-road.sh 2>/dev/null; echo "exit $? $f"
done
```

Expected: exit 2 for the first five, exit 0 for the last two.

**The AsyncAPI contract is valid** (`@asyncapi/parser` 3.6.6).

```bash
npm install @asyncapi/parser && node validate-asyncapi.mjs paved-road/stock-service/contracts/stock-events.asyncapi.yaml
```

Expected: `valid errors: 0 warnings: 0`.

## Not run

The workflows in `.github/` and `platform-templates/` need a GitHub organisation and a platform
repository; the admission policy needs a cluster. Their YAML parses; they were not executed.
Nothing here has been run against Postgres or with more than one instance.
