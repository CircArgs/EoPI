#!/usr/bin/env bash
printenv
pip3 install pipenv;
pipenv install;
pipenv run python -m pytest --cov=. >> $GITHUB_WORKSPACE/coverage_summary
pipenv run python .github/actions/testing/make_coverage_badge.py
cat $GITHUB_WORKSPACE/coverage_summary
tree

