"""Build answer-key-free input sets for the owner's own rating exercise.

These are constructed fictional examples, not captured production model outputs.
The files omit reference labels; this cannot prove a reviewer has not seen them.
"""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
CASE_FIELDS = ("id", "language", "category", "fictional_source",
               "task_requirement", "candidate_output")
PAIR_FIELDS = ("id", "language", "task", "fictional_source",
               "response_A", "response_B")
SETS = (
    ("casebook.jsonl", "unscored_cases.jsonl", CASE_FIELDS),
    ("pairs.jsonl", "unscored_pairs.jsonl", PAIR_FIELDS),
)


def render(source, fields):
    rows = [json.loads(line) for line in source.splitlines() if line.strip()]
    return "\n".join(
        json.dumps({field: row[field] for field in fields},
                   ensure_ascii=False, separators=(",", ":"))
        for row in rows
    ) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify the committed inputs; do not write them")
    args = parser.parse_args()
    for source, target, fields in SETS:
        expected = render((ROOT / source).read_text(encoding="utf-8"), fields)
        dest = ROOT / target
        if args.check:
            assert dest.is_file() and dest.read_text(encoding="utf-8") == expected, (
                f"Out-of-date answer-key-free review inputs: {target}"
            )
        else:
            dest.write_text(expected, encoding="utf-8")
        for forbidden in ('"reference_scores"', '"reference_rationale"',
                          '"reference_decision"', '"candidate_response_verdict"',
                          '"reference_preference"'):
            assert forbidden not in expected, f"Answer key leaked into {target}"
        print(f"{target}: reference labels omitted; {'checked' if args.check else 'written'}")


if __name__ == "__main__":
    main()
