#!/bin/bash
.PHONY: integrate build app app-py venv

venv:
	( \
		python -m pip install --upgrade pip; \
		pip install virtualenv; \
		python -m venv venv; \
		source venv/Scripts/activate; \
		pip install -r requirements.txt; \
	)


# make dockerize ARGS=London
app:
	echo "coucou"

app-py:
	( \
		source venv/Scripts/activate; \
		python main.py; \
	)

################
## CI scripts ##
################
synthax: venv
	( \
		source venv/Scripts/activate; \
		pip install flake8; \
		echo "flake8 analyze :"; \
		flake8 server --count --exit-zero --max-complexity=10 --max-line-length=120 --show-source --statistics; \
		echo "flake8 ended."; \
	)

test: venv
	( \
		source venv/Scripts/activate; \
		pip install coverage; \
		python -m coverage run -m unittest; \
		coverage report -m; \
	)

integrate: test synthax


################
## CD scripts ##
################
build: integrate
	docker build . --tag thibaultsan/auth-app-FastAPI:latest --label auth-app-fastapi
	# docker scan thibaultsan/auth-app-FastAPI:latest