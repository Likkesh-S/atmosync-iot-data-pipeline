# Contributing to AtmoSync

Thanks for your interest in contributing to **AtmoSync**! This guide explains how to report issues, propose changes, and get your work merged smoothly.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Project Structure](#project-structure)

## Code of Conduct

Be respectful, patient, and constructive. Harassment or discrimination of any kind is not tolerated. Maintainers may remove comments, commits, or contributions that violate this principle.

## Ways to Contribute

- Report bugs
- Suggest new features or improvements
- Improve documentation
- Fix issues or implement features
- Review pull requests

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/AtmoSync.git
   cd AtmoSync
   ```
3. **Add the upstream remote:**
   ```bash
   git remote add upstream https://github.com/<owner>/AtmoSync.git
   ```
4. **Set up the environment:**
   ```bash
   cp .env.example .env
   # install dependencies (e.g. npm install / pip install -r requirements.txt)
   ```
5. **Run the project** and confirm everything works before making changes.

## Development Workflow

1. Sync your fork with upstream:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feature/short-description
   ```
   Branch prefixes: `feature/`, `fix/`, `docs/`, `refactor/`, `test/`.
3. Make your changes in small, focused commits.
4. Run tests and linters locally.
5. Push your branch and open a pull request.

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(optional scope): <short summary>
```

Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

Examples:

```
feat(api): add weather sync endpoint
fix(services): handle empty response from provider
docs: update PROJECT_STRUCTURE.md
```

## Pull Request Process

1. Make sure your branch is up to date with `main`.
2. Ensure all tests pass and linting is clean.
3. Fill in the PR description: what changed, why, and how to test it.
4. Link related issues (e.g. `Closes #12`).
5. Update documentation (`README.md`, `PROJECT_STRUCTURE.md`) if your change affects them.
6. Request a review and address feedback promptly.

A PR is merged once it has at least one maintainer approval and passing checks.

## Coding Standards

- Follow the existing style and naming conventions in the codebase.
- Keep functions small and focused; put business logic in `services/`, not route handlers.
- Write clear comments for non-obvious logic.
- Never commit secrets, API keys, or `.env` files.
- Update `.env.example` when adding new environment variables.

## Testing

- Add or update tests for every bug fix and new feature.
- Place tests under `tests/` mirroring the `src/` layout (`unit/` and `integration/`).
- Run the full test suite before opening a PR.

## Reporting Bugs

Open an issue and include:

- A clear, descriptive title
- Steps to reproduce
- Expected vs. actual behaviour
- Environment details (OS, versions)
- Logs or screenshots, if relevant

## Suggesting Features

Open an issue describing:

- The problem you want to solve
- Your proposed solution
- Alternatives you considered

Discussing an idea before writing code helps avoid duplicated or rejected work.

## Project Structure

See [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) for an overview of how the repository is organised.

## Questions?

Open a discussion or issue, and a maintainer will get back to you.

Thank you for helping make AtmoSync better!
