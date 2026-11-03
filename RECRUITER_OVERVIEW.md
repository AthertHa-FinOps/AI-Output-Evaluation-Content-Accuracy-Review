# AI response-review evidence for recruiters

**Relevant paid experience:** Real estate transaction documentation, source checks, conflicting information and follow-up with clients and third parties. **Not claimed:** Paid AI annotation, model benchmarking, evaluator calibration or quality-team leadership.

## Open these examples

| Assignment type | Specific case | What a reviewer can check |
|---|---|---|
| Factual accuracy | [EV-04](ai-evaluation/WORKED_EXAMPLES.md) | Two adjustments total CAD 100, not the reported CAD 90 |
| Privacy and instructions | [EV-13](ai-evaluation/WORKED_EXAMPLES.md) | A mandatory redaction was missed |
| Grounded uncertainty | [EV-10](ai-evaluation/WORKED_EXAMPLES.md) | The answer correctly says the supplied evidence cannot prove deployment |
| English/Spanish meaning | [PAIR-09](ai-evaluation/PAIRED_COMPARISONS.md) | *Pendiente de aprobación* must not become *approved* |
| Pairwise preference | [PAIR-08](ai-evaluation/PAIRED_COMPARISONS.md) | Both candidates invent test results, so neither can be chosen |
| Record controls | [EX-006](back-office-case-study/outputs/exception_register.csv) | The source/export amount mismatch remains unresolved |

## Relevant roles and limits

| Role family | Portfolio supports | Missing evidence |
|---|---|---|
| AI Response Evaluator / factuality reviewer | Checking source support, arithmetic, privacy and stated constraints | Independently completed ratings on unseen material |
| Text annotator / LLM response rater | Structured cases, rating dimensions, proposed rationales and preference labels | Annotation-platform work, calibration and measured consistency |
| English–Spanish evaluator | Five Spanish-source cases and two Spanish-source pairs; paid bilingual communication experience is separate | Independently rated nuanced bilingual examples and professional language-review results |
| AI response quality analyst / reviewer | An identifiable rubric and repeatable mechanical checks | Second-rater disagreements, batch QA metrics and professional adjudication experience |

All casebook candidates and paired responses were **constructed for this exercise**; no actual LLM model outputs were captured. The keys and rationales were drafted with AI assistance. A recruiter can inspect them, but they do not demonstrate that I scored the same cases independently.

The [answer-key-free input files](ai-evaluation/unscored_cases.jsonl) and [personal review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) are available for a subsequent actual review. That worksheet is still blank.

[Overview](README.md) · [Rubric](ai-evaluation/rubric.md) · [Ownership notes](EVIDENCE_AND_OWNERSHIP.md)
