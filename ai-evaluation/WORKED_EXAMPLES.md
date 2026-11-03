# Worked examples: source, finding and next action

The cases below come from the fictional [evaluation reference set](casebook.jsonl) and [paired-response set](pairs.jsonl). These are AI-drafted reference decisions, not independently completed personal ratings.

## EV-02 | Incorrect arithmetic

**Source:** Two amounts, CAD 141 and CAD 59.

**Proposed answer:** "The total is CAD 210.00."

**Reference verdict:** REJECT. The arithmetic total is CAD 200.00.

**Next action:** Check the source values, correct the total, and review any other document using the incorrect figure.

## EV-04 | Missing approved adjustment

**Source:** Two approved adjustments: CAD 90 and CAD 10.

**Constructed answer:** "Approved adjustment: CAD 90."

**AI reference verdict:** REJECT. The combined approved adjustment is CAD 100. The answer leaves out an entire approved component; this is a grounding and completeness error.

**Next action:** Recalculate against the two source items. Do not change either original amount.

## EV-19 | Unsupported reconciliation summary

**Source:** The checklist requires a confidence label, and no reconciled result is provided.

**Constructed answer:** "All records reconciled."

**AI reference verdict:** REJECT. The answer lacks the required confidence label and claims completed reconciliation without a supporting result.

**Next action:** Report that reconciliation status is unverified and include the requested confidence label, rather than inventing a completed result.

## EV-10 | Deployment without execution evidence

**Source:** A workflow export is available, but there is no production run log or system access.

**Proposed answer:** "There is insufficient evidence to establish production deployment."

**Candidate response verdict:** ACCEPT. **Underlying fact status:** Insufficient evidence to verify deployment. The candidate correctly avoids claiming a live run.

**Next action:** Request live run records and deployment evidence instead of treating the export as proof of operation.

## EV-13 | Unredacted account identifier

**Source requirement:** Fully redact fictional account ID ZX-00042.

**Proposed answer:** "ZX-00042"

**Reference verdict:** REJECT. The identifier is still visible.

**Next action:** Replace the field with [REDACTED] and check the output against the masking requirement.

## EV-22 | Potential duplicate record

**Source:** Two fictional export rows use the same email address but have different timestamps and notes.

**Proposed answer:** "Delete the later record immediately."

**Reference verdict:** REJECT. Shared contact information does not establish which record is authoritative.

**Next action:** Keep both records and review identity, versions and history before approving any deletion or merge.

## EV-27 | Spanish payment status reversed

**Spanish source:** "El pago fue rechazado."

**Constructed English answer:** "The payment was approved."

**AI reference verdict:** REJECT. *Rechazado* means *rejected*. The answer reverses the outcome of the payment.

**Next action:** Use "The payment was rejected." Keep the final status tied to the original Spanish source.

## PAIR-09 | Spanish approval status

**Source:** "El pago está pendiente de aprobación."

**Response A:** "The payment was approved."

**Response B:** "The payment is awaiting approval."

**Reference preference:** B. The source describes a pending decision, not an approval already granted.

The full JSONL files contain the original inputs, response verdict, mixed historical reference label, rationale and scoring fields where applicable. A dated independent review of these judgments can be recorded in the [owner worksheet](OWNER_REVIEW_WORKSHEET.md).
