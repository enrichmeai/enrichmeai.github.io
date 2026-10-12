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

    def test_released_library_without_a_row(self):
        facts = dict(CULVERT, maven={**CULVERT["maven"], "data-pipeline-azure-queue": "0.2.0"})
        self.assertTrue(any("data-pipeline-azure-queue" in x for x in culvert(facts=facts)))

    def test_unreleased_library_needs_no_row_yet(self):
        # Releases are batched: a module merged on main waits for the release that publishes it.
        facts = dict(CULVERT, maven={**CULVERT["maven"], "data-pipeline-azure-queue": None})
        self.assertEqual(culvert(facts=facts), [])

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


PENSTOCK = {"release": "0.5.2"}
PENSTOCK_PAGE = """<main>
<p class="eyebrow">Penstock · <span data-penstock="release-version">v0.5.2</span></p>
<section data-penstock-release="0.5.2"><h2>What v0.5.2 ships</h2><p>Recall cites cards.</p></section>
<table data-penstock-history><tr><td>v0.1.0</td><td>138</td></tr><tr><td>v0.5.1</td><td>18</td></tr></table>
<p>Pod access needs Cistern <span data-cistern="release-version">v0.2.0</span>.</p>
</main>"""
HOME_PAGE = """<main>
<dl><dt>Cistern</dt><dd><span data-cistern="release-version">v0.2.0</span> · GHCR</dd>
<dt>Penstock</dt><dd><span data-penstock="release-version">v0.5.2</span> · signed jar</dd></dl>
<span class="status"><span data-eta="maven-version">0.3.0-alpha2</span> · alpha</span>
</main>"""


def penstock(html=PENSTOCK_PAGE, facts=PENSTOCK, primary=True):
    return crp.check(html, facts, "penstock", primary=primary)


class GithubReleaseProjects(unittest.TestCase):
    """Penstock and Cistern release on GitHub, not Maven Central: the truth is the latest release tag."""

    def test_good_page_passes(self):
        self.assertEqual(penstock(), [])

    def test_new_release_makes_the_marker_stale(self):
        e = penstock(facts={"release": "0.5.3"})
        self.assertTrue(any('release-version' in x and "0.5.3" in x for x in e), e)

    def test_new_release_needs_a_whats_new_block(self):
        e = penstock(PENSTOCK_PAGE.replace('release-version">v0.5.2', 'release-version">v0.5.3'), {"release": "0.5.3"})
        self.assertTrue(any("what's new" in x and "0.5.3" in x for x in e), e)

    def test_missing_marker_on_the_project_page(self):
        e = penstock(PENSTOCK_PAGE.replace('data-penstock="release-version"', 'class="x"'))
        self.assertTrue(any('no data-penstock="release-version" marker' in x for x in e), e)

    def test_hard_coded_version_outside_a_marker(self):
        e = penstock(PENSTOCK_PAGE.replace("<p>Recall cites cards.</p></section>", "</section><p>Since v0.5.0 it recalls.</p>"))
        self.assertTrue(any("v0.5.0" in x and "hard-coded" in x for x in e), e)

    def test_history_block_is_exempt(self):
        self.assertFalse(any("v0.1.0" in x for x in penstock()))

    def test_a_tool_version_is_marked_as_other(self):
        page = PENSTOCK_PAGE.replace("</main>", "<p>Gradle <span data-other-version>8.14.6</span>.</p></main>")
        self.assertEqual(penstock(page), [])
        self.assertTrue(any("8.14.6" in x for x in penstock(page.replace("<span data-other-version>8.14.6</span>", "8.14.6"))))

    def test_unmarked_link_naming_a_version(self):
        page = PENSTOCK_PAGE.replace("</main>", '<a href="https://github.com/enrichmeai/penstock/releases/tag/v0.5.2">notes</a></main>')
        e = penstock(page)
        self.assertTrue(any("data-link-penstock" in x and "0.5.2" in x for x in e), e)

    def test_release_link_goes_stale_with_the_release(self):
        page = PENSTOCK_PAGE.replace("</main>", '<a data-link-penstock="release" href="https://github.com/enrichmeai/penstock/blob/v0.5.2/README.md">docs</a></main>')
        self.assertEqual(penstock(page.replace('release-version">v0.5.2', 'release-version">v0.5.2')), [])
        e = penstock(page.replace('release-version">v0.5.2', 'release-version">v0.5.3').replace('penstock-release="0.5.2"', 'penstock-release="0.5.3"'),
                     {"release": "0.5.3"})
        self.assertTrue(any("blob/v0.5.2" in x and "0.5.3" in x for x in e), e)

    def test_history_link_must_be_older(self):
        page = PENSTOCK_PAGE.replace("</main>", '<a data-link-penstock="history" href="https://github.com/enrichmeai/penstock/releases/tag/v0.4.0">the notes</a></main>')
        self.assertFalse(any("v0.4.0" in x and "link" in x for x in penstock(page)))
        self.assertEqual(penstock(page.replace("tag/v0.4.0", "tag/v0.5.2")), [])  # "since v0.5.2" is history too
        e = penstock(page.replace("tag/v0.4.0", "tag/v0.6.0"))
        self.assertTrue(any("marked history" in x and "newer" in x for x in e), e)

    def test_other_projects_links_are_not_this_check(self):
        page = PENSTOCK_PAGE.replace("</main>", '<a href="https://github.com/enrichmeai/cistern/releases/tag/v0.2.0">cistern</a></main>')
        self.assertFalse(any("link" in x for x in penstock(page)))

    def test_history_may_not_name_an_unreleased_version(self):
        self.assertEqual(penstock(PENSTOCK_PAGE.replace("<td>v0.5.1</td>", "<td>v0.5.2</td>")), [])
        e = penstock(PENSTOCK_PAGE.replace("<td>v0.5.1</td>", "<td>v0.6.0</td>"))
        self.assertTrue(any("history" in x and "newer" in x for x in e), e)

    def test_repeated_errors_are_collapsed(self):
        page = PENSTOCK_PAGE.replace("</main>", '<p><span data-penstock="release-version">v0.5.2</span></p></main>')
        e = penstock(page, {"release": "0.5.3"})
        self.assertTrue(any("(×2)" in x for x in e), e)

    def test_tag_with_a_v_prefix_matches(self):
        self.assertEqual(penstock(facts={"release": "v0.5.2".lstrip("v")}), [])


