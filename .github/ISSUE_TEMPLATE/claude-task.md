---
name: Claude task
about: A site task for the Claude workflow. Creating it does not start anything. Review it, then add the `claude` label (founder's account only).
labels: []
---

## Goal

<!-- One sentence: what a visitor will see or be able to do when this is done. -->

## Measure

<!-- Every task names its number, or says why it has none. -->
- Metric (site_check findings, broken links, a claim now sourced, …):
- Baseline, measured on main (command and output):
- Target:

## Evidence of done

<!-- Each line is checkable by someone who only reads the PR and its CI run. -->
- [ ] Red proof: the check that fails on main (a site_check fixture), or the wrong sentence quoted beside the source that contradicts it
- [ ] Green proof: the same check passing on the branch, quoted
- [ ] Each changed page looked at, at 375 px and 1280 px

## Risk

<!-- Exactly one. It decides who merges (merge-gate skill). -->
- [ ] docs: only repo docs (*.md), nothing a visitor sees
- [ ] copy: a claim corrected to match a product's release tag, with the source
- [ ] code: markup, CSS, assets, the checker or hooks
- [ ] voice: new or rewritten wording in the founder's voice (the founder merges)

## Surface

<!-- Pages and files expected to change. -->

## Out of scope

<!-- What must NOT change in this task. -->

## Stop and ask if

<!-- Conditions where Claude replies with a question instead of continuing. -->
- a claim would run ahead of the product's latest release tag
- a caveat ("what it cannot do") would be removed
- the change touches CNAME, the Pages workflow, or DNS
- the surface grows beyond what is listed above
