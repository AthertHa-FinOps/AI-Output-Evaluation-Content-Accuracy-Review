# Evidence types and responsibility

This repository links skills from paid transaction-document review to self-directed AI-output exercises. Those are different types of experience.

| Evidence | What exists | What it supports |
|---|---|---|
| **Paid real estate work** | Reviewing agreements, amendments, identity and financial records; investigating discrepancies and coordinating follow-up | Transferable source-checking, confidentiality and documentation work |
| **Constructed response exercises** | 30 fictional candidate responses and ten A/B pairs with AI-assisted reference labels | A demonstration of evaluation task design and proposed reasoning; **not** independent annotations of real model responses |
| **Reproducible processing exercise** | Fourteen source and fourteen export rows, ten open exceptions, Python script and unit tests | Record matching, exception reporting and conservative action rules on fictional data |
| **Personal evaluator review** | [Answer-key-free inputs](ai-evaluation/unscored_cases.jsonl) and [blank review worksheet](ai-evaluation/OWNER_REVIEW_WORKSHEET.md) | A procedure for future personal evaluation; **no completed ratings yet** |
| **Retrospective document notes** | [Earlier notes](case-studies/detailed-evaluation-notes.md) on technical-document revisions | A narrative of reported checks; not a complete, dated before-and-after audit trail |

## What the labels prove

The casebook's `candidate_response_verdict` contains 16 ACCEPT and 14 REJECT reference labels. The retained `reference_decision` field contains 12 ACCEPT, 14 REJECT and four INSUFFICIENT_EVIDENCE labels; those last four candidate answers correctly avoid inventing missing facts. The counts describe a constructed practice set. **They do not measure a model's error rate, my personal accuracy or agreement with another annotator.**

The privacy dimension is N/A on scored tasks that do not test a privacy rule. The response and paired-output origin fields explicitly mark the examples as constructed; no named AI model output was captured.

## What remains to demonstrate

- Independently evaluate selected cases, including English–Spanish meaning and ambiguous records, recording the actual source reasoning, date and disagreement with the AI reference.
- Work with real evaluation guidelines and previously unseen candidate responses, if permitted, and record results without revealing employer-confidential material.
- Show consistent judgments or second-reviewer calibration only if those activities are genuinely performed and measured.

AI assisted in drafting case material, rubrics, reference labels, code and prose. The executable checks verify defined inputs and outputs, **not professional annotation capability**. No paid AI evaluation engagement, production benchmark or deployed customer system is claimed.

[Overview](README.md) · [Rubric](ai-evaluation/rubric.md) · [Test and audit limits](PORTFOLIO_AUDIT.md)
