# Paired-response quality comparisons

Ten fictional A/B evaluations test preference decisions against the same supplied evidence. This includes a **TIE** where both responses are acceptable and **NEITHER** where both invent test results.

| Pair | Focus | AI-drafted reference preference | Reason |
|---|---|---|---|
| PAIR-01 | grounding | **A** | A correctly totals 225; B introduces a CAD 10 arithmetic error. |
| PAIR-02 | grounding | **A** | The source documents design, not verified delivery. |
| PAIR-03 | instructions | **B** | A delete is unauthorized without an identity/version check. |
| PAIR-04 | privacy | **A** | B leaks a direct name while A follows the masking rule. |
| PAIR-05 | grounding | **A** | Only A preserves the documented waiver; B changes both action and evidence. |
| PAIR-06 | grounding | **A** | A states the missing evidence, B invents a tax outcome. |
| PAIR-07 | grounding | **TIE** | Both express the same status; no grounded preference exists. |
| PAIR-08 | grounding | **NEITHER** | Both claim completed results unsupported by the source; neither is acceptable. |
| PAIR-09 | grounding | **B** | B preserves pending authorization; A asserts approval. |
| PAIR-10 | instructions | **B** | Matching email does not authorize a one-sided overwrite. |

Full prompts, the two responses and references: [pairs.jsonl](pairs.jsonl).

**Status:** AI-generated reference examples, not blind or independent pairwise ratings by Hans, and not a measured model preference outcome. A personal pass can be documented in [owner review worksheet](OWNER_REVIEW_WORKSHEET.md).
