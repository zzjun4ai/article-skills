# Verification and support

Assess source identity and claim support separately.

## Metadata verification

- `verified` — a DOI, PMID, arXiv ID, or publisher record resolves and core metadata
  agree.
- `partial` — two independent scholarly metadata records agree, but no authoritative
  identifier or publisher record was checked.
- `unverified` — identity is ambiguous, metadata conflict, or the source cannot be
  inspected. Exclude it from the final bibliography unless the user explicitly asks
  for an unresolved candidate list.

## Claim support

- `direct` — the inspected source directly studies or establishes the claim.
- `contextual` — it supports background, framing, or a neighboring proposition but
  not the exact claim.
- `insufficient` — title-level similarity, contradictory evidence, or no accessible
  abstract/full text. Do not cite as support.

Store a one-sentence support rationale tied to the inspected abstract, result, method,
or source passage. Do not infer support from venue prestige or citation count.
