# Worked examples: source, finding and next action

The cases below come from the fictional [evaluation reference set](casebook.jsonl) and [paired-response set](pairs.jsonl). These are AI-drafted reference decisions, not independently completed personal ratings.

## EV-02 | Incorrect arithmetic

**Source:** Two amounts, CAD 141 and CAD 59.

**Proposed answer:** "The total is CAD 210.00."

**Reference verdict:** REJECT. The arithmetic total is CAD 200.00.

**Next action:** Check the source values, correct the total, and review any other document using the incorrect figure.

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

## PAIR-09 | Spanish approval status

**Source:** "El pago está pendiente de aprobación."

**Response A:** "The payment was approved."

**Response B:** "The payment is awaiting approval."

**Reference preference:** B. The source describes a pending decision, not an approval already granted.

The full JSONL files contain the original inputs, response verdict, mixed historical reference label, rationale and scoring fields where applicable. A dated independent review of these judgments can be recorded in the [owner worksheet](OWNER_REVIEW_WORKSHEET.md).
