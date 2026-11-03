"""Independent expected counts for deliberately planted fictional defects."""
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from reconcile import analyze, read_csv, DATA, amount, canonical

class ReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.issues, cls.controls = analyze(read_csv(DATA / "source_records.csv"), read_csv(DATA / "processing_export.csv"))

    def test_control_totals(self):
        self.assertEqual((self.controls["source_records"], self.controls["export_records"], self.controls["distinct_export_case_ids"]), (14, 14, 13))

    def test_planted_defects(self):
        self.assertEqual(self.controls["issue_counts"], {
            "SOURCE_NOT_IN_EXPORT": 2, "EXPORT_NOT_IN_SOURCE": 1,
            "DUPLICATE_PROCESSING": 1, "CASE_ID_FORMAT": 1,
            "CUSTOMER_REFERENCE_MISMATCH": 1, "DOCUMENT_TYPE_MISMATCH": 1,
            "INVALID_OR_MISSING_AMOUNT": 1, "AMOUNT_MISMATCH": 1,
            "DOCUMENT_NOT_RECEIVED": 1,
        })
        self.assertEqual(len(self.issues), 10)

    def test_no_assumed_resolution(self):
        self.assertTrue(all(i["disposition"] == "OPEN - review required" for i in self.issues))
        self.assertEqual({i["case_id"] for i in self.issues if i["issue_type"] == "SOURCE_NOT_IN_EXPORT"}, {"CASE-011", "CASE-014"})

    def test_duplicate_source_case_id_is_not_silently_overwritten(self):
        source = [
            {"case_id": "CASE-001", "customer_ref": "C-1", "document_type": "Agreement", "amount_cad": "100"},
            {"case_id": " case-001 ", "customer_ref": "C-2", "document_type": "Waiver", "amount_cad": "200"},
        ]
        with self.assertRaisesRegex(ValueError, "Duplicate source case ID"):
            analyze(source, [])

    def test_blank_source_case_id_is_held(self):
        source = [{"case_id": " ", "customer_ref": "C-1", "document_type": "Agreement", "amount_cad": "100"}]
        with self.assertRaisesRegex(ValueError, "Blank source case ID"):
            analyze(source, [])

    def test_normalization(self):
        self.assertEqual(canonical(" case-002 "), "CASE-002")
        self.assertEqual(amount("14200"), amount("14200.00"))
        self.assertIsNone(amount(""))
        self.assertIsNone(amount("NaN"))
        self.assertIsNone(amount("Infinity"))

if __name__ == "__main__":
    unittest.main()
