# Response matrix

Use one row per atomic comment with `comment_id`, `comment`, `status`,
`response`, `location`, and optional `evidence_status`. Recommended statuses are
`accepted`, `partial`, `clarified`, `disputed`, and `author-input-needed`.
Evidence states are `verified`, `author-input-needed`, and `not-applicable`.

The checker treats an empty response or location as incomplete unless status is
`author-input-needed`. It checks coverage and structure only; authors must still verify
that claimed revisions exist in the manuscript.
