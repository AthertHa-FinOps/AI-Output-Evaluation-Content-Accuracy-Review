# Evidence map: AI response evaluation and document accuracy

My paid work is in real estate transaction documentation: reviewing agreements and supporting records, identifying mismatched information and coordinating corrections. This repository contains fictional exercises applying those same source-checking habits to AI responses and processing extracts. It is **not** paid AI evaluation experience.

## Four checks to open

| Task | Source-backed example | What the reference identifies |
|---|---|---|
| Arithmetic accuracy | [EV-02](ai-evaluation/WORKED_EXAMPLES.md): CAD 141 + CAD 59 | CAD 210 is wrong; the total is CAD 200 |
| Information masking | [EV-13](ai-evaluation/WORKED_EXAMPLES.md): redact ZX-00042 | Exposing the ID violates the explicit redaction rule |
| Bilingual meaning | [PAIR-09](ai-evaluation/PAIRED_COMPARISONS.md): Spanish payment pending approval | An English output saying "approved" reverses the status |
| Document reconciliation | [EX-006](back-office-case-study/outputs/exception_register.csv): CAD 14,200 versus CAD 12,400 | Preserve the discrepancy and request authoritative evidence |

Additional exercises address missing test evidence ([PAIR-08](ai-evaluation/PAIRED_COMPARISONS.md)), uncertain deployment claims ([EV-10](ai-evaluation/WORKED_EXAMPLES.md)) and possible duplicate records ([EV-22](ai-evaluation/WORKED_EXAMPLES.md)).

## What can be repeated

- [Thirty fictional cases](ai-evaluation/README.md) with explicit source, candidate output, proposed response verdict and dimension scores where applicable
- [Ten paired comparisons](ai-evaluation/PAIRED_COMPARISONS.md), including two Spanish examples, one tie and one case where neither answer is defensible
- [Processing-record checks](back-office-case-study/README.md) with 14 source and 14 export rows, 10 open exceptions and automated tests
- [Automated verification](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) of data schemas, anchored examples, internal links and synthetic reconciliation outputs

**How to interview me on this work:** Select a case without showing the reference answer. Ask which statement is supported, what needs correcting and what evidence would change the decision.

The current reference judgments were AI-drafted, and the [independent owner-review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) is blank. The reconciliation is runnable on fictional data. Neither is a verified annotation contract, calibrated evaluation metric or production system.

[Portfolio overview](README.md) · [Rubric](ai-evaluation/rubric.md) · [Evidence classification](EVIDENCE_AND_OWNERSHIP.md)
