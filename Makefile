venv:
	python3.11 -m venv .venv

activate:
	. .venv/bin/activate   								#	or source .venv/bin/activate

install:
		pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black *.py  										#	format code with black

lint:
	pylint *.py											#	static code analysis tool

all:  venv activate install format lint
