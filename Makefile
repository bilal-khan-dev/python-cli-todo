install:
	pip3 install --upgrade pip && \
		pip3 install -r requirements.txt
format:
	black mylib/*.py tests/*.py
lint: 
	pylint --disable=R,C mylib/*.py tests/*.py

test:
	python3 -m pytest tests/

all: install format lint