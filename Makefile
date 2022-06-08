install:
	pip3 install --upgrade pip && \
		pip3 install -r requirements.txt
format:
	black mylib/*.py tests/*.py
lint: 
	pylint --disable=R,C mylib/*.py tests/*.py

all: install format lint