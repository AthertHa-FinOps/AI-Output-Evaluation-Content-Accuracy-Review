# AI response review: fictional casebook

Thirty source-and-candidate-response exercises are organized by issue type. Each includes the supplied evidence, task, proposed verdict, rationale and follow-up. **The keys were drafted with AI assistance and have not been independently scored by me.**

## Open a specific decision

- [EV-02](WORKED_EXAMPLES.md): the source amounts total CAD 200, but the output claims CAD 210
- [EV-04](casebook.jsonl): the output omits an approved CAD 10 adjustment and reports the wrong combined amount
- [EV-10](WORKED_EXAMPLES.md): a workflow export does not establish live deployment
- [EV-13](WORKED_EXAMPLES.md): the output reproduces a fictional account ID that should be redacted
- [EV-19](casebook.jsonl): the answer omits a confidence label and claims reconciliation without evidence
- [EV-22](WORKED_EXAMPLES.md): an email match does not authorize immediate deletion
- [PAIR-09](PAIRED_COMPARISONS.md): a Spanish pending-approval statement must not become an approved status

The complete [casebook](casebook.jsonl) retains the original fictional candidate output and AI-assisted reference rationale. [Paired comparisons](pairs.jsonl) use two answers for the same source. These are teaching examples rather than a benchmark set.

## Case inventory

| Category | Cases |
|---|---:|
| Arithmetic and reconciliation | 5 |
| Evidence and deployment claims | 5 |
| Privacy and masking | 5 |
| Instruction following | 5 |
| Records and identity | 5 |
| Spanish-language meaning | 5 |
| **Total** | **30** |

The older `reference_decision` field records **12 ACCEPT, 14 REJECT and 4 INSUFFICIENT_EVIDENCE** outcomes. The new `candidate_response_verdict` field separately records **16 acceptable and 14 rejected candidate responses**. Four cautious answers correctly report insufficient underlying evidence. This distinction is explained in the [rubric](rubric.md); neither count represents human grading performance.

## Review the material independently

1. Read the task and source, then the candidate answer **without opening the reference label**.
2. Decide whether that answer is acceptable and identify the decisive evidence.
3. Separately note whether the business fact is actually verifiable from the source.
4. Compare with the AI-assisted reference, retaining any disagreement and the review date.

The [owner-review worksheet](OWNER_REVIEW_WORKSHEET.md) remains blank. Do not turn draft references into claimed personal ratings.

## Mechanical validation

```bash
python ai-evaluation/scripts/validate_examples.py
```

The validator checks schemas, score ranges, fixed examples and reference counts. It does not determine whether every subjective language judgment is correct. [Earlier exploratory examples](evaluation_batch.csv) remain a separate four-row file.
