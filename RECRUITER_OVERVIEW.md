# Recruiter review — one-page evidence map

**Candidate fit:** Back-office document/data verification, AI output evaluation contracts, CRM/data-quality support. Evidence comes first from paid real estate transaction work, then from labelled self-directed practice.

## What the repository actually demonstrates

| Hiring criterion | Traceable work sample | What it does / does not prove |
|---|---|---|
| Check figures against source | [EV-02; arithmetic review](ai-evaluation/WORKED_EXAMPLES.md) | Demonstrates a concrete calculation error and correction; not commercial finance analysis |
| Catch unsupported claims | [EV-10; deployment](ai-evaluation/WORKED_EXAMPLES.md) | Separates an export from actual observed execution |
| Follow privacy requirements | [EV-13; identifier redaction](ai-evaluation/WORKED_EXAMPLES.md) | Illustrates a masking failure on **fictional** identifiers |
| Handle ambiguous/duplicate records | [PAIR-03 and EV-22](ai-evaluation/PAIRED_COMPARISONS.md) | Prioritizes source verification over blind deletion |
| Compare alternative answers | [Ten paired examples](ai-evaluation/PAIRED_COMPARISONS.md) | Includes A/B, TIE and NEITHER; AI-generated reference decisions |
| Run controlled record checks | [Back-office script and test outputs](back-office-case-study/README.md) | 14/14 input rows, 10 logged exceptions; four automated tests |
| Distinguish paid from technical work | [Ownership and provenance](EVIDENCE_AND_OWNERSHIP.md) | Paid real estate documentation work; portfolio is not paid AI annotation |

## Illustrative issue register

| Item | Evidence available | Proposed action |
|---|---|---|
| Wrong financial total | Source 141 + 59; output claims 210 | **Correct to 200** after source confirmation |
| Overstated deployment | Workflow export; no run logs | **Hold claim**, request execution records |
| Identifying text | Unmasked fictional account ID | **Reject**, redact and recheck |
| Duplicate case | Two rows share email | **Hold both**, verify history before merge |

## Evidence scale and limitations

The 30-case review and ten paired comparisons are AI-authored **reference practice material**. They are neither independent human judgments nor a validated benchmark. The runnable reconciliation and automated tests show a narrower, reproducible technical check. Stronger hiring evidence requires the candidate to discuss choices independently and document his personal review of a sample.

[Main portfolio](README.md) · [Detailed rubric](ai-evaluation/rubric.md) · [Owner sign-off worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md)
