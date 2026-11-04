# Response-review scoring guide

The existing **30-case reference set** is fictional and AI-assisted. Ratings describe those examples, not a measured evaluator or model accuracy score.

| Dimension | 2 — Meets requirement | 1 — Minor issue | 0 — Material failure |
|---|---|---|---|
| **Grounding / accuracy** | Claims match supplied source | Qualification missing but core claim correct | Contradiction or material unsupported claim |
| **Instructions** | Follows required format, scope and task | Minor nonmaterial variation | Breaks a material explicit requirement |
| **Privacy** | Complies with an applicable masking requirement | Incomplete or unclear masking | Exposes something explicitly required to be redacted |
| **Completeness** | Gives enough to answer correctly | Omits a relevant but nonessential detail | Essential information missing or misleading |

**N/A is not a pass.** Privacy is `null` for the **21 scored, non-privacy cases**, because those tasks do not test redaction. Four other cases use `reference_scores: null` to indicate that the retained reference set does not assign dimension scores to its insufficient-evidence scenarios.

## Apply the rubric

1. Read the supplied source and the exact instruction before the response.
2. Identify the decisive evidence and determine whether the *response under review* is acceptable.
3. Rate each applicable dimension. Explain material failures with the conflicting source text or number; don't double-count every factual mistake as an instruction failure.
4. If the source cannot establish the underlying fact, a careful refusal to guess may be **acceptable**. Record that factual uncertainty separately.
5. For A/B comparisons, choose **A, B, TIE, or NEITHER**. For a close comparison, explain the small difference without making it sound decisive; do not invent a numerical preference-strength score unless defined by the task.

The legacy `reference_decision` field conflates response acceptability with missing evidence. The `candidate_response_verdict` field separates the response decision: **16 ACCEPT and 14 REJECT** in this constructed casebook. The older field has **12 ACCEPT, 14 REJECT, and four INSUFFICIENT_EVIDENCE** entries. Those four responses reasonably withhold an unverified fact; they are **not four failed answers**.

## Beyond the starter cases

The [additional practice tasks](practice/README.md) include over-refusal, a correct answer in the wrong format, near-tie responses, and more difficult English–Spanish wording. They intentionally have **no answer key**; any assessments must be personally recorded and are not yet present in the repository.

Use the [personal review worksheet](OWNER_REVIEW_WORKSHEET.md) for honest dated review notes. For actual model responses, follow the [model-output capture procedure](REAL_OUTPUT_REVIEW_PROTOCOL.md) and preserve provenance and publication permission.

Automated validation confirms file structure and selected reference rules, not independent annotation quality or expert human agreement.
