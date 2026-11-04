# AI response evaluation | English and Spanish

**Hans Atherton · Stouffville, Ontario, Canada · English / Spanish · [LinkedIn](https://www.linkedin.com/in/hans-atherton-82638234/)**

**Target roles:** AI Response Evaluator, LLM Text Annotator, Bilingual AI Evaluator, and Content Accuracy Reviewer. The record-review sample also supports document-quality and back-office QA applications.

This portfolio uses short, fictional response-review tasks: check an answer against a supplied source, apply a defined rating rule, and explain a correction or a decision to withhold judgment. The responses and reference ratings were developed with AI assistance; they are **not captured model outputs or my independently completed ratings**.

## One response, checked against its source

**EV-04 — approved adjustments** · [full reference example](ai-evaluation/WORKED_EXAMPLES.md)

| Source and task | Response under review | Reference rating |
|---|---|---|
| Approved adjustments: **CAD 90 + CAD 10**. Report their combined amount. | “Approved adjustment: CAD 90.” | **Reject** — grounding 0/2; instructions 2/2; completeness 0/2; privacy N/A |

**Reason:** The source contains two approved amounts totaling **CAD 100**. The response reports only CAD 90, so the total is wrong and one adjustment is omitted. It needs a corrected total, not an invented change to either source amount.

*This worked rating is from the AI-assisted reference set, not a personal evaluation result.*

For bilingual review, see [PAIR-09](ai-evaluation/PAIRED_COMPARISONS.md): *El pago está pendiente de aprobación* must not be reported as already approved.

## Portfolio samples

| Review work | What to open |
|---|---|
| **30 single-response exercises** | [Source, response, and proposed ratings](ai-evaluation/README.md) · [Scoring rules](ai-evaluation/rubric.md) |
| **10 A/B comparisons** | [Pair decisions](ai-evaluation/PAIRED_COMPARISONS.md), including two Spanish-source pairs, a tie, and a case where neither answer is acceptable |
| **More difficult practice** | [Unscored exercises](ai-evaluation/practice/README.md) covering Spanish register and regional usage, format adherence, unnecessary refusals, and close A/B calls |
| **Supporting record-quality work** | [Fictional processing reconciliation](back-office-case-study/README.md): two 14-row files, ten open exceptions, and automated tests |

## Relevant experience

In paid real estate work, I review agreements, amendments, identity documents, and financial records, and follow up when source documents disagree. Earlier, as a **Project Associate / Analyst (Contract)** in HOOPP's QRM area (June 2005–June 2008), I checked pension accounts and calculations during successive system defect-remediation projects. Those are document-review and reconciliation responsibilities, **not paid AI annotation**.

## Scope

The 30 ratings and ten pair preferences are **AI-assisted references**. No independent first-pass ratings, professional agreement scores, or live model-output benchmark are recorded. I have not completed the [personal review record](ai-evaluation/OWNER_REVIEW_WORKSHEET.md). A [capture protocol](ai-evaluation/REAL_OUTPUT_REVIEW_PROTOCOL.md) is provided for future permitted evaluations of actual model responses; it does not represent completed work.

[Recruiter role guide](RECRUITER_OVERVIEW.md) · [Evaluation examples](ai-evaluation/WORKED_EXAMPLES.md) · [Tests and limitations](PORTFOLIO_AUDIT.md)

<details>
<summary>Reproduce the repository checks</summary>

From the repository root, with Python 3:

```bash
python ai-evaluation/scripts/validate_examples.py
python ai-evaluation/scripts/prepare_review_inputs.py --check
python ai-evaluation/scripts/validate_practice.py
cd back-office-case-study
python -m unittest discover -s tests -v
python scripts/reconcile.py
```

[GitHub Actions](.github/workflows/portfolio-checks.yml) checks the files, selected reference rules and reconciliation outputs. It does not determine whether every reference judgment is correct.

</details>
