# AI response accuracy and record-review exercises

**Hans Atherton | English and Spanish | Self-directed portfolio using fictional data**

My paid real estate work involves checking agreements, amendments, financial figures and identity documents, then following up when records conflict. This portfolio uses fictional tasks to demonstrate a related method: compare a proposed answer with its source, identify what is unsupported and document the required correction or hold.

## Start with the source, not the score

| Exercise | What the fictional source establishes | Reference assessment |
|---|---|---|
| [EV-02](ai-evaluation/WORKED_EXAMPLES.md) | CAD 141 + CAD 59 = CAD 200 | Reject the answer claiming CAD 210 |
| [EV-13](ai-evaluation/WORKED_EXAMPLES.md) | Account ID ZX-00042 must be fully redacted | Reject the output exposing the ID |
| [PAIR-08](ai-evaluation/PAIRED_COMPARISONS.md) | No workflow test was run | Neither response is acceptable: both invent completed results |
| [PAIR-09](ai-evaluation/PAIRED_COMPARISONS.md) | Spanish source says a payment awaits approval | Prefer the translation that preserves the pending status |
| [EX-006](back-office-case-study/outputs/exception_register.csv) | Source CAD 14,200; processed extract CAD 12,400 | Leave the discrepancy open for verification |

These are **AI-assisted reference assessments** for fictional examples, not independent ratings I have completed.

## What is available

| Work sample | Inspectable material | Actual verification |
|---|---|---|
| [AI response casebook](ai-evaluation/README.md) | 30 supplied sources, candidate outputs, proposed verdicts, scores and corrections; five Spanish-language cases | Automated schema/consistency checks; **no recorded personal review** |
| [Paired evaluations](ai-evaluation/PAIRED_COMPARISONS.md) | 10 A/B exercises, including two Spanish pairs, one tie and one neither-acceptable pair | Reference preference and rationale; not a measured model comparison |
| [Back-office reconciliation](back-office-case-study/README.md) | Two fictional 14-row files, a Python review, exception register and unit tests | Reproducible checks; 10 open exceptions, no automatic data corrections |
| [Earlier document-review notes](case-studies/detailed-evaluation-notes.md) | Author-attributed account of earlier technical-document errors | Retrospective narrative; complete dated before/after evidence is unavailable |

### What the casebook labels mean

The initial reference set has **12 ACCEPT, 14 REJECT and 4 INSUFFICIENT_EVIDENCE** labels. Those four uncertainty cases contain appropriately cautious candidate answers. The revised data therefore distinguishes **candidate response acceptability** (16 ACCEPT, 14 REJECT) from the older reference category. These are counts of invented exercise labels, **not** accuracy statistics or independent annotator performance. See the [rubric](ai-evaluation/rubric.md).

The [owner-review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) remains blank. The practical next step is a dated independent review of selected cases, recording any disagreement with the reference key rather than replacing the original.

## Reproduce the mechanical checks

From the repository root, with Python 3:

```bash
python ai-evaluation/scripts/validate_examples.py
cd back-office-case-study
python scripts/reconcile.py
python -m unittest discover -s tests -v
```

[GitHub Actions](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) checks the programmatic rules and generated outputs. It **cannot adjudicate whether every language judgment is correct**.

This is an AI-assisted, self-directed exercise, not paid AI annotation, professional model benchmarking or a live customer system. No real client records appear here.

[Recruiter evidence map](RECRUITER_OVERVIEW.md) · [Worked decisions](ai-evaluation/WORKED_EXAMPLES.md) · [Evidence and ownership](EVIDENCE_AND_OWNERSHIP.md) · [Audit limitations](PORTFOLIO_AUDIT.md)
