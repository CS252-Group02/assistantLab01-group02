"""Run the assistant benchmark stored in ``eval/cases.csv``."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))

from assistant.rules import reply

CASES_PATH = Path(__file__).with_name("cases.csv")


def load_cases(path: Path = CASES_PATH) -> list[dict[str, str]]:
    """Load benchmark cases and validate their required columns."""
    with path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        required_columns = {"question", "expected", "category"}
        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise ValueError("Benchmark CSV must include question, expected, and category columns.")
        return list(reader)


def run_benchmark(cases: list[dict[str, str]]) -> tuple[int, int]:
    """Return the number of correct answers and total benchmark cases."""
    correct = sum(reply(case["question"]) == case["expected"] for case in cases)
    return correct, len(cases)


def main() -> int:
    try:
        cases = load_cases()
    except (OSError, ValueError) as error:
        print(f"Could not run benchmark: {error}", file=sys.stderr)
        return 1

    correct, total = run_benchmark(cases)
    accuracy = correct / total if total else 0.0
    print(f"Accuracy: {accuracy:.1%} ({correct}/{total})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
