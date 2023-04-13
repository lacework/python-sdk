
# Contributing to the Lacework Go-sdk

### Table Of Contents

* [Before getting started?](#before-getting-started)

* [How to contribute](#how-to-contribute)
    * [Reporting Bugs](#reporting-bugs)
    * [Feature Requests](#feature-requests)
    * [Pull Requests](#pull-requests)

* [Developer Guidelines](/DEVELOPER_GUIDELINES.md)


## Before getting started

Read the [README.md](https://github.com/lacework/python-sdk/blob/main/README.md)

### Poetry

```
pyenv install 3.8
pyenv virtualenv 3.8 python-sdk
pyenv local python-sdk

poetry install
poetry run pytest ...

pre-commit install --hook-type commit-msg --hook-type pre-push
```

#### Install Dependencies


https://python-poetry.org/docs/basic-usage/#installing-dependencies

#### Run

```poetry run```

https://python-poetry.org/docs/basic-usage/#installing-dependencies


## How to contribute
There are 3 ways that community members can help contribute to the Lacework Python SDK. Reporting any issues you may find in the functionality or documentation. Or if you believe some functionality should exist within the SDK you can make a feature request. Finally, if you've gone one step further and made the changes to submit for a pull request.

### Reporting Bugs

Ensure the issue you are raising has not already been created under [issues](https://github.com/lacework/python-sdk/issues).

If no current issue addresses the problem, open a new [issue](https://github.com/lacework/python-sdk/issues/new).
Include as much relevant information as possible. See the [bug template](https://github.com/lacework/python-sdk/blob/main/.github/ISSUE_TEMPLATE/bug_report.md) for help on creating a new issue.

### Feature Requests

If you wish to submit a request to add new functionality or an improvement to the go-sdk then use the the [feature request](https://github.com/lacework/python-sdk/blob/main/.github/ISSUE_TEMPLATE/feature_request.md) template to
open a new [issue](https://github.com/lacework/python-sdk/issues/new)

### Pull Requests

When submitting a pull request follow the [commit message standard](DEVELOPER_GUIDELINES.md#commit-message-standard).


Thanks,
Project Maintainers
