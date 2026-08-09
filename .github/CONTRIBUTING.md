# Contributing

Thanks for taking the time to contribute.

## Getting started

You will need [uv](https://docs.astral.sh/uv/getting-started/installation/) and a
Discord bot token for testing.

```sh
git clone https://github.com/blocksandbuddies/discord-allay.git
cd discord-allay
uv sync
cp .env.example .env
uv run allay
```

Test against your own private server rather than a live community one.

## Making a change

1. Open an issue first for anything substantial, so we can agree on the approach
   before you spend time on it. Small fixes can go straight to a pull request.
2. Branch off `main`.
3. Make your change, keeping it focused on one thing.
4. Run the checks below.
5. Open a pull request describing what changed and why.

## Checks

```sh
uv run ruff check --fix
uv run ruff format
```

Both must pass before a pull request can be merged.

## Style

- Follow the conventions already in the surrounding code.
- Use type hints on function signatures.
- Write docstrings for anything public.
- Keep commit messages short and in the imperative mood ("Add ping command").

## Reporting bugs

Open an issue with what you expected, what happened, and the steps to reproduce
it. Include any relevant log output.

Do not open a public issue for security vulnerabilities — see
[SECURITY.md](SECURITY.md).

## Code of Conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By taking part,
you agree to uphold it.
