# Source-based AI response exercises

The original set has **30 fictional single-response cases** and **10 fictional A/B comparisons**. Each task supplies its own source, instruction and response, followed by an AI-assisted reference rating or pair preference. The responses were made for this exercise, not captured from named models.

[Single-response casebook](casebook.jsonl) · [A/B pairs with proposed ratings](pairs.jsonl) · [Scoring guide](rubric.md) · [Selected worked examples](WORKED_EXAMPLES.md)

## Where the cases focus

| Case | Question to check |
|---|---|
| EV-04 | Does the amount include both approved adjustments (CAD 90 + CAD 10)? |
| EV-10 | Does an export alone prove a workflow was deployed? |
| EV-13 | Was an account identifier fully redacted as requested? |
| EV-19 | Does the response claim a reconciliation result not present in the source? |
| EV-22 | Can a shared email justify deleting a contact? |
| EV-27 | Does *rechazado* preserve the rejected-payment status? |
| PAIR-09 | Does *pendiente de aprobación* remain conditional? |

There are five Spanish-source single responses and two Spanish-source pairs. Their responses are in English. The [more challenging practice questions](practice/README.md) add Spanish-language responses, formal register, Chilean regional usage and closer A/B comparisons, but contain **no ratings**.

## Review process

For existing cases, use the [rating-hidden inputs](unscored_cases.jsonl) and [rating-hidden pairs](unscored_pairs.jsonl). For each response, record the first judgment, decisive source detail, applicable dimension scores and actual date in the [personal review log](owner_review_log_template.csv). Then compare the first judgment with the AI-assisted reference and note any disagreement. Previously seen keys make the exercise reference-hidden, not truly blind.

For independent evidence on real model outputs, follow the [capture procedure](REAL_OUTPUT_REVIEW_PROTOCOL.md). No such runs or personal results have been recorded.

## Technical checks

The [data validator](scripts/validate_examples.py) checks record structure, selected score rules and the retained reference counts (**16 response ACCEPT / 14 REJECT**). Four cautious answers have a legacy `reference_decision` of `INSUFFICIENT_EVIDENCE`; those are not response failures. [Practice-data validation](scripts/validate_practice.py) checks the additional unscored material and templates. Neither script validates expert judgment.
