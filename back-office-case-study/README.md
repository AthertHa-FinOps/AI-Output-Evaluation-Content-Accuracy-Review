# Back-office reconciliation and exception management

**Fictional records | AI-assisted work sample | Not a client project**

The task is to compare an administrative processing export with source cases and report discrepancies rather than silently fix them. Both inputs contain 14 rows, but row-count agreement does not establish record agreement.

## Business rules

- Match on trimmed, uppercase case IDs but preserve original identifiers.
- Find source cases missing in the export, export cases without a source and duplicate processing.
- Compare customer references, document type, amount and required-document status.
- Never guess monetary corrections, invent missing documents or delete/merge records automatically.
- Preserve each finding with source evidence, observed value, severity and a suggested follow-up.

## Artifacts

| Artifact | Location |
|---|---|
| Fictional source records | [data/source_records.csv](data/source_records.csv) |
| Fictional processing export | [data/processing_export.csv](data/processing_export.csv) |
| Python 3 script | [scripts/reconcile.py](scripts/reconcile.py) |
| Four unit tests | [tests/test_reconcile.py](tests/test_reconcile.py) |
| Exception register | [outputs/exception_register.csv](outputs/exception_register.csv) |
| Control totals | [outputs/control_summary.md](outputs/control_summary.md) |

## Reproduce

~~~shell
python scripts/reconcile.py
python -m unittest discover -s tests -v
~~~

Python standard library only. The script regenerates the output files.

## Sample result and decision limits

Source and processing counts are both **14**, but the export has **13 distinct case IDs** and the checks identify **10 exceptions**. Two source cases are absent from processing, one processed case lacks a source, a case is duplicated, and other records contain missing or contradictory information.

Every exception remains **OPEN - review required**. A duplicate might be a legitimate amendment; an unmatched processed record might come from another intake system; a wrong amount needs supporting documents. No automatic correction is presented as a completed transaction.

AI assisted code and text drafting. The repository states its review rules, provides the planted synthetic defects and includes four automated tests that check the expected outputs; those tests passed on the published CI workflow. This supports only a small designed example, not paid programming, current securities/insurance operations, production control systems or real-world error-rate claims.
