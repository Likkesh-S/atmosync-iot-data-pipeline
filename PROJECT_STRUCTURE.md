# AtmoSync — Project Structure

> This document describes how the **AtmoSync** repository is organised.
> Replace or trim any section below so it matches the actual repo.

## Overview

AtmoSync is organised into clearly separated layers so each part can be developed, tested, and deployed independently.

## Directory Tree

```
AtmoSync/
├── .github/
│   └── workflows/          # CI/CD pipelines (lint, test, build, deploy)
├── docs/                   # Extra documentation, diagrams, API notes
├── src/
│   ├── api/                # Route handlers / API endpoints
│   ├── services/           # Business logic (data sync, processing)
│   ├── models/             # Data models and schemas
│   ├── utils/              # Shared helpers and utilities
│   ├── config/             # App configuration and environment loading
│   └── main.*              # Application entry point
├── tests/
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── scripts/                # Setup, migration, and maintenance scripts
├── public/ (or assets/)    # Static files and images
├── .env.example            # Sample environment variables
├── .gitignore
├── LICENSE
├── README.md
├── PROJECT_STRUCTURE.md    # This file
└── package.json / requirements.txt   # Dependencies
```

## Folder Descriptions

| Path | Purpose |
|------|---------|
| `.github/workflows/` | Automated checks and deployment on push or pull request |
| `docs/` | Architecture notes, API references, design decisions |
| `src/api/` | Entry points that receive requests and return responses |
| `src/services/` | Core logic; keeps API handlers thin |
| `src/models/` | Definitions of data structures and validation |
| `src/utils/` | Reusable functions with no side effects |
| `src/config/` | Central place for settings and environment variables |
| `tests/` | Automated tests mirroring the `src/` layout |
| `scripts/` | One-off and recurring developer scripts |

## Key Files

- **README.md**: project introduction, setup, and usage
- **.env.example**: lists required environment variables (never commit real secrets)
- **LICENSE**: licensing terms
- **PROJECT_STRUCTURE.md**: this guide

## Conventions

- Keep business logic in `services/`, not in route handlers.
- Mirror the `src/` folder layout inside `tests/`.
- Store secrets only in `.env` (git-ignored); update `.env.example` when adding new variables.
- Update this document whenever folders are added, moved, or removed.

## Getting Started

```bash
git clone <repository-url>
cd AtmoSync
cp .env.example .env
# install dependencies, then run the app
```
