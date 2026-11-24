"""Gate: every acceptance criterion in every spec has a test tagged with its id, and no test names an id the spec lacks.
Paths are resolved from this file, so it gives the same answer from any directory. Finding no criteria is a failure:
a gate that cannot see anything has not passed."""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
specs = {m for p in (HERE / "specs").glob("*/spec.md")
         for m in re.findall(r"^- (AC-\d+):", p.read_text(), re.M)}
tags = {m for p in (HERE / "src/test").rglob("*.java")
        for m in re.findall(r'@Tag\("(AC-\d+)"\)', p.read_text())}
if not specs:
    print("FAIL no acceptance criteria found under", HERE / "specs")
    sys.exit(1)
missing, unknown = sorted(specs - tags), sorted(tags - specs)
for ac in missing: print(f"FAIL {ac} has no test")
for ac in unknown: print(f"FAIL a test is tagged {ac}, which no spec defines")
print(f"{len(specs)} criteria, {len(specs & tags)} traced")
sys.exit(1 if missing or unknown else 0)
