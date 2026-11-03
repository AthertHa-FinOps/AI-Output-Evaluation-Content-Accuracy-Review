"""Validate sample structure and selected fixed reference anchors (not human judgment)."""
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = ("grounding", "instructions", "privacy", "completeness")
CATS = {"arithmetic", "evidence", "privacy", "instruction", "records", "bilingual"}


def load(path):
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def check_cases(rows):
    assert len(rows) == 30, f"Expected 30 cases, saw {len(rows)}"
    assert len(set(r["id"] for r in rows)) == 30, "Duplicate case IDs"
    assert {r["category"] for r in rows} == CATS
    assert Counter(r["category"] for r in rows) == {x: 5 for x in CATS}
    assert sum(r["language"] == "es" for r in rows) == 5
    decisions = Counter(r["reference_decision"] for r in rows)
    assert decisions["ACCEPT"] >= 8 and decisions["REJECT"] >= 12
    assert decisions["INSUFFICIENT_EVIDENCE"] >= 3
    for r in rows:
        assert set(r) == {
            "id","category","language","fictional_source","task_requirement",
            "candidate_output","reference_decision","priority_dimension",
            "reference_scores","reference_rationale","recommended_followup",
            "reference_provenance",
        }, r["id"]
        assert r["language"] in {"en","es"}
        assert r["priority_dimension"] in DIMENSIONS
        assert all(isinstance(r[k], str) and len(r[k]) >= 10 for k in (
            "fictional_source","task_requirement","candidate_output",
            "reference_rationale","recommended_followup",
        )), r["id"]
        assert r["reference_provenance"] == "AI_DRAFT_NOT_HUMAN_ADJUDICATED"
        if r["reference_decision"] == "INSUFFICIENT_EVIDENCE":
            assert r["reference_scores"] is None, r["id"]
        else:
            scores = r["reference_scores"]
            assert set(scores) == set(DIMENSIONS) and all(
                type(v) is int and 0 <= v <= 2 for v in scores.values()), r["id"]
            if r["reference_decision"] == "ACCEPT":
                assert all(v == 2 for v in scores.values()), r["id"]
            else:
                assert scores[r["priority_dimension"]] == 0, r["id"]
    keyed = {r["id"]: r for r in rows}
    assert keyed["EV-02"]["reference_decision"] == "REJECT"
    assert "200" in keyed["EV-02"]["recommended_followup"]
    assert keyed["EV-13"]["reference_scores"]["privacy"] == 0
    assert keyed["EV-30"]["reference_decision"] == "INSUFFICIENT_EVIDENCE"
    return decisions


def check_pairs(rows):
    assert len(rows) == 10
    assert len(set(r["id"] for r in rows)) == 10
    preferences = Counter(r["reference_preference"] for r in rows)
    assert preferences["TIE"] >= 1 and preferences["NEITHER"] >= 1
    assert preferences["A"] >= 1 and preferences["B"] >= 1
    assert sum(r["language"] == "es" for r in rows) >= 2
    for p in rows:
        assert set(p) == {
            "id","language","task","fictional_source","response_A","response_B",
            "reference_preference","decisive_dimension","reference_rationale",
            "reference_provenance",
        }, p["id"]
        assert p["language"] in {"en","es"}
        assert p["reference_preference"] in {"A","B","TIE","NEITHER"}
        assert p["decisive_dimension"] in DIMENSIONS
        assert p["reference_provenance"] == "AI_DRAFT_NOT_HUMAN_ADJUDICATED"
        assert len(p["reference_rationale"]) >= 20
    return preferences


if __name__ == "__main__":
    decisions = check_cases(load(ROOT / "casebook.jsonl"))
    prefs = check_pairs(load(ROOT / "pairs.jsonl"))
    print("PASS: 30 case schema, distribution, reference-score and fixed-anchor checks")
    print("PASS: 10 paired comparison schemas and all preference classes")
    print("Reference distribution:", dict(decisions), dict(prefs))
    print("NOTE: This verifies structure, not independent human grading.")
