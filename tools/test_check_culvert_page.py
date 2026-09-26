"""Tests for tools/check-culvert-page.py: each rule fails on the page it is meant to catch.

Run: python3 -m unittest tools/test_check_culvert_page.py
"""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("ccp", Path(__file__).with_name("check-culvert-page.py"))
ccp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ccp)

FACTS = {
    "pypi_version": "0.1.1",
    "maven": {"data-pipeline-core": "0.2.0", "data-pipeline-aws-s3": "0.2.0", "data-pipeline-new": None},
    "extras": ["gcp", "all"],
}

GOOD = """<html><body><main>
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


def errors(html, facts=FACTS):
    return ccp.check(html, facts)


class CheckCulvertPage(unittest.TestCase):
    def test_good_page_passes(self):
        self.assertEqual(errors(GOOD), [])

    def test_stale_pypi_version(self):
        e = errors(GOOD.replace('pypi-version">0.1.1', 'pypi-version">0.1.0'))
        self.assertTrue(any("pypi-version" in x and "0.1.0" in x for x in e), e)

    def test_new_maven_release(self):
        facts = dict(FACTS, maven={**FACTS["maven"], "data-pipeline-core": "0.3.0", "data-pipeline-aws-s3": "0.3.0"})
        e = errors(GOOD, facts)
        self.assertTrue(any("maven-version" in x for x in e), e)
        self.assertTrue(any("data-pipeline-core row shows version" in x for x in e), e)
        self.assertTrue(any('data-culvert-release="0.3.0"' in x for x in e), e)

    def test_new_library_without_a_row(self):
        facts = dict(FACTS, maven={**FACTS["maven"], "data-pipeline-azure-queue": None})
        self.assertTrue(any("data-pipeline-azure-queue" in x for x in errors(GOOD, facts)))

    def test_library_released_but_row_says_unreleased(self):
        facts = dict(FACTS, maven={**FACTS["maven"], "data-pipeline-new": "0.2.0"})
        e = errors(GOOD, facts)
        self.assertTrue(any("data-pipeline-new is released" in x for x in e), e)

    def test_row_for_removed_library(self):
        facts = dict(FACTS, maven={k: v for k, v in FACTS["maven"].items() if k != "data-pipeline-new"})
        self.assertTrue(any("no longer" in x or "not a library" in x for x in errors(GOOD, facts)))

    def test_extras_both_ways(self):
        e = errors(GOOD, dict(FACTS, extras=["gcp", "all", "aws"]))
        self.assertTrue(any("culvert[aws] is missing" in x for x in e), e)
        e = errors(GOOD, dict(FACTS, extras=["gcp"]))
        self.assertTrue(any("culvert[all]" in x and "no longer" in x for x in e), e)

    def test_hard_coded_version_outside_markers(self):
        e = errors(GOOD.replace("Python 3.10", "Python 3.10, culvert 0.1.0"))
        self.assertEqual(e, ["version 0.1.0 is hard-coded outside a data-culvert marker — mark it, or drop it"])

    def test_missing_marker_is_an_error(self):
        e = errors(GOOD.replace(' data-culvert="maven-version"', ""))
        self.assertTrue(any('no data-culvert="maven-version"' in x for x in e), e)

    def test_the_real_page_parses(self):
        page = (Path(__file__).resolve().parent.parent / "culvert" / "index.html").read_text(encoding="utf-8")
        nodes = list(ccp.parse(page).walk())
        self.assertTrue(any("data-culvert-artifact" in n.attrs for n in nodes))


if __name__ == "__main__":
    unittest.main()
