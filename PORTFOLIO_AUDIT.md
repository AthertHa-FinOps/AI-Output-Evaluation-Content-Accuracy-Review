# Repository evidence and release checks

**Review date:** November 3, 2026

## Published sample inventory

| Item | Recorded evidence |
|---|---|
| Evaluation casebook | 30 fictional cases across six categories |
| Earlier mixed reference labels | 12 ACCEPT, 14 REJECT, 4 INSUFFICIENT_EVIDENCE |
| Candidate response assessments | 16 ACCEPT, 14 REJECT; four ACCEPT answers correctly withhold an unverified fact |
| Spanish-language material | Five casebook entries and two paired comparisons |
| Paired-response set | Ten pairs: five A, three B, one TIE, one NEITHER |
| Processing reconciliation | 14 source rows, 14 export rows, 13 distinct export case IDs and ten recorded exceptions; duplicate/blank source-ID collision guards |
| Independent owner review | Seven worksheet prompts; no completed decisions |

These counts are drawn from the committed sample files. Reference ratings and rationales were drafted with AI assistance; the numbers are not an accuracy score or a benchmark result.

## Automated checks

The repository workflow runs on pushes to `main` and pull requests. It performs:

- Casebook and paired-example field, ID, score-range, category, response-verdict and selected fixed-anchor checks
- Relative Markdown-link checks
- Six Python reconciliation unit tests, including rejection of duplicate or blank source case IDs
- Regeneration and count/status checks of the ten-row exception register, plus a committed-output diff check

See the [GitHub Actions run history](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) for the outcome on the latest published commit. A passing run verifies these programmed checks, not agreement with every language judgment.

## Known limits

- The new evaluation cases have no dated independent personal ratings or second-reviewer agreement record.
- A generated answer key is not a validated model comparison or professional annotation history. The four INSUFFICIENT_EVIDENCE scenarios cannot be counted as four poor candidate answers: each candidate response is appropriately cautious.
- The source files are fictional. The back-office checks do not establish production-system accuracy or business error rates.
- The earlier AWS document-review narrative has not been matched claim by claim to dated before-and-after versions.
- Internal link checks do not establish whether every external resource is currently accessible.

## Review conclusion

The repository provides inspectable source/output comparisons and a reproducible record-checking exercise. The next substantive evidence addition would be dated, independent review decisions entered in the existing worksheet, including any disagreements with the reference key.
