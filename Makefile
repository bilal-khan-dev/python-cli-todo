install:
	pip3 install --upgrade pip && \
		pip3 install -r requirements.txt
format:
	black mylib/*.py
lint: 
	pylint --disable=R,C mylib/*.py

all: install format lint