# Codex Mini (FREE)

Lightweight CLI agent system running entirely in Docker.

## Quickstart

```
make setup && make up
make ingest DOCS=./examples/target_repo
make plan TASK="Install & run"
make run MODE=auto
# Kill-switch
docker compose down
```
