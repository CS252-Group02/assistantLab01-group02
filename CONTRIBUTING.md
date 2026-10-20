# Contributing

## Development Setup

1. Clone the repository.
2. Follow the setup instructions in `README.md`.
3. If environment variables are required, copy `.env.example` to `.env` and configure your local values.

## Secrets

- Never commit API keys, passwords, access tokens, or private keys.
- Store local secrets in `.env`.
- Use `.env.example` to document required environment variables with placeholder values only.
- Ensure `.env` is ignored by Git.
- Never put real secrets in source code, documentation, logs, or pull requests.
- If a secret is accidentally committed, revoke or rotate it immediately and notify the team.

## Pull Requests

- Work on a feature branch rather than directly on `main`.
- Add or update tests when appropriate.
- Explain your changes and testing in the pull request.
- Disclose any AI assistance used in the pull request.

