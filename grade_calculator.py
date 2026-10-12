"""Calculate subject results and a student's overall grade."""

from math import isfinite


GRADE_THRESHOLDS = ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F"))


def letter_grade(percentage: float) -> str:
    """Return the documented letter grade for a percentage from 0 to 100."""
    if not isfinite(percentage) or not 0 <= percentage <= 100:
        raise ValueError("percentage must be a finite number from 0 to 100")
    for threshold, grade in GRADE_THRESHOLDS:
        if percentage >= threshold:
            return grade
    raise AssertionError("grade thresholds must cover all valid percentages")


def calculate_report(subjects: list[tuple[str, float, float]]) -> dict:
    """Return each subject's percentage and the class average/overall result.

    Each subject is a tuple of (name, marks_earned, maximum_marks).
    """
    if not subjects:
        raise ValueError("at least one subject is required")

    results = []
    total_earned = 0.0
    total_possible = 0.0
    for name, marks, maximum in subjects:
        if not name.strip():
            raise ValueError("subject names cannot be empty")
        if not isfinite(marks) or not isfinite(maximum):
            raise ValueError("marks must be finite numbers")
        if maximum <= 0:
            raise ValueError("maximum marks must be greater than zero")
        if marks < 0 or marks > maximum:
            raise ValueError(f"marks for {name} must be between 0 and {maximum:g}")
        percentage = marks / maximum * 100
        results.append({"name": name.strip(), "marks": marks, "maximum": maximum,
                        "percentage": percentage, "grade": letter_grade(percentage)})
        total_earned += marks
        total_possible += maximum

    overall_percentage = total_earned / total_possible * 100
    return {
        "subjects": results,
        "average_marks": sum(item["marks"] for item in results) / len(results),
        "overall_percentage": overall_percentage,
        "overall_grade": letter_grade(overall_percentage),
        "total_earned": total_earned,
        "total_possible": total_possible,
    }


def _read_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if not isfinite(value):
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid finite number.")


def main() -> None:
    print("Student Grade Calculator")
    while True:
        try:
            count = int(input("How many subjects? "))
            if count < 1:
                raise ValueError
            break
        except ValueError:
            print("Enter a whole number of at least 1.")

    subjects = []
    for index in range(1, count + 1):
        name = input(f"Subject {index} name: ").strip()
        while not name:
            print("Subject name cannot be empty.")
            name = input(f"Subject {index} name: ").strip()
        maximum = _read_number(f"Maximum marks for {name}: ")
        while maximum <= 0:
            print("Maximum marks must be greater than zero.")
            maximum = _read_number(f"Maximum marks for {name}: ")
        marks = _read_number(f"Marks earned in {name}: ")
        while not 0 <= marks <= maximum:
            print(f"Marks must be between 0 and {maximum:g}.")
            marks = _read_number(f"Marks earned in {name}: ")
        subjects.append((name, marks, maximum))

    report = calculate_report(subjects)
    print("\nResults")
    for subject in report["subjects"]:
        print(f"{subject['name']}: {subject['marks']:g}/{subject['maximum']:g} "
              f"({subject['percentage']:.2f}%) — Grade {subject['grade']}")
    print(f"Average marks per subject: {report['average_marks']:.2f}")
    print(f"Overall: {report['total_earned']:g}/{report['total_possible']:g} "
          f"({report['overall_percentage']:.2f}%) — Grade {report['overall_grade']}")


if __name__ == "__main__":
    main()
