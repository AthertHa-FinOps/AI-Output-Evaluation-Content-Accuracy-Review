# AI response checking | English and Spanish

**Hans Atherton | Stouffville, Ontario | Self-directed work sample**

In real estate transactions, I check agreements and supporting records for conflicting figures, missing details and statements that need correction. This portfolio applies those checks to **constructed fictional responses**. The examples are not captured outputs from a deployed model or client assignments.

## Inspect a source and the proposed judgment

| Case | Evidence in the exercise | Issue to decide |
|---|---|---|
| [EV-04](ai-evaluation/README.md) | Approved adjustments of CAD 90 and CAD 10 | The candidate reports CAD 90, leaving out CAD 10 |
| [EV-10](ai-evaluation/WORKED_EXAMPLES.md) | A workflow export exists, but no run record | A cautious response is acceptable; deployment is unverified |
| [EV-13](ai-evaluation/WORKED_EXAMPLES.md) | An account identifier must be fully redacted | The candidate exposes the identifier |
| [EV-27](ai-evaluation/README.md) | Spanish source: *El pago fue rechazado* | An English answer incorrectly says the payment was approved |
| [PAIR-08](ai-evaluation/PAIRED_COMPARISONS.md) | No test was executed | Neither answer is acceptable because both claim results |

These decisions are **AI-assisted reference examples**, not my completed independent ratings.

## Evidence you can inspect

| Component | Included | Verification boundary |
|---|---|---|
| [Individual responses](ai-evaluation/README.md) | 30 source/task/output cases and a [rubric](ai-evaluation/rubric.md) | Constructed examples; reference labels have not been personally adjudicated |
| [Response comparisons](ai-evaluation/PAIRED_COMPARISONS.md) | Ten A/B pairs, including two Spanish-source comparisons | Not actual head-to-head model results |
| [Document reconciliation](back-office-case-study/README.md) | Fictional 14-row source and export, Python script, ten open exceptions | Reproducible local exercise, not employer records |
| [Earlier review notes](case-studies/detailed-evaluation-notes.md) | Retrospective technical-document examples | Full dated before/after evidence is not available |

**To review without the answer key:** [individual prompts](ai-evaluation/unscored_cases.jsonl) · [A/B prompts](ai-evaluation/unscored_pairs.jsonl) · [blank personal review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md).

The original reference labels include four `INSUFFICIENT_EVIDENCE` cases whose **candidate answers appropriately refuse to guess**. Privacy scores are marked **N/A** when no privacy rule is tested. These are invented practice labels, not a model's accuracy or an annotator agreement rate.

## Reproduce the checks

```bash
python ai-evaluation/scripts/validate_examples.py
python ai-evaluation/scripts/prepare_review_inputs.py --check
cd back-office-case-study
python -m unittest discover -s tests -v
python scripts/reconcile.py
```

[GitHub Actions](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) checks schemas, reference-free inputs, reconciliation tests and committed outputs. It cannot establish the correctness of every language judgment.

I used AI assistance for case construction, reference ratings, code and documentation. This is not paid annotation, a calibrated benchmark or a production system. My independent ratings have **not yet been recorded**.

[Recruiter overview](RECRUITER_OVERVIEW.md) · [Evidence boundaries](EVIDENCE_AND_OWNERSHIP.md) · [Audit and outstanding work](PORTFOLIO_AUDIT.md)
