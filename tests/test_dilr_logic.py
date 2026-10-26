import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


def positions(order):
    return {letter: i + 1 for i, letter in enumerate(order)}


def valid_q1_low(order):
    p = positions(order)
    return p["B"] == p["A"] + 1 and p["C"] == p["B"] + 1 and p["D"] < p["A"] and p["C"] < p["E"]


def valid_q1_medium(order):
    p = positions(order)
    return p["C"] == p["A"] + 1 and p["B"] == p["C"] + 1 and p["D"] < p["A"] and p["E"] > p["B"] and p["F"] != 6


def valid_q1_high(order):
    p = positions(order)
    return p["C"] == p["A"] + 1 and p["B"] == p["C"] + 1 and p["D"] < p["A"] and p["B"] < p["E"] and p["E"] < p["G"] and p["F"] != 7


def valid_q2_low(order):
    p = positions(order)
    return p["B"] == p["C"] + 1 and p["A"] == p["B"] + 1 and p["A"] < p["E"] and p["C"] != 2


def valid_q2_medium(order):
    p = positions(order)
    return p["B"] == p["C"] + 1 and p["A"] == p["B"] + 1 and p["C"] < p["F"] and p["A"] < p["E"] and p["C"] != 2


def valid_q2_high(order):
    p = positions(order)
    return p["B"] == p["C"] + 1 and p["A"] == p["B"] + 1 and p["G"] < p["C"] and p["C"] != 2 and p["C"] < p["F"] and p["A"] < p["E"]


class TestDILRAnswerKeys(unittest.TestCase):
    def assert_forced(self, entities, predicate, answer, slot):
        valid = []
        for order in itertools.permutations(entities):
            p = positions(order)
            if predicate(order):
                valid.append(p)
        self.assertGreater(len(valid), 0, "Question has no valid arrangements")
        self.assertEqual({p[answer] for p in valid}, {slot})

    def test_q1_all_difficulty_levels(self):
        self.assert_forced("ABCDE", valid_q1_low, "E", 5)
        self.assert_forced("ABCDEF", valid_q1_medium, "E", 6)
        self.assert_forced("ABCDEFG", valid_q1_high, "G", 7)

    def test_q2_all_difficulty_levels(self):
        self.assert_forced("ABCDE", valid_q2_low, "A", 3)
        self.assert_forced("ABCDEF", valid_q2_medium, "A", 3)
        self.assert_forced("ABCDEFG", valid_q2_high, "C", 3)

    def test_source_declares_level_variants_and_visual_item(self):
        for level in ("low", "medium", "high"):
            self.assertIn(f"{level}:{{answer:", HTML)
        self.assertIn("const questionBanks={", HTML)
        self.assertIn("tag:'Visual DI", HTML)
        self.assertIn("function renderVisualChart(chart)", HTML)
        self.assertIn("id=\"difficultyHelp\"", HTML)

    def test_explanations_and_personalised_popup_exist(self):
        self.assertIn("Candidate block placements", HTML)
        self.assertIn("function makePersonalizedFeedback", HTML)
        self.assertIn("id=\"personalFeedbackModal\"", HTML)
        self.assertIn("id=\"feedbackNext\"", HTML)


if __name__ == "__main__":
    unittest.main()
