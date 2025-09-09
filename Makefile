.PHONY: setup up ingest plan run dryrun down test

setup:
	docker compose build

up:
	docker compose up -d

ingest:
	docker compose run --rm runner python -m agent.main ingest $(DOCS)

plan:
	docker compose run --rm runner python -m agent.main plan "$(TASK)"

run:
	docker compose run --rm -e MODE=$(MODE) runner python -m agent.main run "$(CMD)"

dryrun:
	docker compose run --rm runner python -m agent.main dryrun "$(CMD)"

down:
	docker compose down

test:
	pytest -q
