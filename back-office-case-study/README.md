# Back-office record reconciliation

This exercise compares a fictional processing export with a fictional source register. It checks whether the same cases are present and whether customer references, amounts and documents agree. Matching row counts are not enough.

## Results

| Control | Result |
|---|---:|
| Source rows | 14 |
| Processing rows | 14 |
| Distinct processed case IDs | 13 |
| Logged exceptions | 10 |

The [exception register](outputs/exception_register.csv) retains the original discrepancies. For example:

- **EX-006 / CASE-006:** The source amount is CAD 14,200; the processed amount is CAD 12,400. The amount remains unresolved until supporting records are checked.
- **EX-004 / CASE-003:** One source case has two processing entries. Both remain on hold until the history establishes whether the second is a duplicate or a legitimate version.
- **EX-001 / CASE-011:** A source case has no processing entry. The proposed follow-up is to check the queue or transmission history, not invent a processed record.

All ten findings have the disposition **OPEN - review required**. No source row is deleted or corrected automatically.

## Checks used

- Normalize case IDs for matching while preserving the original values; stop with an explicit error if source IDs are blank or collide after normalization.
- Find missing source cases, processed cases without a source and repeated processing IDs.
- Compare amounts, document types, customer references and received-document status.
- Record the issue, observed value, severity and next step without assuming authorization to change a record.

## Files

| Artifact | Link |
|---|---|
| Source cases | [source_records.csv](data/source_records.csv) |
| Processing export | [processing_export.csv](data/processing_export.csv) |
| Reconciliation script | [reconcile.py](scripts/reconcile.py) |
| Six unit tests | [test_reconcile.py](tests/test_reconcile.py) |
| Exception register | [exception_register.csv](outputs/exception_register.csv) |
| Control summary | [control_summary.md](outputs/control_summary.md) |

## Reproduce the checks

From this folder, with Python 3 (standard library only):

```bash
python scripts/reconcile.py
python -m unittest discover -s tests -v
```

The six unit tests check expected counts, planted defects, unresolved status, normalization, and whether duplicate or blank source case IDs are rejected rather than silently replaced. The [published CI workflow](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) runs the same sample checks.

**Scope:** The records and defects are deliberately fictional. AI assisted with the code and documentation. The tests verify this defined exercise, not a live processing system.
