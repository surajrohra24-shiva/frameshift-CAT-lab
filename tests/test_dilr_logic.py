import itertools
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


def valid_q1(order):
    p = {letter: i + 1 for i, letter in enumerate(order)}
    return (
        p["C"] == p["A"] + 1
        and p["B"] == p["C"] + 1
        and p["D"] < p["A"]
        and p["E"] > p["B"]
        and p["F"] != 6
    )


def valid_q2(order):
    p = {letter: i + 1 for i, letter in enumerate(order)}
    return (
        p["B"] == p["C"] + 1
        and p["A"] == p["B"] + 1
        and p["C"] < p["F"]
        and p["A"] < p["E"]
        and p["C"] != 2
    )


class TestDILRAnswerKeys(unittest.TestCase):
    def test_q1_forces_e_into_slot_six(self):
        valid = [p for p in itertools.permutations("ABCDEF") if valid_q1(p)]
        self.assertEqual(len(valid), 3)
        self.assertEqual({p.index("E") + 1 for p in valid}, {6})

    def test_q2_forces_a_into_stop_three(self):
        valid = [p for p in itertools.permutations("ABCDEF") if valid_q2(p)]
        self.assertEqual(len(valid), 6)
        self.assertEqual({p.index("A") + 1 for p in valid}, {3})

    def test_source_contains_both_declared_answer_keys(self):
        self.assertIn("const q1={answer:'E'", HTML)
        self.assertIn("const q2={answer:'A'", HTML)

    def test_explanations_cover_elimination(self):
        self.assertIn("Candidate block placements", HTML)
        self.assertIn("Start 2", HTML)
        self.assertIn("only forced answer", HTML)


if __name__ == "__main__":
    unittest.main()
