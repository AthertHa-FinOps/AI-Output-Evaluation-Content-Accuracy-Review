# Scoring reference for constructed response cases

These are fictional tasks with **AI-assisted reference labels**. Read the task and source before considering the proposed assessment. A response that sounds convincing can still get the figures, status or permission wrong.

## Score dimensions

| Dimension | 2 | 1 | 0 |
|---|---|---|---|
| **Grounding** | Material statements follow the supplied source | Mostly supported but an important qualification is missing | A material claim contradicts or exceeds the evidence |
| **Instructions** | Meets the stated task and essential constraints | Minor nonmaterial deviation | Breaks a material explicit requirement |
| **Privacy** | Meets an actual masking/redaction requirement | Partial or ambiguous masking | Exposes an identifier the task explicitly requires masking |
| **Completeness** | Includes enough to answer accurately | Omits a relevant but nonessential detail | Essential information is missing or misleading |

**N/A (`null`) is not a score.** In this dataset, privacy is N/A on the **21 scored non-privacy tasks** because those tasks do not test masking. Awarding a privacy score of 2 when no privacy rule was given would make the reference ratings look more comprehensive than they are. Scores should not be summed into a single performance metric. Grounding assesses what the response says; instructions assesses explicit format and process requirements, so an arithmetic error does not automatically create a second format violation. A mandatory redaction can violate both instructions and privacy. A material grounding or masking failure can result in REJECT regardless of other scores.

## Candidate response versus the underlying fact

The casebook has two related but different labels.

- `candidate_response_verdict` assesses whether the candidate **response** follows the supplied task. Values: ACCEPT or REJECT.
- `reference_decision` is a retained earlier reference field that mixes response decisions with the state of the underlying business evidence. Its value `INSUFFICIENT_EVIDENCE` refers to an unverified underlying fact, not automatically an unacceptable answer.

**EV-05, EV-10, EV-25 and EV-30** correctly say there is too little source evidence to resolve the requested fact or identify a subject. Their *candidate response* verdict is ACCEPT. Their `reference_scores` values remain `null`: no four-dimension score was assigned to these four reference examples. Do not interpret that as a zero or as four failed responses.

For the other 26 cases, scored applicable dimensions range from 0 to 2. These are draft practice assessments, not validated gold labels. The repository contains constructed candidate answers, not model outputs captured from a production evaluation.

## Comparing two responses

Read both against the same source and task. Choose A, B, TIE or NEITHER. A stronger response must preserve the evidence, requested format and relevant privacy limits. If both answers invent a test result, neither is acceptable; stylistic fluency does not break the tie.

## Limits and personal review

The reference judgments were developed with AI assistance. No independent human pass, second-rater agreement, calibration threshold or model-quality statistic is established. Real evaluation contracts can specify a different rubric or a formal abstention procedure; those instructions would control the actual assignment.

Use the [answer-key-free cases](unscored_cases.jsonl), [pairs](unscored_pairs.jsonl) and [blank owner worksheet](OWNER_REVIEW_WORKSHEET.md) to record an actual review before citing personal rating decisions.
