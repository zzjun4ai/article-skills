# Revision Package Consistency

Treat the decision letter, internal tracker, reviewer-specific responses, clean
manuscript, marked manuscript, figures/supplements, and cover letter as one package.

Before delivery:

1. Pair every preserved comment with exactly one direct response and stable internal ID.
2. Match each `completed` claim to inspectable revised text, analysis, figure, table, or
   supplement. Otherwise use `reported-unverified`, `planned`, or
   `AUTHOR_INPUT_NEEDED`.
3. Verify every quoted revised passage verbatim against the latest manuscript and every
   location against the latest pagination or line numbering.
4. Confirm that clean and marked manuscripts differ only by intended changes and that
   deleted text is represented consistently.
5. Keep the internal master private. Each reviewer-facing file contains only that
   reviewer's comments and responses unless the journal explicitly requires a combined
   document.
6. Recheck terminology, numbers, units, figure/table references, citations, and the
   response letter after any manuscript edit.

Any manuscript edit invalidates prior quote and location checks. Repeat the package
audit rather than treating it as a one-time final step. Return `ready`,
`draft-with-placeholders`, `needs-author-input`, or `blocked` from the item-level state;
do not label an unresolved package ready.

