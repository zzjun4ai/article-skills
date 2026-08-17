# Behavior reference

The normalizer applies rules in this order:

1. Decode the complete input as UTF-8.
2. Split on universal newline boundaries.
3. Trim leading and trailing Unicode whitespace.
4. Remove empty records.
5. Retain only the first exact occurrence of each record.

Comparison is case-sensitive and performs no Unicode normalization. Change these semantics only with matching tests and an explicit user requirement.
