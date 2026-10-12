# Student Grade Calculator

A small Python 3.13 command-line app for recording marks across subjects and reviewing per-subject results plus an overall percentage and letter grade. The overall percentage is weighted by each subject's maximum marks; the displayed average is the mean of marks earned per subject.

## Grade scale

| Percentage | Grade |
|---:|:---|
| 90–100 | A |
| 80–<90 | B |
| 70–<80 | C |
| 60–<70 | D |
| 0–<60 | F |

Marks must be finite and between 0 and the subject's maximum, which must be greater than zero.

## Run

```powershell
python grade_calculator.py
```

Follow the prompts to enter the number of subjects, each subject name, maximum marks, and marks earned.

## Test

```powershell
python -m unittest -v
```

Only the Python standard library is used.
