#!/usr/bin/env bash

pip3 install pipenv
pipenv install
pipenv run pytest --cov=.
