# Worked decisions — what a recruiter should look for

These are source-grounded **AI-drafted examples**. They show a review method; they do not claim personal independent annotation or paid QA experience.

## Example A: Arithmetic that sounds plausible

- Source: approved amounts CAD 141 and CAD 59.
- Candidate answer: “The total is CAD 210.”
- Reference decision: **REJECT**.
- Evidence: CAD 141 + CAD 59 = CAD 200.
- Resolution: Correct the total after checking source records, and propagate the correction to affected documents. The test is not how confidently a number is stated, but whether it reconciles.

## Example B: An uncertain deployment claim

- Source: workflow file exists, but no production execution record is available.
- Candidate answer: “There is insufficient evidence to establish deployment.”
- Reference decision: **INSUFFICIENT_EVIDENCE** for the deployment fact; the candidate answer appropriately recognizes the gap.
- Resolution: Ask for a live execution and deployment history. Never convert a design into a claimed working service.

## Example C: Privacy controls must include free text

- Source: a fictional note contains a person's full name, which the task requires masking everywhere.
- Candidate response leaves the name inside a note while masking the name field.
- Reference decision: **REJECT**, privacy score 0.
- Resolution: Remove the name from all relevant fields and review similar records for the same failure mode.

## Example D: Duplicate ≠ safe deletion

- Source: two fictional CRM rows share an email but have different notes and timestamps.
- Candidate response: “Delete the newest row.”
- Reference decision: **REJECT**.
- Resolution: Preserve both and check authoritative identity, ownership and version history first.

## Example E: Faithful bilingual interpretation

- Spanish source: “El pago está pendiente de aprobación.”
- Response A: “The payment was approved.”
- Response B: “The payment is awaiting approval.”
- Reference preference: **B** because approval has not yet happened.

These examples are deliberately compact. More nuanced judgments should be documented with contrary evidence, unknowns and a clear decision trail rather than a label alone.
