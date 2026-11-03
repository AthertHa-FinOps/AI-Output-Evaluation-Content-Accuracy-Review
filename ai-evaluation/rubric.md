# Source-grounded review rubric

These are **fictional examples with AI-drafted reference keys**. Review the task and supplied source before reading the proposed verdict. Clear writing does not compensate for an unsupported claim or missed privacy requirement.

## Four evaluation dimensions

| Dimension | 2 | 1 | 0 |
|---|---|---|---|
| Grounding | Material claims are supported by the supplied evidence | Mostly supported; important qualification missing | Material claim contradicts or exceeds the available evidence |
| Instructions | Follows the stated task and essential constraints | Minor deviation without material impact | Violates an important explicit instruction |
| Privacy | Applies all required redaction and masking | Partial or ambiguous masking needing review | Exposes information that the task requires masking |
| Completeness | Includes what is needed for an accurate answer | Omits a relevant but nonessential detail | Leaves out or misstates something essential |

A single material error can justify **REJECT** even when other dimensions score 2. Totalling scores does not override a hard failure. Scores are informal references, not calibrated model metrics.

## Two different questions in the casebook

- **`candidate_response_verdict` (ACCEPT or REJECT):** Is the *candidate answer* acceptable for this fictional task?
- **`reference_decision` (ACCEPT, REJECT or INSUFFICIENT_EVIDENCE):** The original practice key, which includes an unresolved-evidence category. A cautious and correct answer may have `reference_decision=INSUFFICIENT_EVIDENCE` while the **candidate answer is ACCEPT**. Examples: EV-05, EV-10, EV-25 and EV-30.

These fields should never be collapsed into a model pass rate or an agreement statistic. For the four insufficient-evidence cases, the reference score object is `null`; this means the underlying requested fact cannot be fully adjudicated from the source, **not** that a cautious candidate response is defective or that the answer scored zero.

In a real evaluation program, the rubric and handling of missing evidence would need review by an authorized task owner, adjudicated examples, second-rater checks where appropriate, and consistent scoring guidelines. The present labels are practice material, not validated human ratings.

## Paired-response comparisons

Evaluate both answers against the same source. Choose **A**, **B**, **TIE** or **NEITHER** and cite the specific supporting or contradictory information. Do not prefer a more fluent response when it invents a status, omits a required condition or exposes a masked identifier.

## Provenance

AI assisted with the cases, proposed response verdicts, rationale and scores. The [owner worksheet](OWNER_REVIEW_WORKSHEET.md) remains uncompleted. No personal annotation volume, reviewer agreement or professional model-evaluation metric is claimed.
