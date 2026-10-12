import unittest

from grade_calculator import calculate_report, letter_grade


class GradeCalculatorTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual([letter_grade(score) for score in (100, 90, 89.99, 80, 70, 60, 59.99, 0)],
                         ["A", "A", "B", "B", "C", "D", "F", "F"])

    def test_calculates_weighted_overall_percentage_and_subject_results(self):
        report = calculate_report([("Math", 45, 50), ("English", 80, 100)])
        self.assertAlmostEqual(report["overall_percentage"], 125 / 150 * 100)
        self.assertEqual(report["average_marks"], 62.5)
        self.assertEqual(report["overall_grade"], "B")
        self.assertEqual([item["grade"] for item in report["subjects"]], ["A", "B"])

    def test_rejects_empty_subjects_and_invalid_marks(self):
        for subjects in ([], [("Math", -1, 100)], [("Math", 101, 100)], [("Math", 10, 0)],
                         [(" ", 1, 2)], [("Math", float("nan"), 100)]):
            with self.subTest(subjects=subjects), self.assertRaises(ValueError):
                calculate_report(subjects)

    def test_rejects_invalid_percentage(self):
        for value in (-0.1, 100.1, float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                letter_grade(value)


if __name__ == "__main__":
    unittest.main()
