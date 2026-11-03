"""Validate fictional evaluation reference schemas and selected internal consistency rules.

This checks draft reference data, not the correctness of all judgments or reviewer skill.
"""
from collections import Counter
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = ("grounding", "instructions", "privacy", "completeness")
CATS = {"arithmetic", "evidence", "privacy", "instruction", "records", "bilingual"}
VERDICTS = {"ACCEPT", "REJECT", "INSUFFICIENT_EVIDENCE"}


def load(path):
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def check_cases(rows):
    assert len(rows) == 30, f"Expected 30 cases, saw {len(rows)}"
    assert len(set(r["id"] for r in rows)) == 30, "Duplicate case IDs"
    assert Counter(r["category"] for r in rows) == {x: 5 for x in CATS}
    assert sum(r["source_language"] == "es" for r in rows) == 5
    decisions = Counter(r["reference_decision"] for r in rows)
    response_verdicts = Counter(r["candidate_response_verdict"] for r in rows)
    assert decisions == {"ACCEPT": 12, "REJECT": 14, "INSUFFICIENT_EVIDENCE": 4}
    assert response_verdicts == {"ACCEPT": 16, "REJECT": 14}
    for r in rows:
        assert set(r) == {
            "id", "category", "source_language", "response_language", "fictional_source",
            "task_requirement", "candidate_output", "reference_decision",
            "candidate_response_verdict", "priority_dimension",
            "reference_scores", "reference_rationale", "recommended_followup",
            "reference_provenance", "candidate_output_origin",
        }, r["id"]
        assert r["category"] in CATS and r["source_language"] in {"en", "es"}
        assert r["response_language"] == "en", r["id"]
        assert r["reference_decision"] in VERDICTS
        assert r["candidate_response_verdict"] in {"ACCEPT", "REJECT"}
        assert r["priority_dimension"] in DIMENSIONS
        assert all(isinstance(r[k], str) and len(r[k]) >= 10 for k in (
            "fictional_source", "task_requirement",
            "reference_rationale", "recommended_followup",
        )), r["id"]
        assert isinstance(r["candidate_output"], str) and len(r["candidate_output"]) >= 2
        assert r["reference_provenance"] == "AI_DRAFT_NOT_HUMAN_ADJUDICATED"
        assert r["candidate_output_origin"] == "CONSTRUCTED_FICTIONAL_RESPONSE"
        if r["reference_decision"] == "INSUFFICIENT_EVIDENCE":
            assert r["reference_scores"] is None, r["id"]
            assert r["candidate_response_verdict"] == "ACCEPT", r["id"]
        else:
            assert r["candidate_response_verdict"] == r["reference_decision"], r["id"]
            scores = r["reference_scores"]
            assert set(scores) == set(DIMENSIONS), r["id"]
            for dimension, value in scores.items():
                if dimension == "privacy" and r["category"] != "privacy":
                    assert value is None, r["id"]
                else:
                    assert type(value) is int and 0 <= value <= 2, r["id"]
            if r["candidate_response_verdict"] == "ACCEPT":
                assert all(v == 2 for v in scores.values() if v is not None), r["id"]
            else:
                assert scores[r["priority_dimension"]] == 0, r["id"]
    keyed = {r["id"]: r for r in rows}
    assert keyed["EV-02"]["reference_scores"]["grounding"] == 0
    assert "200" in keyed["EV-02"]["recommended_followup"]
    assert keyed["EV-04"]["reference_scores"]["grounding"] == 0
    assert keyed["EV-04"]["priority_dimension"] == "grounding"
    assert keyed["EV-13"]["reference_scores"]["privacy"] == 0
    assert keyed["EV-19"]["reference_scores"]["grounding"] == 0
    assert keyed["EV-19"]["reference_scores"]["instructions"] == 0
    assert keyed["EV-22"]["reference_scores"]["grounding"] == 0
    assert keyed["EV-30"]["reference_decision"] == "INSUFFICIENT_EVIDENCE"
    for id_ in ("EV-05", "EV-10", "EV-25", "EV-30"):
        assert keyed[id_]["candidate_response_verdict"] == "ACCEPT"
    return decisions, response_verdicts


def check_pairs(rows):
    assert len(rows) == 10
    assert len(set(r["id"] for r in rows)) == 10
    preferences = Counter(r["reference_preference"] for r in rows)
    assert preferences == {"A": 5, "B": 3, "TIE": 1, "NEITHER": 1}
    assert sum(r["source_language"] == "es" for r in rows) == 2
    for p in rows:
        assert set(p) == {
            "id", "source_language", "response_language", "task", "fictional_source", "response_A",
            "response_B", "reference_preference", "decisive_dimension",
            "reference_rationale", "reference_provenance", "pair_origin",
        }, p["id"]
        assert p["source_language"] in {"en", "es"}
        assert p["response_language"] == "en", p["id"]
        assert p["reference_preference"] in {"A", "B", "TIE", "NEITHER"}
        assert p["decisive_dimension"] in DIMENSIONS
        assert p["reference_provenance"] == "AI_DRAFT_NOT_HUMAN_ADJUDICATED"
        assert p["pair_origin"] == "CONSTRUCTED_FICTIONAL_PAIR"
        assert len(p["reference_rationale"]) >= 20
    return preferences


def check_early_examples(path, case_rows):
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    identifiers = [r["example_id"] for r in rows]
    assert identifiers == [f"BATCH-{n:02d}" for n in range(1, 5)]
    assert not (set(identifiers) & {r["id"] for r in case_rows})
    assert all(r["decision"] in {"PASS", "FAIL"} for r in rows)
    assert all(r["severity"] in {"HIGH", "MEDIUM", "LOW", "NONE"} for r in rows)


if __name__ == "__main__":
    cases = load(ROOT / "casebook.jsonl")
    reference_decisions, response_verdicts = check_cases(cases)
    check_early_examples(ROOT / "evaluation_batch.csv", cases)
    preferences = check_pairs(load(ROOT / "pairs.jsonl"))
    print("PASS: 30 case schemas, reference consistency and fixed-anchor checks")
    print("PASS: 10 paired-comparison schemas and reference-preference counts")
    print("Reference decisions:", dict(reference_decisions))
    print("Candidate response verdicts:", dict(response_verdicts))
    print("Pair preferences:", dict(preferences))
    print("NOTE: No independent human grading is established by this script.")
