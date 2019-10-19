.PHONY: all clean install test test_int test_all uninstall

all: install

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

install:
	python setup.py install

test:
	pytest -v --cov --cov-config=tox.ini tests/unit

test_integration:
	pytest -v tests/integration

test_all:
	pytest -v --cov --cov-config=tox.ini tests

uninstall:
	pip uninstall globalentry
