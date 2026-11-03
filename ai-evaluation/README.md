# Source-based response evaluation exercises

The casebook contains **30 constructed fictional candidate responses** with task instructions, sources, AI-assisted reference judgments, explanations and proposed corrections. The pairs contain **10 constructed A/B comparisons**. These are not captured results from named LLMs or paid annotation tasks.

## Examples to inspect

| Case | Review issue | Source-based result |
|---|---|---|
| **EV-02** | Arithmetic | CAD 141 + CAD 59 = CAD 200, not CAD 210 |
| **EV-04** | Missing adjustment | CAD 90 + CAD 10 = CAD 100, not CAD 90 |
| **EV-10** | Evidence status | An export without a run log does not establish deployment; the cautious response is acceptable |
| **EV-13** | Redaction | Account ID ZX-00042 was exposed despite a masking requirement |
| **EV-19** | Instructions and grounding | The answer omits the confidence label and claims reconciliation without evidence |
| **EV-22** | Duplicate handling | A shared email is not sufficient grounds for immediate deletion |
| **EV-27** | Spanish meaning | *Rechazado* means rejected, not approved |
| **EV-30** | Spanish context | The sentence does not identify what was registered; the answer should not invent a subject |

The [reference casebook](casebook.jsonl) holds the proposed verdicts and score fields; [paired source/answers](pairs.jsonl) hold the proposed A/B preferences.

## Rating rules

The [rubric](rubric.md) checks grounding, instructions, privacy and completeness. Privacy is **null / N/A** for scored cases with no masking requirement; it should not earn two points just because privacy was not tested. Four cases with insufficient source evidence keep `reference_scores=null` and separately record an **ACCEPT** verdict for a cautious candidate response. These choices are AI-assisted practice keys, not completed personal annotation.

| Category | Cases |
|---|---:|
| Arithmetic | 5 |
| Evidence and deployment claims | 5 |
| Privacy and masking | 5 |
| Instruction following | 5 |
| Records and identity | 5 |
| Spanish-source interpretation | 5 |
| **Total** | **30** |

There are five Spanish-source cases and two Spanish-source pairs. The files distinguish `source_language` from `response_language`; the examples use English candidate responses, including for Spanish inputs. The translations are illustrative, not independently certified bilingual evaluation.

## Complete an answer-key-free review

1. Open [unscored_cases.jsonl](unscored_cases.jsonl) or [unscored_pairs.jsonl](unscored_pairs.jsonl). They contain sources and candidate responses but **no labels, scores or rationales**.
2. Record your own verdict, source evidence, uncertainty and correction in the [review worksheet](OWNER_REVIEW_WORKSHEET.md).
3. Only afterward compare with the [reference key](casebook.jsonl). Preserve disagreements and dates.

The blank worksheet is not evidence of an independent review. If you have seen an example's key already, that later exercise is not genuinely blind; label it a reference-hidden self-check instead.

## Programmatic checks

```bash
python ai-evaluation/scripts/validate_examples.py
python ai-evaluation/scripts/prepare_review_inputs.py --check
```

The earlier [four exploratory rows](evaluation_batch.csv) now use separate `BATCH-..` IDs rather than reusing different `EV-..` case IDs. Structural checks cannot determine whether every subjective reference judgment is correct.
