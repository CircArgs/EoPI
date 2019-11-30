#!/usr/bin/env bash

pip3 install pipenv;
pipenv install;
pipenv run python -m pytest --cov=. >> $GITHUB_WORKSPACE/coverage_summary
