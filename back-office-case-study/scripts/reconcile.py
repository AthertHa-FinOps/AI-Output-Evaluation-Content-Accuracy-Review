"""Read-only comparison of fictional source and processing exports; standard library only."""
import csv
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
OUT = BASE / "outputs"

def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def canonical(value):
    return (value or "").strip().upper()

def amount(value):
    try:
        return Decimal((value or "").strip()).quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        return None

def analyze(source_rows, export_rows):
    source = {canonical(r["case_id"]): r for r in source_rows}
    by_id = defaultdict(list)
    for r in export_rows:
        by_id[canonical(r["case_id"])].append(r)
    issues = []
    def flag(case_id, process_id, category, severity, src, observed, action):
        issues.append({
            "exception_id": f"EX-{len(issues)+1:03d}", "case_id": case_id,
            "process_id": process_id, "issue_type": category, "severity": severity,
            "source_value": str(src), "observed_value": str(observed),
            "recommended_action": action, "disposition": "OPEN - review required",
        })
    for case_id in sorted(source):
        if case_id not in by_id:
            flag(case_id, "", "SOURCE_NOT_IN_EXPORT", "High", "Source case exists", "No processed record", "Check queue or transmission history; do not invent a record")
    for case_id, entries in sorted(by_id.items()):
        if case_id not in source:
            for row in entries:
                flag(case_id, row["process_id"], "EXPORT_NOT_IN_SOURCE", "High", "No matching source case", "Processed record exists", "Investigate origin before any deletion")
            continue
        if len(entries) > 1:
            flag(case_id, ",".join(r["process_id"] for r in entries), "DUPLICATE_PROCESSING", "High", "One source case", f"{len(entries)} processed rows", "Hold both records; check for legitimate versioning before resolving")
        s = source[case_id]
        for row in entries:
            pid = row["process_id"]
            if row["case_id"] != case_id:
                flag(case_id, pid, "CASE_ID_FORMAT", "Low", case_id, row["case_id"], "Normalize identifier only after source confirmation")
            if row["customer_ref"] != s["customer_ref"]:
                flag(case_id, pid, "CUSTOMER_REFERENCE_MISMATCH", "High", s["customer_ref"], row["customer_ref"], "Confirm against authoritative customer record")
            if row["document_type"] != s["document_type"]:
                flag(case_id, pid, "DOCUMENT_TYPE_MISMATCH", "Medium", s["document_type"], row["document_type"], "Confirm source document classification")
            if amount(row["amount_cad"]) is None:
                flag(case_id, pid, "INVALID_OR_MISSING_AMOUNT", "High", s["amount_cad"], row["amount_cad"] or "(blank)", "Hold amount for source-backed correction")
            elif amount(row["amount_cad"]) != amount(s["amount_cad"]):
                flag(case_id, pid, "AMOUNT_MISMATCH", "High", s["amount_cad"], row["amount_cad"], "Reconcile against supporting financial record")
            if canonical(row["document_status"]) != "RECEIVED":
                flag(case_id, pid, "DOCUMENT_NOT_RECEIVED", "High", "Required document received", row["document_status"], "Hold completion pending document verification")
    return issues, {
        "source_records": len(source_rows), "export_records": len(export_rows),
        "distinct_export_case_ids": len(by_id),
        "source_cases_absent_from_export": sum(k not in by_id for k in source),
        "export_case_ids_without_source": sum(k not in source for k in by_id),
        "duplicate_case_groups": sum(len(v) > 1 for v in by_id.values()),
        "exceptions": len(issues),
        "issue_counts": dict(sorted(Counter(i["issue_type"] for i in issues).items())),
    }

def write_results(issues, controls):
    OUT.mkdir(parents=True, exist_ok=True)
    fields = ["exception_id", "case_id", "process_id", "issue_type", "severity", "source_value", "observed_value", "recommended_action", "disposition"]
    with (OUT / "exception_register.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(issues)
    lines = ["# Reconciliation control summary", "", "**Synthetic training data.** No client records or production work.", "", "| Control | Observed |", "|---|---:|"]
    for k in ("source_records", "export_records", "distinct_export_case_ids", "source_cases_absent_from_export", "export_case_ids_without_source", "duplicate_case_groups", "exceptions"):
        lines.append(f"| {k.replace('_', ' ').capitalize()} | {controls[k]} |")
    lines.extend(["", "## Exceptions by type", "", "| Category | Count |", "|---|---:|"])
    for k, value in controls["issue_counts"].items():
        lines.append(f"| {k} | {value} |")
    lines.extend(["", "**Disposition:** No records were deleted, created, merged or auto-corrected. Every exception remains open for human review.", "", "**Control limitation:** Equal source/export row totals do not establish the same cases are present.", ""])
    (OUT / "control_summary.md").write_text("\n".join(lines), encoding="utf-8")

def main():
    issues, controls = analyze(read_csv(DATA / "source_records.csv"), read_csv(DATA / "processing_export.csv"))
    write_results(issues, controls)
    print(f"Source={controls['source_records']} Export={controls['export_records']} Exceptions={controls['exceptions']}")

if __name__ == "__main__":
    main()
