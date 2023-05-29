# How to contribute

There are a few guidelines that we need contributors to follow so that we can have a chance of keeping on top of things.

## Getting Started

- Make sure you have a GitHub account.
- Submit your issue if one does not already exist.
  - Clearly describe the issue including steps to reproduce when it is a bug.
  - Make sure you fill in the earliest version that you know has the issue.
- Fork the repository on GitHub.
- Open project in your favorite Editor (Mine is VsCode 😍)
- Install [poetry](https://python-poetry.org/docs/#installation)
- Create Shell

```
poetry shell
```

- Install dependencies

```
poetry install
```

- Start Contributing and Happy Coding 😄

## Making Changes

- Create a `feature`/`fix`/`release` branch from where you want to base your work.
  eg: `feature/{ISSUE-NO}-topic`
  - Please avoid working directly on the main branch.
- Make commits of logical and atomic units.
- Check for unnecessary whitespace with git diff --check before committing.
- Make sure you have added the necessary tests for your changes.
- To run tests:

```
poetry run pytest -v
```

- Make sure to update the requirements.txt file if added a new dependency

```
poetry export -f requirements.txt --output requirements.txt --without-hashes
poetry export -f requirements.txt --with dev --output requirements_dev.txt --without-hashes
```

## Submitting Changes

- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request to the repository with good description of your work.
- The core team looks at pull requests on a regular basis.
- After feedback has been given we expect responses within two weeks. After two weeks we may close the pull request if it isn't showing any activity.
