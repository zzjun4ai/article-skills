# Meaning-preservation rules

Treat these as protected unless the user explicitly authorizes a scientific change:

- numbers, signs, ranges, percentages, units, sample sizes, p-values, and effect sizes;
- equations, chemical formulas, gene/protein names, abbreviations, and identifiers;
- LaTeX citation keys, labels, references, commands, and math spans;
- direction of effects, comparison groups, causal versus correlational wording;
- hedging and scope terms such as `may`, `suggests`, `in this cohort`, and `under these conditions`.

If the source appears factually inconsistent, flag it rather than silently repairing it.
Machine token comparison catches only deterministic differences; the final semantic
read-back must still check claim strength and logical relationships.
