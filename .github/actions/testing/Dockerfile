# Starting from Python 3 base image
FROM python:3.7-alpine

LABEL "com.github.actions.name"="Pytesting"
LABEL "com.github.actions.description"="Run pytest on problem code."
LABEL "com.github.actions.icon"="layers"
LABEL "com.github.actions.color"="yellow"

# Set the WORKDIR to /EoPI so all following commands run in /EoPI
WORKDIR /EoPI

# copy project to workdir
COPY . .


# RUN ["chmod", "+x", "./.github/actions/testing/entrypoint.sh"]
ENTRYPOINT ["./.github/actions/testing/entrypoint.sh"]