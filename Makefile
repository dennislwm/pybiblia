.PHONY: default install test verbose

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src/pybiblia pytest

verbose:
	PYTHONPATH=./src/pybiblia pytest -v -s