class OtherPages(unittest.TestCase):
    """The home page and /persona/ repeat project facts: each mention is a marker, checked against the truth."""

    def test_home_page_in_step(self):
        self.assertEqual(crp.check(HOME_PAGE, PENSTOCK, "penstock", primary=False), [])

    def test_home_page_behind_a_penstock_release(self):
        stale = HOME_PAGE.replace('release-version">v0.5.2', 'release-version">v0.3.0')
        e = crp.check(stale, PENSTOCK, "penstock", primary=False)
        self.assertTrue(any("v0.3.0" in x and "0.5.2" in x for x in e), e)

    def test_unmarked_version_on_the_home_page(self):
        e = crp.check(HOME_PAGE.replace("signed jar", "signed jar, v0.3.0 before"), PENSTOCK, "penstock", primary=False)
        self.assertTrue(any("v0.3.0" in x and "hard-coded" in x for x in e), e)

    def test_another_projects_marker_is_not_a_stray(self):
        self.assertFalse(any("0.3.0-alpha2" in x or "v0.2.0" in x
                             for x in crp.check(HOME_PAGE, PENSTOCK, "penstock", primary=False)))

    def test_no_required_marker_on_a_secondary_page(self):
        self.assertEqual(crp.check("<main><p>No versions here.</p></main>", PENSTOCK, "penstock", primary=False), [])

    def test_maven_marker_on_the_home_page_is_checked(self):
        stale = HOME_PAGE.replace('maven-version">0.3.0-alpha2', 'maven-version">0.3.0-alpha1')
        e = crp.check(stale, {"maven": {"test-core": "0.3.0-alpha2"}}, "enrich-test-api", primary=False)
        self.assertTrue(any("maven-version" in x and "0.3.0-alpha1" in x for x in e), e)


class RealPages(unittest.TestCase):
    MARKER = {"maven": "maven-version", "github": "release-version"}

    def test_real_pages_parse_and_carry_markers(self):
        for project, cfg in crp.PROJECTS.items():
            nodes = list(crp.parse((ROOT / cfg["page"]).read_text(encoding="utf-8")).walk())
            want = self.MARKER[cfg.get("kind", "maven")]
            self.assertTrue(any(n.attrs.get(cfg["attr"]) == want for n in nodes), project)

    def test_penstock_and_cistern_are_covered_with_the_home_page(self):
        for project in ("penstock", "cistern"):
            self.assertIn(project, crp.PROJECTS)
            self.assertIn("index.html", crp.PROJECTS[project].get("also", []))


if __name__ == "__main__":
    unittest.main()
