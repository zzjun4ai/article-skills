# Article data contract

Record raw inputs, derived outputs, keys, units, filters, joins, aggregation,
missing-value handling, and the figure or table consuming each output. Keep raw
files immutable and use deterministic output names.

Before delivery, check row counts, column names, duplicate keys, missingness,
numeric ranges, units, and whether every displayed value can be traced back to
an input or documented transformation.

`profile_table.py` is an initial CSV audit, not a substitute for domain
validation or statistical review.
