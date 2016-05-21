UID = $(shell id -u $$USER)
GID = $(shell id -g $$USER)

default: up

install:
	@cp .env-example .env

	@docker-compose rm -f
	@docker-compose stop

	@docker-compose build

	@docker-compose up -d postgres
	@sleep 30
	@docker-compose stop postgres

	@docker-compose run --rm web python manage.py migrate
	@docker-compose run --rm web python manage.py createsuperuser --username=admin --email=admin@admin.com
	@docker-compose run --rm bower --allow-root --config.interactive=false install

fix-perms:
	docker-compose run --rm --entrypoint bash --no-deps web -c "chown -R $(UID):$(GID) ."

build:
	@docker-compose build

up:
	@docker-compose up --force-recreate --no-deps web postgres

bower-install:
	@docker-compose run --rm bower --allow-root --config.interactive=false install

migrations:
	@docker-compose run --rm web python manage.py makemigrations

migrate:
	@docker-compose run --rm web python manage.py migrate

createsuperuser:
	@docker-compose run --rm web python manage.py createsuperuser

test:
	@docker-compose run --rm web coverage run --source=. --omit=*/wsgi.py manage.py test --keepdb --failfast
	@docker-compose run --rm web coverage report -m --fail-under 90
	@docker-compose run --rm web coverage html

flake8:
	@docker-compose run --rm web flake8 . --max-line-length=99 --max-complexity=8 --exclude="*/migrations/**"

clear:
	@rm -fr bower_components/
	@rm -fr node_modules/
	@rm -fr .coverage
	@rm -fr html_cov/
