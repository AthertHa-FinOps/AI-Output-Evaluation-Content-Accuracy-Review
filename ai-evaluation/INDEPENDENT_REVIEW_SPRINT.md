# Six independent review exercises — completion guide

**Status: Not completed.** This guide names six existing fictional practice tasks and explains how to record your own first-pass decisions. It contains **no grades, proposed answers, rationales, dates or statements that these reviews have been performed**.

The source exercises were constructed with AI assistance, and the repository has other solved examples. Even if you have not seen a particular reference answer, this is **practice with prepared questions, not a blind external model evaluation**.

## Review these six items

| Review order | Case ID | Type | What to evaluate |
|---:|---|---|---|
| 1 | ADV-01 | Individual | Preserve conditions and pending approval when translating a customer notice |
| 2 | ADV-02 | Individual | Apply Chilean context to regional vocabulary |
| 3 | ADV-03 | Individual | Preserve formal Spanish address and the client's actual status |
| 4 | ADV-08 | Individual | Preserve documentary verification requirements and non-confirmation |
| 5 | ADV-PAIR-01 | A/B | Assess nuanced tone and meaning in a business-email translation |
| 6 | ADV-PAIR-03 | A/B | Assess a formal Spanish response and the consequence of nonresponse |

The questions and constructed responses are in [practice/cases.jsonl](practice/cases.jsonl) and [practice/pairs.jsonl](practice/pairs.jsonl). The [practice guide](practice/README.md) gives the procedure; it does **not** contain answer keys. Use the [scoring rubric](rubric.md) for applicable dimensions.

## How to record a genuine first decision

1. Open one source and its task instruction. Read the constructed response as it appears. Do not request or consult an AI-produced answer or explanation first.
2. For an individual case, record ACCEPT or REJECT and relevant grounding, instruction, privacy and completeness scores. Mark a dimension N/A only when it is not applicable. For a pair, record A, B, TIE or NEITHER.
3. Quote the decisive source detail and write a short explanation of the decision. Write **at least two original explanations in Spanish** for Spanish-source or Spanish-output tasks, including any relevant register or regional distinction.
4. Record your **actual date** and initial decision in the corresponding row of [owner_review_log_template.csv](owner_review_log_template.csv). Save the first judgment before consulting anything else.
5. After saving, optionally check the facts, reconsider the decision, or compare it with an outside review. Keep the initial decision and any subsequent correction in separate fields. Never replace the original record silently.
6. Complete only the six selected rows initially. The remaining prepared rows can stay blank. Do not compute an “accuracy,” calibration or reviewer-agreement percentage from these practice tasks.

## Additional evidence beyond constructed exercises

For stronger proof of evaluation work, use [REAL_OUTPUT_REVIEW_PROTOCOL.md](REAL_OUTPUT_REVIEW_PROTOCOL.md) to capture three or four **actual responses from a named model** to permitted fictional or public-domain tasks. Record the model identifier, prompt, unchanged response, timestamp and your original judgment **before** seeking an AI assessment.

No live-model runs or individual ratings are currently recorded. Do not represent prepared forms, reference examples or protocol steps as completed results.

## Publishing a completed example

When a review has actually been performed, a recruiter-facing example should link to:

- The source, instruction and response as reviewed.
- Your dated first decision and specific supporting evidence.
- Your original rationale, including Spanish text where applicable.
- Any later correction, disagreement or limitation, clearly separated.

Only then update [../README.md](../README.md) and [../RECRUITER_OVERVIEW.md](../RECRUITER_OVERVIEW.md) to feature that review as personally completed work. Avoid inventing a reviewer, score or completion date.
