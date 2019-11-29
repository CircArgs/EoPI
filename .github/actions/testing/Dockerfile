FROM python:3.7

LABEL "com.github.actions.name"="GitHub Action for pytest"
LABEL "com.github.actions.description"="Run pytest commands"
LABEL "com.github.actions.icon"="upload-cloud"
LABEL "com.github.actions.color"="yellow"

COPY . .
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
