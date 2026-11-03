# AI-response evaluation casebook

Thirty fictional source-and-answer cases are organized by issue type, with a proposed verdict, rationale, corrective action and four-dimension rubric where the evidence permits scoring. **The reference decisions were drafted with AI assistance; I have not yet recorded independent personal ratings.**

## Start with a decision

- [EV-02](WORKED_EXAMPLES.md): two source amounts total CAD 200, but the candidate answer says CAD 210
- [EV-10](WORKED_EXAMPLES.md): a workflow export exists without evidence of a live deployment
- [EV-13](WORKED_EXAMPLES.md): a fictional account ID is reproduced despite an explicit redaction requirement
- [EV-22](WORKED_EXAMPLES.md): matching email addresses do not authorize deleting a record
- [PAIR-09](PAIRED_COMPARISONS.md): a Spanish approval status must remain pending in English

The full [casebook](casebook.jsonl) preserves each fictional source, task, candidate output, proposed decision, scoring fields, rationale and follow-up. [Response pairs](pairs.jsonl) provide two alternatives against the same source.

## How to review a case

1. Read the task and fictional source before looking at the reference decision.
2. Check the response against the [rubric](rubric.md) for grounding, instructions, privacy and completeness.
3. Record a supported decision or identify what evidence is missing.
4. Compare your finding with the reference key afterward. Record any disagreement in the [owner worksheet](OWNER_REVIEW_WORKSHEET.md).

## Case inventory

| Category | Cases |
|---|---:|
| Arithmetic and reconciliation | 5 |
| Evidence and deployment claims | 5 |
| Privacy and masking | 5 |
| Instruction-following | 5 |
| Records and identity | 5 |
| Spanish-language meaning | 5 |
| **Total** | **30** |

Reference verdicts: **12 ACCEPT, 14 REJECT, 4 INSUFFICIENT_EVIDENCE**. The ten paired comparisons include **two Spanish-language pairs**.

## Structural verification

From the repository root with Python 3:

```bash
python ai-evaluation/scripts/validate_examples.py
```

The script checks IDs, fields, selected example anchors, score ranges and distribution. It does not determine whether every reference judgment is correct. The [four earlier exploratory examples](evaluation_batch.csv) remain available separately.
