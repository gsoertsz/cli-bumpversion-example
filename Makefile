
.PHONY: install test lint clean build docs all
.ONESHELL:

install:
	pip install -r requirements-dev.txt
	pip install -r requirements.txt

TARGET ?= hello/tests
test:
	pytest --cov=hello --no-cov-on-fail --cov-report=html --junit-xml=unittest_output.xml $(TARGET)

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

lint-hard:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

docs:
	sphinx-apidoc --ext-autodoc -f -o docs/source hello "tests"
	sphinx-build -M html docs/source docs/build

docs-clean:
	rm -rf docs/build/*

COVLINT_FILES = cov.xml coverage.xml pytest-report.xml pylint-report.txt htmlcov unittest*.xml
clean: docs-clean
	rm -rf $(COVLINT_FILES) 
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf dist .pytest_cache
	rm -rf unittest_output.xml
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

build:
	python -m build --sdist

all: clean test lint install build docs
