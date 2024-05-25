build:
	@docker-compose build

up:
	@docker-compose up

down:
	@docker-compose down

test:
	@docker-compose run --rm app pytest -s

rebuild:
	@docker-compose down
	@docker-compose build
	@docker-compose up
