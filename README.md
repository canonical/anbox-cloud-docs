---
orphan: true
---

# Anbox Cloud documentation

This repository hosts the product documentation for Anbox Cloud.

```{important}
The concepts of the Anbox component in Anbox Cloud are similar to the [Anbox open source project](https://github.com/anbox/anbox), but the Anbox open source project is an independent project that is not related to or used in Anbox Cloud.
```

## Contributing to Anbox Cloud documentation
You can contribute to the Anbox Cloud documentation through either of the following channels:
- Report an issue in GitHub
- Raise a pull request with your changes

The Anbox Cloud team will review the issue/pull request and take the necessary action.

### First-time contributors
We welcome your engagement with the Anbox Cloud community and appreciate all contributions, suggestions and feedback. There are many reasons why you should contribute to the Anbox Cloud documentation.

- Improve your skills

    Contributing to the Anbox Cloud docs is a great way to improve your documentation and technical communication skills. You’ll get experience writing clear, concise documentation following [Diátaxis](https://diataxis.fr/) principles.

- Learn more about Anbox Cloud

    Contributing to the Anbox Cloud documentation can help you broaden your understanding of the product and its related technologies. Writing documentation often involves exploring new features and investigating potential problems or challenges users may face, which can help you learn more about how Anbox Cloud works and how users interact with it.

- Connect with the Anbox Cloud user community

    As a user of Anbox Cloud, you’re encouraged to collaborate with other users and participate in discussions in the [Discourse forum](https://discourse.ubuntu.com/c/anbox-cloud/users/148). Contributing to the documentation is a great way to connect with other users and learn from their experiences.

### Style and language

Anbox Cloud documentation follows [Diátaxis](https://diataxis.fr/) principles. Before starting to contribute, we encourage you to familiarise yourself with Diátaxis.

To accommodate different kinds of audience, try to:

- Write content in a tone that’s appropriate for the subject.
- Write inclusively and assume very little prior knowledge of the reader.
- Link or explain phrases, acronyms and concepts that may be unfamiliar, and if unsure, err on the side of caution.

We (mostly) adhere to the [Ubuntu style guide](https://docs.ubuntu.com/styleguide/en). Any deviations from the Ubuntu style guide are documented in the [Anbox Cloud documentation style guide](./contribute/anbox-style-guide.md).

### Quality checks
* The following pre-commit checks are run automatically before every commit:
  - Inclusive language checks (`woke`)
  - Spellcheck (`spellcheck`)

#### Running pre-commit checks

To be able to run these pre-commit checks:

* Install the `pre-commit` package from the Ubuntu repositories.
* Install the `aspell` and `aspell-en` packages from the Ubuntu repositories. This is required by the spellchecker.
* Navigate to the top-level directory of this repository and run `pre-commit install --install-hooks`.

#### Overriding pre-commit checks

Enabling pre-commit checks are optional as these checks are executed on pull requests automatically. If you do not want to run these checks before commits or to skip a particular check, use the following tips:

* To disable the pre-commit hook, use `--no-verify` when running `git commit`.
* To skip a particular pre-commit check, prefix `SKIP=<pre-commit-hook-name>` when running `git commit`.
* To allow a valid word that is regularly used in the documentation but is flagged by `spellcheck`, add the word to `.wordlist.txt`.
* In special cases, there are ways to avoid a particular file or text from being flagged by `woke`. See [woke user guide](https://docs.getwoke.tech/ignore/).
