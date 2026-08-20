# Whole-Manuscript Consistency Sweep

Use this after passage-level editing when the input is a full manuscript or has passed
through multiple revisions. Work from a terminology ledger and scan the entire document,
not only changed paragraphs.

Check:

- one canonical form for each method, model, cohort, dataset, metric, abbreviation,
  symbol, and capitalization pattern;
- units, denominators, sample sizes, group labels, and replicate definitions;
- numerical precision and rounding for the same quantity across prose, tables, and
  legends;
- abstract, Results, Discussion, figures, and conclusions for conflicting headline
  counts or effect directions;
- claim strength against the manuscript's own tables and uncertainty displays;
- citation keys, figure/table references, equation labels, and LaTeX commands; and
- tense and voice only where inconsistency obscures chronology or responsibility.

Classify every difference as intentional, corrected, or `AUTHOR_INPUT_NEEDED`. Do not
normalize a scientifically meaningful distinction merely because two terms look
similar. After changes, rerun the protected-token comparison and repeat the sweep until
no new cross-document drift is found.

