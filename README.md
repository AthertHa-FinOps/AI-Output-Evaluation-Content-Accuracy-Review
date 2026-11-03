# AI output evaluation and record-quality review

**Hans Atherton | Stouffville, Ontario | English and Spanish**

In my real estate work, I check agreements, amendments and supporting financial and identity records, identify conflicting information and follow up on corrections before contractual deadlines. This portfolio applies similar source-checking methods to fictional AI responses and administrative records.

## Four examples to review first

| Example | What the source says | Review decision shown in the exercise |
|---|---|---|
| [EV-02: Incorrect total](ai-evaluation/WORKED_EXAMPLES.md) | CAD 141 + CAD 59 | Reject CAD 210; the supported total is CAD 200 |
| [EV-13: Identifier not masked](ai-evaluation/WORKED_EXAMPLES.md) | Fictional ID ZX-00042 must be fully redacted | Reject the unmasked output and require redaction |
| [PAIR-08: Unsupported test results](ai-evaluation/PAIRED_COMPARISONS.md) | Testing has not taken place | Neither response is acceptable because both claim successful execution |
| [EX-006: Processing amount mismatch](back-office-case-study/outputs/exception_register.csv) | Source amount CAD 14,200; export amount CAD 12,400 | Leave the exception open and compare supporting financial records before correction |

These are reference decisions in fictional exercises. The casebook decisions were drafted with AI assistance and have not yet been independently scored by me.

## What is available to inspect

| Work sample | Contents | Current evidence |
|---|---|---|
| [AI-response casebook](ai-evaluation/README.md) | 30 source-based examples covering arithmetic, evidence, privacy, instructions, records and Spanish meaning | 12 ACCEPT, 14 REJECT and 4 INSUFFICIENT_EVIDENCE reference verdicts |
| [Paired-response comparisons](ai-evaluation/PAIRED_COMPARISONS.md) | Ten A/B exercises, including a tie and a neither-acceptable pair | Five A, three B, one TIE and one NEITHER reference preferences |
| [Back-office reconciliation](back-office-case-study/README.md) | Two fictional 14-row datasets, Python reconciliation, an exception register and unit tests | Ten logged exceptions; no source records automatically changed |
| [Earlier document-review notes](case-studies/detailed-evaluation-notes.md) | Examples involving unsupported claims, inconsistent figures, captions and privacy | First-person narrative; original revision evidence is not complete |

The structured evaluation set includes **five Spanish-language cases**; the paired set includes **two Spanish comparisons**.

## Review method

I compare the stated requirement with the supplied source, identify the unsupported or incorrect part of the output, and record the next action. Some errors have a definite correction, such as the arithmetic example. Others require a hold or a request for more evidence, such as a possible duplicate or a claimed deployment without run records.

The [evaluation rubric](ai-evaluation/rubric.md) describes the decision rules. [Worked examples](ai-evaluation/WORKED_EXAMPLES.md) show how the reference decisions apply them. [The recruiter overview](RECRUITER_OVERVIEW.md) provides a shorter path through the evidence.

## Project status

This is **self-directed portfolio work using fictional data**. AI assisted with the evaluation reference cases, comparisons, code and documentation. The [personal-review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) has no completed entries; the reference scores should not be described as my independent annotation results.

The Python reconciliation and casebook-structure checks are run through [GitHub Actions](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml). They check programmed expectations, not the correctness of every natural-language judgment. This repository does not represent paid AI annotation or a deployed customer system.

[Evidence and ownership details](EVIDENCE_AND_OWNERSHIP.md) · [Two-minute walkthrough outline](DEMO_WALKTHROUGH.md) · [Repository audit](PORTFOLIO_AUDIT.md)

Related work: [CRM data quality](https://github.com/AthertHa-FinOps/crm-automation-data-quality-portfolio) · [AWS cost investigation](https://github.com/AthertHa-FinOps/aws-finops-cost-allocation-investigation)
