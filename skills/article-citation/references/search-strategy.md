# Claim Search Strategy

Convert each atomic claim into five fields before searching:

- `entity`: organism, population, molecule, method, dataset, or system;
- `relationship`: associates, predicts, regulates, causes, improves, or measures;
- `outcome`: the reported effect or property;
- `context`: tissue, disease, condition, geography, device, or time period; and
- `boundary`: species, population, intervention, dose, comparator, or other limit.

Generate a precise query, a synonym/abbreviation query, and a broader fallback query.
For Chinese prose, translate scientific concepts rather than the sentence word for
word, and preserve standard nomenclature and acronyms.

Grade candidate evidence conservatively:

- `direct`: tests the same relationship in a sufficiently similar context;
- `partial`: supports only one component or a narrower context;
- `background`: establishes field context but not the focal relationship;
- `contradictory`: conflicts with or materially narrows the claim;
- `metadata-only`: identity or relevance has not been checked beyond metadata.

Record the evidence basis used for the grade: abstract, full text, publisher page, or
verified data record. A title, search snippet, citation count, or journal prestige does
not establish support. If the best source is only partial, narrow the manuscript claim
or mark the gap instead of upgrading the source.

For more than about ten claims, process stable claim IDs in batches. Deduplicate by DOI
or another stable identifier after every batch and preserve rejected candidates and
their rejection reasons so later batches do not reintroduce them.

