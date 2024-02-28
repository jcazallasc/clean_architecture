build:
	docker-compose build

up:
	docker-compose up

stop:
	docker-compose stop

down:
	docker-compose down

migrations:
	docker-compose run clean_architecture python manage.py makemigrations events_context janto_events_context

migrate:
	docker-compose run clean_architecture python manage.py migrate

showmigrations:
	docker-compose run clean_architecture python manage.py showmigrations

tests:
	docker-compose run clean_architecture python manage.py test

enter:
	docker-compose run clean_architecture bash

isort:
	docker-compose run clean_architecture isort -c .

flake8:
	docker-compose run clean_architecture flake8 .

createsuperuser:
	docker-compose run clean_architecture python manage.py createsuperuser

run: migrations migrate up