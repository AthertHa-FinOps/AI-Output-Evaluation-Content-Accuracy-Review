# Portfolio review: evidence, limits and release checks

**Review date:** November 3, 2026  
**Intended roles:** Entry-level/contract AI response evaluator, text annotator, bilingual English–Spanish reviewer and factual-accuracy reviewer. Senior evaluator QA or annotation team leadership requires separate evidence.

## What can be inspected

| Material | What exists |
|---|---|
| Individual tasks | 30 constructed fictional candidate responses in six categories; five use Spanish source text |
| Paired tasks | Ten constructed comparisons; two use Spanish source text |
| AI-assisted reference labels | 16 ACCEPT / 14 REJECT candidate-response verdicts; the older mixed field also has four INSUFFICIENT_EVIDENCE cases |
| Source-data reconciliation | 14 fictional source rows, 14 processing rows, ten open exceptions and six unit tests |
| Independent personal evaluations | **None recorded**; the worksheet is blank |
| Key-free review sets | Separate individual-case and paired-case files with no reference labels, scores or rationales |

These counts are properties of a **constructed exercise**, not a benchmark, annotation throughput or model error rate.

## Corrections from the critical re-audit

- Mark `candidate_output_origin` and `pair_origin` explicitly as constructed fictional material. Record `source_language` separately from `response_language` so a Spanish source is not mistaken for a Spanish output.
- Stop awarding privacy credit on tasks without a privacy requirement: use `null` (N/A) for the 21 scored non-privacy cases.
- Keep candidate-response acceptability separate from the underlying insufficient-evidence state.
- Give the four exploratory batch rows unique `BATCH-..` identifiers rather than reusing distinct `EV-..` case IDs.
- Add generated answer-key-free review files and an integrity check; **do not** present them as completed independent ratings.
- Treat non-finite financial values as invalid and define the document-status check as an exercise rule, not a fact independently established by the source.
- Preserve the earlier duplicate-source-ID guard and run output-diff checks for generated reconciliation files.

## Tests and what they do not establish

The CI workflow checks schema and selected reference-score constraints, integrity of answer-key-free samples, six reconciliation tests, exact generated-output snapshots and internal Markdown links. Check [the run history](https://github.com/AthertHa-FinOps/AI-Output-Evaluation-Content-Accuracy-Review/actions/workflows/portfolio-checks.yml) for the published commit's actual result.

Automated checks cannot validate translation nuance in all scenarios, prove a second evaluator agrees, show that the author independently rated examples, detect every security issue or establish model quality.

## Remaining credibility gaps

1. No dated, personally authored first-pass judgments on unseen or reference-hidden examples.
2. No captured response from a named model, prompt-run log, model version or real output benchmark.
3. Only short fictional Spanish-source cases; nuanced bilingual competence has not been independently assessed in this repository.
4. No professional calibration process, sampling analysis, second-rater comparison or documented disagreement resolution.
5. The earlier technical-document review narrative lacks a complete claim-by-claim dated version trail.

**Release wording:** A reproducible, AI-assisted set of fictional response-review exercises and a processing reconciliation example. Useful as a supplementary work sample for junior/contract roles; not evidence of paid AI annotation, independent accuracy or evaluator-lead experience.

[Main portfolio](README.md) · [Reviewer overview](RECRUITER_OVERVIEW.md) · [Ownership boundary](EVIDENCE_AND_OWNERSHIP.md) · [Blank review record](ai-evaluation/OWNER_REVIEW_WORKSHEET.md)
