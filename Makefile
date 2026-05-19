.PHONY: install run format lint test clean

install:
	python3.11 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && uvicorn app.main:app --reload

format:
	. .venv/bin/activate && black app tests
	. .venv/bin/activate && ruff check app tests --fix

lint:
	. .venv/bin/activate && ruff check app tests

test:
	. .venv/bin/activate && pytest

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
