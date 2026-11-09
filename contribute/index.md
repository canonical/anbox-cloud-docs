---
myst:
  html_meta:
    "description": "How to contribute to Anbox Cloud documentation by fixing errors, adding content, or raising issues."
---

(contribute)=
# Contribute to Anbox Cloud documentation

Although Anbox Cloud is a closed-source product, its documentation is open to contributions and is available at the [Anbox Cloud documentation repository](https://github.com/canonical/anbox-cloud-docs). If something is inaccurate, unclear or missing, we welcome your feedback and fixes.

## Ways to contribute

- Propose a fix by [opening a pull request](https://github.com/canonical/anbox-cloud-docs/pulls) in the documentation repository.
- Report a documentation issue,  such as a broken link or a command that no longer works, on [GitHub](https://github.com/canonical/anbox-cloud-docs/issues/new).
- Report an Anbox Cloud product bug on [Launchpad](https://bugs.launchpad.net/anbox-cloud/+filebug). Include the steps to reproduce it and any relevant command output.
- Ask a question or discuss an improvement in the [public Matrix channel](https://matrix.to/#/#anbox-cloud:ubuntu.com) or the [Anbox Cloud forum](https://discourse.ubuntu.com/c/project/anbox-user/148).

## How the docs are built

Anbox Cloud documentation is built with [Sphinx](https://www.sphinx-doc.org/) using [Canonical's Sphinx Stack](https://github.com/canonical/sphinx-stack). It is hosted on [Read the Docs](https://about.readthedocs.com/).

We write the source files in [Markdown](https://commonmark.org/) with [MyST](https://myst-parser.readthedocs.io/) extensions. For syntax help and guidelines, see the [MyST syntax guide](https://documentation.ubuntu.com/sphinx-stack/latest/reference/myst-syntax/) in the [Sphinx Stack documentation](https://documentation.ubuntu.com/sphinx-stack/latest/).

We use the [Diátaxis](https://diataxis.fr/) framework to organize the documentation into tutorials, how-to guides, reference and explanation. Follow the {ref}`style-guide` for Anbox Cloud conventions on terminology, formatting and cross-references.

## Contribute a change

### Before you start

Contributing to our documentation is straightforward. We only require that all contributors sign the [Canonical contributor license agreement](https://canonical.com/legal/contributors).

### Set up your working copy

To submit a change, you need a GitHub account and a [git environment](https://canonical-open-documentation-academy.readthedocs.io/en/latest/docs/howto/get-started/using_git/).

If you're new to Git, see the [Canonical Open Documentation Academy's getting started guide](https://canonical-open-documentation-academy.readthedocs.io/en/latest/docs/howto/get-started/).

Fork the documentation repository, clone your fork and create a branch for your change.

### Edit the source

For a small fix, you can open a pull request directly. If you're planning a larger change, such as rewriting a guide or updating several pages, consider opening a GitHub issue first to discuss the scope with the maintainers.

Edit the relevant Markdown files in your branch. If you move or rename a page, add an entry in `redirects.txt` using the format `"old.md" "new.md"`. Both paths are relative to the repository root.

### Preview your changes locally

Run the following command from the repository root.

```bash
make run
```

The first run creates a Python virtual environment and installs the build dependencies. Open the page you changed in the local preview (`http://127.0.0.1:8000`) and check any headings, links, code blocks, tabs or admonitions you edited. The site rebuilds when you save changes.

### Run documentation checks locally

Before pushing your changes, run the following checks from the repository root.

- `make spelling` checks spelling.
- `make linkcheck` checks links.
- `make lint-md` checks Markdown formatting.
- `make woke` checks inclusive language.

For optional local checks, use `make vale` for style and `make pa11y` for accessibility.

### Submit and preview your pull request

Commit your changes and push your branch to your fork. Then [open a pull request](https://github.com/canonical/anbox-cloud-docs/compare) targeting main in the Anbox Cloud documentation repository. Describe what changed and link to the issue if there is one.

GitHub Actions automatically checks spelling, links and inclusive language on your pull request. If a check fails, open its details to see what needs fixing.

Before your pull request can be merged, all required checks must pass and a maintainer must approve it.

## Get help

If you're unsure about a convention or a check, you can still submit your changes. Ask in your pull request or in the public Matrix channel, and we can help during review.

```{toctree}
:hidden:
Style guide <anbox-style-guide>
```
