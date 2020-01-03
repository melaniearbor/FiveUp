Getting Started
===============


Testing
=======

The following will run the entire test suite and print an interactive html coverage report to the
directory `cov_html`. You can then open `cov_html/index.html` in your browser to inspect
coverage. All PRs must maintain 100% test coverage.

``pytest --cov-report html:cov_html --cov=.``
