# Structured evaluation exercise — 30 source-grounded cases

This is a **reference exercise generated with AI assistance**, not a record of thirty independently adjudicated assignments. Its purpose is to make the verification standard inspectable and to support later personal review.

## Review process

1. Read the task and supplied fictional evidence.
2. Examine the proposed answer for grounding, instruction compliance, privacy and completeness.
3. Choose ACCEPT, REJECT or INSUFFICIENT_EVIDENCE, and state which supporting source controls the finding.
4. Record a correction or verification request. Do not automatically resolve an unknown.
5. Check the reference key **after** independent review; log disagreements in [owner review worksheet](OWNER_REVIEW_WORKSHEET.md).

The generated answer key is in [casebook.jsonl](casebook.jsonl); ten [paired comparisons](pairs.jsonl) test preference selection, including ties and neither-acceptable answers. The [rubric](rubric.md) defines hard-failure rules and scoring anchors. A [sample of worked decisions](WORKED_EXAMPLES.md) shows the reasoning and limitations without dumping every item onto the front page.

## Distribution

| Category | Cases |
|---|---:|
| Arithmetic and reconciliation | 5 |
| Evidence and deployment claims | 5 |
| Privacy and masking | 5 |
| Instruction-following | 5 |
| Records and identity | 5 |
| Spanish-language meaning | 5 |
| **Total** | **30** |

Reference decision distribution: **12 ACCEPT / 14 REJECT / 4 INSUFFICIENT_EVIDENCE**. Each decision and four-dimension score (if applicable) is AI-drafted, not a certified rating or benchmark.

## Verify structure

From the repository root, with Python 3:

```bash
python ai-evaluation/scripts/validate_examples.py
```

This validates counts, fields, score ranges, IDs and distributions; it cannot verify human authorship, professional annotation ability or the correctness of every nuanced judgment. The original four-case exploratory file remains available as [legacy examples](evaluation_batch.csv).
