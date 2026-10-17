# Study Assistant - group02

A starter repository for the **CSC10014 Smart Virtual Assistant** project. The current implementation is a lightweight, rule-based assistant that responds to greetings and answers questions about campus offices using the data in `data/offices.csv`.

## Setup

### Requirements

- Python 3.10 or newer
- Git

### 1. Clone the repository

```bash
git clone https://github.com/CS252-Group02/assistantLab01-group02.git
cd assistantLab01-group02
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install the project and development dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The optional `dev` dependency installs `pytest`, which is used to run the test suite.

## Run

Run the assistant with a single question:

```bash
python -m assistant "where is the training office?"
```

Or start an interactive session:

```bash
python -m assistant
```

Type a question at the `>` prompt. Enter `quit` or `exit` to end the session.

The starter assistant supports greetings and office lookups from `data/offices.csv`. For example, you can ask about the Training Office, Student Affairs, the Library, or the IT Helpdesk. The current version uses simple rules and local CSV data; it does not yet use an AI language model.

## Test

Run all tests from the repository root:

```bash
python -m pytest
```

For more detailed output, use:

```bash
python -m pytest -v
```

The test configuration is defined in `pyproject.toml`, and tests are collected from the `tests/` directory. A successful run reports the number of tests passed; if a test fails, review the failure details printed by `pytest`.

## Evaluation

Run the benchmark from the repository root:

```bash
python eval/run.py
```

The script evaluates the assistant against `eval/cases.csv` and prints its accuracy.

## Project structure

```text
.
├── data/             # Local data used by the assistant (including offices.csv)
├── docs/             # Project documentation
├── scripts/          # Helper scripts
├── src/
│   └── assistant/    # Python package
│       ├── __main__.py  # CLI entry point: python -m assistant
│       └── rules.py     # Rule-based response and office lookup logic
├── tests/            # Automated tests
├── ui/               # User-interface files
├── .gitignore        # Files excluded from version control
├── requirements.txt  # Python test dependencies
├── pyproject.toml    # Package metadata, dependencies, and pytest configuration
└── README.md         # Project setup and usage guide
```

## Data

Office information is stored in `data/offices.csv` with three columns: `name`, `room`, and `hours`. To add or update an office, edit this CSV while keeping the same column names.
