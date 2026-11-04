# AI response evaluation | English and Spanish

**Hans Atherton · Stouffville, Ontario, Canada · English / Spanish · [LinkedIn](https://www.linkedin.com/in/hans-atherton-82638234/)**

**Relevant roles:** AI Response Evaluator, LLM Text Annotator, Bilingual AI Evaluator, Content Accuracy Reviewer, and document-quality / back-office QA.

This repository demonstrates how to compare a response with its supplied source, apply defined scoring rules, and explain a correction or an evidence limit. Its AI-response examples and proposed ratings were constructed with AI assistance. **They are not captured model outputs or independent ratings I completed.**

## Start with three examples

| Example | Evidence to inspect | What it illustrates |
|---|---|---|
| [EV-04 — missing adjustment](ai-evaluation/WORKED_EXAMPLES.md) | Source amounts CAD 90 and CAD 10; fictional answer says CAD 90 | A plausible response can omit a component and give the wrong total of CAD 100 |
| [PAIR-09 — approval still pending](ai-evaluation/PAIRED_COMPARISONS.md) | *El pago está pendiente de aprobación* | A translation must preserve pending approval rather than claim approval happened |
| [EX-006 — record discrepancy](back-office-case-study/README.md) | Source CAD 14,200 versus processing export CAD 12,400 | A Python reconciliation flags a mismatch without altering either input |

EV-04 and PAIR-09 are **AI-assisted reference decisions**. EX-006 is an exception from a **fictional dataset processed by the repository script**, not a real customer case. These examples illustrate the review method; they do not establish personal annotation accuracy.

## Inspect the work

| Material | Contents and status |
|---|---|
| [Individual response exercises](ai-evaluation/README.md) | 30 fictional source/response cases with proposed reference ratings |
| [A/B comparisons](ai-evaluation/PAIRED_COMPARISONS.md) | Ten fictional pairs, including Spanish-source examples, a tie, and a neither-acceptable outcome |
| [Rubric](ai-evaluation/rubric.md) | Source grounding, instructions, privacy and completeness; distinguishes insufficient underlying evidence from a failed response |
| [Additional practice](ai-evaluation/practice/README.md) | Eight individual exercises and four pairs with **no supplied ratings** |
| [Record reconciliation](back-office-case-study/README.md) | Two fictional 14-row files; ten open exceptions; six automated unit tests |
| [Recruiter role guide](RECRUITER_OVERVIEW.md) | Examples matched to potential junior/contract roles and documented limitations |

## Paid experience behind the method

In my paid real estate work since 2012, I review legally binding agreements, amendments, identification and financial documents, investigate inconsistent information, and coordinate clarification with clients, lawyers, lenders and other parties. Earlier, at **HOOPP (2005–2008)**, I audited pension accounts and recalculated benefits during migration-related defect-remediation projects. These are relevant document and financial-record review duties, **not paid AI annotation**.

## Independent-review progress

The [personal review record](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) has **no completed first-pass ratings**. There are no recorded runs of named models, independent reviewer-agreement metrics or paid annotation assignments in this repository.

The next evidence-building step is the [six-review practice plan](ai-evaluation/INDEPENDENT_REVIEW_SPRINT.md). It identifies specific unscored exercises and how to preserve first decisions without inventing results. The [real-model capture protocol](ai-evaluation/REAL_OUTPUT_REVIEW_PROTOCOL.md) is available for future permitted runs; the corresponding log is empty.

[Evidence and authorship](EVIDENCE_AND_OWNERSHIP.md) · [Technical checks and limits](PORTFOLIO_AUDIT.md) · [Two-minute walkthrough outline](DEMO_WALKTHROUGH.md)

<details>
<summary>Reproduce the automated checks</summary>

From the repository root with Python 3:

```bash
python ai-evaluation/scripts/validate_examples.py
python ai-evaluation/scripts/prepare_review_inputs.py --check
python ai-evaluation/scripts/validate_practice.py
python ai-evaluation/scripts/check_links.py
cd back-office-case-study
python -m unittest discover -s tests -v
python scripts/reconcile.py
```

[GitHub Actions](.github/workflows/portfolio-checks.yml) checks data structure, selected reference rules, internal links, and synthetic reconciliation outputs. Passing tests does not validate every subjective reference judgment or establish personal evaluator performance.

</details>
