"""Tests for tools/check-release-page.py: each rule fails on the page it is meant to catch.

Run: python3 -m unittest tools/test_check_release_page.py
"""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("crp", Path(__file__).with_name("check-release-page.py"))
crp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crp)
ROOT = Path(__file__).resolve().parent.parent

CULVERT = {
    "pypi_version": "0.1.1",
    "maven": {"data-pipeline-core": "0.2.0", "data-pipeline-aws-s3": "0.2.0", "data-pipeline-new": None},
    "extras": ["gcp", "all"],
}
CULVERT_PAGE = """<html><body><main>
<p>culvert <span data-culvert="pypi-version">0.1.1</span> ·
   java <span data-culvert="maven-version">0.2.0</span> · Python 3.10 · Airflow 2.9.x</p>
<code data-culvert-extra="gcp">culvert[gcp]</code><code data-culvert-extra="all">culvert[all]</code>
<table><tbody>
<tr data-culvert-artifact="data-pipeline-core" data-state="released"><td>core</td><td><span data-culvert="artifact-version">0.2.0</span></td></tr>
<tr data-culvert-artifact="data-pipeline-aws-s3" data-state="released"><td>s3</td><td><span data-culvert="artifact-version">0.2.0</span></td></tr>
<tr data-culvert-artifact="data-pipeline-new" data-state="unreleased"><td>new</td><td>not yet</td></tr>
</tbody></table>
<section data-culvert-release="0.2.0"><h3>0.2.0</h3><p>Upgrading from 0.1.1 needs LoadOptions.</p></section>
<script>var v = "9.9.9";</script>
</main></body></html>"""

ETA = {"maven": {"test-core": None, "test-cloud-aws": None}, "main_version": "0.3.0-alpha1-SNAPSHOT",
       "capabilities": ["BlobStorage", "Queue"]}
ETA_PAGE = """<main>
<p><span data-eta="main-version">0.3.0-alpha1-SNAPSHOT</span> on main · <span data-eta="maven-version">unpublished</span></p>
<p>wait for <code>v<span data-eta="next-version">0.3.0-alpha1</span></code>; coverage 0.81, localstack 3.8</p>
<dt data-eta-capability="BlobStorage">BlobStorage</dt><dt data-eta-capability="Queue">Queue</dt>
<code data-eta-artifact="test-core" data-state="unreleased">test-core</code>
<code data-eta-artifact="test-cloud-aws" data-state="unreleased">test-cloud-aws</code>
</main>"""


def culvert(html=CULVERT_PAGE, facts=CULVERT):
    return crp.check(html, facts, "culvert")


def eta(html=ETA_PAGE, facts=ETA):
    return crp.check(html, facts, "enrich-test-api")


class Culvert(unittest.TestCase):
    def test_good_page_passes(self):
        self.assertEqual(culvert(), [])

    def test_stale_pypi_version(self):
        e = culvert(CULVERT_PAGE.replace('pypi-version">0.1.1', 'pypi-version">0.1.0'))
        self.assertTrue(any("pypi-version" in x and "0.1.0" in x for x in e), e)

    def test_new_maven_release(self):
        facts = dict(CULVERT, maven={**CULVERT["maven"], "data-pipeline-core": "0.3.0", "data-pipeline-aws-s3": "0.3.0"})
        e = culvert(facts=facts)
        self.assertTrue(any("maven-version" in x for x in e), e)
        self.assertTrue(any("data-pipeline-core row shows version" in x for x in e), e)
        self.assertTrue(any('data-culvert-release="0.3.0"' in x for x in e), e)

    def test_new_library_without_a_row(self):
        facts = dict(CULVERT, maven={**CULVERT["maven"], "data-pipeline-azure-queue": None})
        self.assertTrue(any("data-pipeline-azure-queue" in x for x in culvert(facts=facts)))

    def test_library_released_but_row_says_unreleased(self):
        facts = dict(CULVERT, maven={**CULVERT["maven"], "data-pipeline-new": "0.2.0"})
        self.assertTrue(any("data-pipeline-new is released" in x for x in culvert(facts=facts)))

    def test_row_for_removed_library(self):
        facts = dict(CULVERT, maven={k: v for k, v in CULVERT["maven"].items() if k != "data-pipeline-new"})
        self.assertTrue(any("not a published library" in x for x in culvert(facts=facts)))

    def test_extras_both_ways(self):
        self.assertTrue(any("pip extra aws is missing" in x for x in culvert(facts=dict(CULVERT, extras=["gcp", "all", "aws"]))))
        self.assertTrue(any("pip extra all" in x and "no longer" in x for x in culvert(facts=dict(CULVERT, extras=["gcp"]))))

    def test_hard_coded_version_outside_markers(self):
        e = culvert(CULVERT_PAGE.replace("Python 3.10", "Python 3.10, culvert 0.1.0"))
        self.assertEqual(e, ["version 0.1.0 is hard-coded outside a data-culvert marker — mark it, or drop it"])

    def test_missing_marker_is_an_error(self):
        e = culvert(CULVERT_PAGE.replace(' data-culvert="maven-version"', ""))
        self.assertTrue(any('no data-culvert="maven-version"' in x for x in e), e)


class EnrichTestApi(unittest.TestCase):
    def test_good_unpublished_page_passes(self):
        self.assertEqual(eta(), [])

    def test_main_version_bump(self):
        e = eta(facts=dict(ETA, main_version="0.4.0-SNAPSHOT"))
        self.assertTrue(any("main-version" in x for x in e), e)
        self.assertTrue(any("next-version" in x and "0.4.0" in x for x in e), e)

    def test_first_release(self):
        e = eta(facts=dict(ETA, maven={"test-core": "0.3.0-alpha1", "test-cloud-aws": "0.3.0-alpha1"}))
        self.assertTrue(any('maven-version" says \'unpublished\'' in x for x in e), e)
        self.assertTrue(any("test-core is released" in x for x in e), e)
        self.assertTrue(any('data-eta-release="0.3.0-alpha1"' in x for x in e), e)

    def test_new_capability(self):
        e = eta(facts=dict(ETA, capabilities=["BlobStorage", "Queue", "Secrets"]))
        self.assertEqual(e, ["capability Secrets is missing from the page (data-eta-capability)"])

    def test_removed_capability(self):
        e = eta(facts=dict(ETA, capabilities=["BlobStorage"]))
        self.assertTrue(any("capability Queue" in x and "no longer" in x for x in e), e)

    def test_tag_and_snapshot_versions_are_caught(self):
        e = eta(ETA_PAGE.replace("coverage 0.81", "tag v0.3.0-alpha1, main 0.3.0-alpha1-SNAPSHOT, coverage 0.81"))
        self.assertIn("version v0.3.0-alpha1 is hard-coded outside a data-eta marker — mark it, or drop it", e)
        self.assertIn("version 0.3.0-alpha1-SNAPSHOT is hard-coded outside a data-eta marker — mark it, or drop it", e)


class RealPages(unittest.TestCase):
    def test_real_pages_parse_and_carry_markers(self):
        for project, cfg in crp.PROJECTS.items():
            nodes = list(crp.parse((ROOT / cfg["page"]).read_text(encoding="utf-8")).walk())
            self.assertTrue(any(n.attrs.get(cfg["attr"]) == "maven-version" for n in nodes), project)


if __name__ == "__main__":
    unittest.main()
