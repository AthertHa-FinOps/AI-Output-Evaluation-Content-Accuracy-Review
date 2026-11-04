"""Validate the unscored practice questions and the optional review-log templates.

These checks do not judge the quality of any answer or establish human review work.
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
CASE_FIELDS = {
    "id", "source_language", "response_language", "category",
    "source", "task", "response_under_review",
}
PAIR_FIELDS = {
    "id", "source_language", "response_language", "category",
    "source", "task", "response_A", "response_B",
}
REVIEW_COLUMNS = (
    "case_id", "review_kind", "set", "review_date",
    "first_verdict_or_preference", "grounding_score", "instructions_score",
    "privacy_score", "completeness_score", "source_evidence",
    "original_rationale", "rationale_language", "uncertainty_or_strength",
    "reference_checked_later", "disagreement_or_revision",
)
MODEL_COLUMNS = (
    "task_id", "run_datetime_timezone", "source_kind", "source_reference",
    "source_language", "response_language", "prompt_file", "raw_output_file",
    "model_provider", "model_version", "model_settings", "first_verdict",
    "grounding_score", "instructions_score", "privacy_score",
    "completeness_score", "source_evidence", "first_rationale",
    "rationale_language", "subsequent_reviewer", "subsequent_view",
    "disagreement_or_revision", "permission_to_publish",
)


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def check_exercises(rows, expected_count, fields, prefix):
    assert len(rows) == expected_count
    assert len({row["id"] for row in rows}) == expected_count
    for index, row in enumerate(rows, 1):
        assert row["id"] == f"{prefix}-{index:02d}", row["id"]
        assert set(row) == fields, row["id"]
        assert row["source_language"] in {"en", "es"}
        assert row["response_language"] in {"en", "es"}
        assert all(isinstance(value, str) and value.strip() for value in row.values())
        assert len(row["source"]) > 20 and len(row["task"]) > 20
    assert sum(row["source_language"] == "es" for row in rows) >= 2
    assert sum(row["response_language"] == "es" for row in rows) >= 1


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return tuple(reader.fieldnames), list(reader)


def validate():
    cases = read_jsonl(ROOT / "practice" / "cases.jsonl")
    pairs = read_jsonl(ROOT / "practice" / "pairs.jsonl")
    check_exercises(cases, 8, CASE_FIELDS, "ADV")
    check_exercises(pairs, 4, PAIR_FIELDS, "ADV-PAIR")

    base_cases = read_jsonl(ROOT / "casebook.jsonl")
    base_pairs = read_jsonl(ROOT / "pairs.jsonl")
    expected_ids = (
        [(r["id"], "single", "existing-reference") for r in base_cases]
        + [(r["id"], "pair", "existing-reference") for r in base_pairs]
        + [(r["id"], "single", "additional-practice") for r in cases]
        + [(r["id"], "pair", "additional-practice") for r in pairs]
    )
    headers, entries = read_csv(ROOT / "owner_review_log_template.csv")
    assert headers == REVIEW_COLUMNS
    assert len(entries) == len(expected_ids) == 52
    assert [(r["case_id"], r["review_kind"], r["set"]) for r in entries] == expected_ids
    # Allow genuinely entered personal ratings in future without breaking CI.
    for entry in entries:
        for name in ("grounding_score", "instructions_score", "privacy_score",
                     "completeness_score"):
            assert entry[name] in {"", "0", "1", "2", "N/A"}, (entry["case_id"], name)

    model_headers, runs = read_csv(ROOT / "model_output_log_template.csv")
    assert model_headers == MODEL_COLUMNS
    # If actual model runs are added later, they must have a task ID and provider.
    assert all(r["task_id"] and r["model_provider"] and r["raw_output_file"]
               for r in runs)

    print("PASS: 8 unscored practice cases, 4 pairs, 52 review-log rows")
    print(f"PASS: model-output log schema ({len(runs)} recorded runs)")
    print("NOTE: This does not establish completed ratings or actual model runs.")


if __name__ == "__main__":
    validate()
