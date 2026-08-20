# Citation workflow

Use a claim-to-source table with these columns:

`claim_id`, `claim`, `section`, `source_type`, `title`, `year`, `doi`, `url`,
`support_level`, `verification_status`, `support_rationale`, and
`verification_note`.

Use `primary`, `review`, `method`, `dataset`, or `software` for `source_type`.
Use `direct`, `contextual`, or `insufficient` for `support_level`. Use `verified`,
`partial`, or `unverified` for `verification_status`. Keep a source's stable
identifier and do not treat a search snippet as evidence.

The companion validator requires `key`, `title`, `year`, and `source_type`.
It reports duplicate keys, missing required fields, invalid years, malformed DOIs,
and unknown controlled values without changing the input file. It validates a table's
structure, not the truth of its metadata or its support for a claim.
