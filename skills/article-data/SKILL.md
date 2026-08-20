---
name: article-data
description: >-
  Prepare, audit, and document scientific data and data-sharing materials for
  manuscripts. Use for figure or table source data, supplementary datasets,
  provenance and transformation records, Data Availability or code-availability
  statements, repository and identifier planning, FAIR metadata checks, and
  requests such as 数据可用性声明、数据共享、数据仓库选择 or 源数据整理. Do not
  replace domain-specific statistical analysis or alter raw data in place.
---

# Article Data

Build a reviewable data package and an accurate data-availability account.

## Route the request

- `source-data-package` — profile, transform, and link data to figures or tables.
- `availability-statement` — inventory supporting datasets, classify access routes,
  and draft ready-to-paste data/code availability text.
- `data-audit` — inspect an existing package for provenance, identifiers, metadata,
  and reproducibility gaps without altering the data.

## Shortest successful workflow

1. Identify the target journal or repository requirements and inventory every dataset
   supporting a result, including reused, restricted, third-party, and code outputs.
2. Classify each dataset into an access route using
   [references/data-availability.md](references/data-availability.md).
3. Choose a repository and identifier strategy with
   [references/repository-selection.md](references/repository-selection.md). Record
   `planned`, `pending`, and `complete` deposits separately; a planned DOI is not a DOI.
4. Preserve raw inputs. For tabular data, run `profile_table.py`; create derived files
   with deterministic names and record filters, joins, transformations, exclusions,
   units, replicate definitions, and aggregation.
5. Link every figure and table to exact source and derived files. Record repository,
   persistent identifier, licence, embargo, and restrictions only when verified.
6. Validate the data manifest, then draft the statement or package index. List every
   unresolved field instead of filling it with plausible text.

## Output contract

For source-data work, return derived data, a data dictionary, and a manifest mapping
raw inputs through transformations to figures/tables. For availability work, return
the statement, dataset-to-location table, formal dataset citations where available,
and unresolved fields. Distinguish planned deposits from completed deposits.

## Failure behavior

Stop before final claims when identifiers, units, joins, licences, access conditions,
or repository deposits are ambiguous. Never invent accession numbers, DOIs, ethics
approvals, access committees, licences, embargo dates, or repository names.

## Non-goals

Do not silently impute, delete, overwrite, reinterpret, or disclose restricted data.
Do not use “available upon request” as a default when a repository or explicit access
route is appropriate.

## Supporting resources

- Read [references/data-contract.md](references/data-contract.md) before
  preparing a figure or table data package.
- Read [references/data-availability.md](references/data-availability.md) before
  drafting an availability statement or repository plan.
- Read [references/repository-selection.md](references/repository-selection.md) before
  choosing a repository, accession/DOI route, embargo, or controlled-access wording.
- Run `python {baseDir}/scripts/profile_table.py INPUT.csv` for a deterministic
  CSV profile.
- Run `python {baseDir}/scripts/validate_data_manifest.py MANIFEST.json` before
  delivering a data package or availability statement.
