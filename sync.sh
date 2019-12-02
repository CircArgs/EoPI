#!/usr/bin/env bash

set -e
black .
git add .
git commit -m $0
git push