# Including commands
run-django-server:
	poetry run task server localhost:8000

install-backend:
	poetry run pip install -U setuptools
	poetry install --no-root

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

# Primary commands
.PHONY: install
install:
	@make install-backend
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: install-prod
install-prod:
	poetry run pip install -U pip
	@make install-backend
	poetry run task initconfig

.PHONY: run
run:
	@make run-django-server

.PHONY: build
build:
	poetry run task collectstatic
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: install-host
install-host:
	python3 -m poetry run pip install -U setuptools
	python3 -m poetry install --no-root
	python3 -m poetry run task collectstatic
	python3 -m poetry run task migrate
	python3 -m run task defaultadmin
