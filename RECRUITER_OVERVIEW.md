# Evidence map for AI evaluation and document-quality roles

I have 13+ years of paid real estate transaction experience checking agreements and supporting records, finding discrepancies and coordinating corrections. This repository shows how those habits translate to fictional output-evaluation and processing-record exercises. The technical work is self-directed, not paid AI evaluation.

## Start with the records

| Review task | Specific evidence | Decision demonstrated |
|---|---|---|
| Verify calculations | [EV-02](ai-evaluation/WORKED_EXAMPLES.md): source values CAD 141 and CAD 59; answer says CAD 210 | The reference rejects the answer and gives CAD 200 |
| Challenge unsupported system claims | [EV-10](ai-evaluation/WORKED_EXAMPLES.md): workflow export exists; no live run record | Deployment remains unverified until execution evidence is available |
| Apply privacy requirements | [EV-13](ai-evaluation/WORKED_EXAMPLES.md): fictional ZX-00042 must be redacted | The reference rejects the exposed identifier |
| Preserve meaning across languages | [PAIR-09](ai-evaluation/PAIRED_COMPARISONS.md): "El pago está pendiente de aprobación" | Prefer "The payment is awaiting approval," not "was approved" |
| Handle contradictory amounts | [EX-006](back-office-case-study/outputs/exception_register.csv): CAD 14,200 in source, CAD 12,400 in export | Hold the exception for supporting-record verification |
| Avoid unauthorized record deletion | [EX-004](back-office-case-study/outputs/exception_register.csv): two processed rows for CASE-003 | Retain both pending a check of version history |

## What can be reproduced

- [Thirty fictional AI-response cases](ai-evaluation/README.md) with four-dimension scoring rules, evidence and proposed follow-ups
- [Ten paired-response comparisons](ai-evaluation/PAIRED_COMPARISONS.md), including a tie and a case where neither answer is supported
- [Four reconciliation unit tests](back-office-case-study/tests/test_reconcile.py) checking counts, planted defects, unresolved exceptions and normalization on the fictional records
- [GitHub Actions checks](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) for the evaluation schema, relative links and reconciliation outputs

## How to assess this work in an interview

Choose a source record and ask what the evidence permits. For a definite arithmetic error, the next step is a source-backed correction. For a duplicate, an approval status or a deployment claim, the answer may be to preserve the record and request more evidence. The [walkthrough outline](DEMO_WALKTHROUGH.md) links the examples.

**Evidence boundary:** The evaluation verdicts and paired preferences are AI-drafted practice keys, not my completed independent ratings. The [owner-review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) remains blank. The reconciliation is an executed synthetic example, not a live enterprise process.

[Main README](README.md) · [Rubric](ai-evaluation/rubric.md) · [Evidence classification](EVIDENCE_AND_OWNERSHIP.md)
