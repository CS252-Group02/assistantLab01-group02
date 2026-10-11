"""
check_env.py — Verify the developer environment for assistantLab01-group02.

Run:  python scripts/check_env.py
Every line should end with  [ OK ]
"""
from __future__ import annotations

import importlib
import shutil
import subprocess
import sys
from pathlib import Path

# ── Colours (disabled on Windows if colorama is absent) ─────────────────────
try:
    import colorama  # type: ignore

    colorama.init()
    GREEN = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"
except ImportError:
    GREEN = RED = RESET = ""

OK = f"{GREEN}[ OK ]{RESET}"
FAIL = f"{RED}[FAIL]{RESET}"

ROOT = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


# ── Helper ───────────────────────────────────────────────────────────────────
def check(label: str, passed: bool, hint: str = "") -> None:
    tag = OK if passed else FAIL
    print(f"  {tag}  {label}")
    if not passed:
        if hint:
            print(f"        > {hint}")
        FAILURES.append(label)


# ── 1. Python version ────────────────────────────────────────────────────────
def check_python() -> None:
    print("\n[Python]")
    ver = sys.version_info
    ok = ver >= (3, 10)
    check(
        f"Python >= 3.10  (found {ver.major}.{ver.minor}.{ver.micro})",
        ok,
        "Upgrade to Python 3.10+",
    )


# ── 2. Required packages ─────────────────────────────────────────────────────
REQUIRED_PACKAGES = [
    ("pytest", "pytest"),
    ("assistant", "assistant"),   # the local package itself
]


def check_packages() -> None:
    print("\n[Packages]")
    for display, module in REQUIRED_PACKAGES:
        try:
            importlib.import_module(module)
            check(f"import {display}", True)
        except ImportError:
            check(
                f"import {display}",
                False,
                f"Run: pip install {display}" if display != "assistant"
                else "Run: pip install -e .",
            )


# ── 3. CLI tools ─────────────────────────────────────────────────────────────
def check_tools() -> None:
    print("\n[CLI tools]")
    for tool in ("git", "pytest"):
        found = shutil.which(tool) is not None
        check(f"{tool} on PATH", found, f"Install {tool} and add it to PATH")


# ── 4. Project files ─────────────────────────────────────────────────────────
REQUIRED_FILES = [
    "README.md",
    ".gitignore",
    "src/assistant/__init__.py",
    "src/assistant/rules.py",
    "data/offices.csv",
    "tests/test_smoke.py",
    "scripts/check_env.py",
]


def check_files() -> None:
    print("\n[Project files]")
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        check(rel, path.exists(), f"Missing: {path}")


# ── 5. assistant package imports & basic smoke ────────────────────────────────
def check_assistant() -> None:
    print("\n[Assistant module]")
    try:
        from assistant.rules import reply  # noqa: PLC0415

        check("assistant.rules.reply importable", True)

        result = reply("hi")
        check(
            "reply('hi') returns a greeting",
            "Hello" in result,
            f"Got: {result!r}",
        )

        result2 = reply("Where is the Training Office?")
        check(
            "reply contains room I.101 for Training Office",
            "I.101" in result2,
            f"Got: {result2!r}",
        )

        result3 = reply("   ")
        check(
            "reply('   ') returns 'Please type a question.'",
            result3 == "Please type a question.",
            f"Got: {result3!r}",
        )
    except Exception as exc:  # noqa: BLE001
        check(f"assistant.rules import/smoke ({exc})", False)


# ── 6. pytest smoke tests ─────────────────────────────────────────────────────
def check_pytest() -> None:
    print("\n[pytest smoke tests]")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-q", "--tb=short"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    passed = result.returncode == 0
    # Show a condensed summary line from pytest output
    for line in result.stdout.splitlines():
        if "passed" in line or "failed" in line or "error" in line:
            summary = line.strip()
            break
    else:
        summary = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "no output"

    check(f"pytest tests/  ({summary})", passed, "Run: pytest -v  for details")
    if not passed and result.stdout:
        for line in result.stdout.splitlines()[-10:]:
            print(f"        {line}")


# ── 7. data/offices.csv has expected columns ─────────────────────────────────
def check_data() -> None:
    print("\n[Data files]")
    import csv  # noqa: PLC0415

    csv_path = ROOT / "data" / "offices.csv"
    if not csv_path.exists():
        check("data/offices.csv readable", False, "File missing")
        return
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or []
            rows = list(reader)
        has_cols = {"name", "room", "hours"}.issubset(set(fieldnames))
        check(
            f"offices.csv has required columns (name, room, hours)",
            has_cols,
            f"Found columns: {fieldnames}",
        )
        check(
            f"offices.csv has >= 1 data row (found {len(rows)})",
            len(rows) >= 1,
        )
    except Exception as exc:  # noqa: BLE001
        check(f"offices.csv readable ({exc})", False)


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> int:
    print("=" * 54)
    print("  Environment check — assistantLab01-group02")
    print("=" * 54)

    check_python()
    check_packages()
    check_tools()
    check_files()
    check_assistant()
    check_pytest()
    check_data()

    print("\n" + "=" * 54)
    if FAILURES:
        print(f"{RED}  {len(FAILURES)} check(s) FAILED:{RESET}")
        for f in FAILURES:
            print(f"    • {f}")
        print("=" * 54)
        return 1
    else:
        print(f"{GREEN}  All checks passed!{RESET}")
        print("=" * 54)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
