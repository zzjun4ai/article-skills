---
name: article-writing
description: >-
  Plan, draft, or restructure scientific manuscripts and initial-submission materials from author-provided
  claims, results, figures, notes, or Chinese drafts. Use for titles, abstracts,
  introductions, related work, methods, experiments, results, discussions,
  conclusions, complete manuscript outlines, argument flow, cover letters, title pages,
  highlights, and requests such as 论文写作、科研写作、写paper、搭论文框架、起草论文
  or 首次投稿材料. Use article-polishing for
  language-only editing of finished prose; do not invent evidence or citations.
---

# Article Writing

Build a coherent scientific manuscript whose claims remain matched to evidence.

## Route the request

Determine five axes before drafting: task (`manuscript` or `submission-package`), paper
type (`research`, `methods`, `review`, `hypothesis`, or `algorithmic`), section,
language direction, and target journal or generic audience. Initial-submission
materials belong here; post-decision revision correspondence belongs to
`article-response`. Distinguish drafting from language-only polishing. When the source
material is incomplete, proceed with explicit assumptions only if they do not change
the scientific claim; otherwise use placeholders.

## Shortest successful workflow

1. Inventory author-provided claims, results, figures, tables, methods, citations,
   limitations, and missing inputs. Write the one-sentence manuscript argument before
   drafting paragraphs.
2. Build a claim-evidence-boundary map and section outline. Read
   [references/section-playbooks.md](references/section-playbooks.md) only for the
   requested section.
   For a complete section with genuinely ambiguous framing, show the one-sentence
   argument and paragraph map for confirmation before expanding prose; skip this gate
   when the claim, evidence, and boundary are already clear.
3. Draft each paragraph around one job and one controlling claim. Keep observation,
   analysis, interpretation, and limitation distinct.
4. Use placeholders such as `AUTHOR_INPUT_NEEDED: sample size` for essential missing
   evidence; never fill them with plausible scientific content.
5. Audit terminology, numbers, units, sample sizes, citation keys, figure/table
   references, claim strength, and unresolved placeholders.
6. Read back as a skeptical reviewer. Revise logical jumps and overclaim. When the
   user redirects a draft, apply targeted edits and preserve unaffected paragraphs;
   read [references/routing-and-revision.md](references/routing-and-revision.md).
7. Deliver
   the requested section plus assumptions and missing inputs.

## Output contract

Return the requested manuscript section or outline, the one-sentence argument,
claim-evidence map when useful, and an `Assumptions or missing inputs` block. Preserve
the target medium and report unresolved placeholders and checks actually run.

## Failure behavior

Do not fill gaps with plausible-sounding content. If central evidence, methods, or scope
are missing, preserve a clear placeholder and state the exact input needed. Do not
present literature claims as verified unless citation work actually verified them.

## Non-goals

Do not fabricate data, citations, experiments, ethics approvals, author contributions,
or journal requirements. Route citation discovery to `article-citation`, final language
editing to `article-polishing`, and reviewer replies to `article-response`.

## Supporting resources

- Read [references/manuscript-outline.md](references/manuscript-outline.md)
  when planning a sectioned manuscript.
- Read [references/section-playbooks.md](references/section-playbooks.md) only for the
  section being drafted.
- Read [references/claim-evidence-audit.md](references/claim-evidence-audit.md) before
  finalizing results, discussion, abstract, or conclusion text.
- Read [references/routing-and-revision.md](references/routing-and-revision.md) for
  axis routing, initial-submission boundaries, alignment gates, and targeted revision.
- Run `python {baseDir}/scripts/check_manuscript_refs.py INPUT.md` to inspect
  figure, table, citation references, and unresolved placeholders.
