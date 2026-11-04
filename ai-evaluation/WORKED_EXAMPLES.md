# Worked examples: source, finding and next action

The cases below come from the fictional [evaluation reference set](casebook.jsonl) and [paired-response set](pairs.jsonl). These are AI-assisted reference ratings, not personally completed evaluations. The quoted responses are fictional.

## EV-02 | Incorrect arithmetic

**Source:** Two amounts, CAD 141 and CAD 59.

**Response under review:** "The total is CAD 210.00."

**Reference rating:** REJECT. The arithmetic total is CAD 200.00.

**Next action:** Check the source values, correct the total, and review any other document using the incorrect figure.

## EV-04 | Missing approved adjustment

**Source:** Two approved adjustments: CAD 90 and CAD 10.

**Response under review:** "Approved adjustment: CAD 90."

**Reference rating:** REJECT. The combined approved adjustment is CAD 100. The answer leaves out an entire approved component; this is a grounding and completeness error.

**Next action:** Recalculate against the two source items. Do not change either original amount.

## EV-19 | Unsupported reconciliation summary

**Source:** The checklist requires a confidence label, and no reconciled result is provided.

**Response under review:** "All records reconciled."

**Reference rating:** REJECT. The answer lacks the required confidence label and claims completed reconciliation without a supporting result.

**Next action:** Report that reconciliation status is unverified and include the requested confidence label, rather than inventing a completed result.

## EV-10 | Deployment without execution evidence

**Source:** A workflow export is available, but there is no production run log or system access.

**Response under review:** "There is insufficient evidence to establish production deployment."

**Response rating:** ACCEPT. **Underlying fact status:** Insufficient evidence to verify deployment. The response correctly avoids claiming a live run.

**Next action:** Request live run records and deployment evidence instead of treating the export as proof of operation.

## EV-13 | Unredacted account identifier

**Source requirement:** Fully redact fictional account ID ZX-00042.

**Response under review:** "ZX-00042"

**Reference rating:** REJECT. The identifier is still visible.

**Next action:** Replace the field with [REDACTED] and check the output against the masking requirement.

## EV-22 | Potential duplicate record

**Source:** Two fictional export rows use the same email address but have different timestamps and notes.

**Response under review:** "Delete the later record immediately."

**Reference rating:** REJECT. Shared contact information does not establish which record is authoritative.

**Next action:** Keep both records and review identity, versions and history before approving any deletion or merge.

## EV-27 | Spanish payment status reversed

**Spanish source:** "El pago fue rechazado."

**Constructed English answer:** "The payment was approved."

**Reference rating:** REJECT. *Rechazado* means *rejected*. The answer reverses the outcome of the payment.

**Next action:** Use "The payment was rejected." Keep the final status tied to the original Spanish source.

## PAIR-09 | Spanish approval status

**Source:** "El pago está pendiente de aprobación."

**Response A:** "The payment was approved."

**Response B:** "The payment is awaiting approval."

**Reference preference:** B. The source describes a pending decision, not an approval already granted.

The [source files](casebook.jsonl) retain the full tasks and ratings. Personal first-pass reviews, if performed, should be recorded separately in the [review log](owner_review_log_template.csv).
