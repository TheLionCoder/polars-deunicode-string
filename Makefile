SHELL=/bin/bash

## Install dependencies
.PHONY: .venv
.venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt



.PHONY: install
install: .venv
	unset CONDA_PREFIX && \
	source .venv/bin/activate && \
	python3 -m pip install --upgrade pip && \
	maturin develop

.PHONY: install-release
install-release: .venv
	unset CONDA_PREFIX && \
	source .venv/bin/activate && maturin develop --release

.PHONY: pre-commit
pre-commit: .venv
	cargo fmt --all && cargo clippy --all-features
	.venv/bin/python -m ruff check . --fix --exit-non-zero-on-fix
	.venv/bin/python -m ruff format polars_deunicode_string tests
	.venv/bin/mypy polars_deunicode_string tests

.PHONY: test
test: .venv
	.venv/bin/python -m pytest tests

.PHONY: run
run: install
	source .venv/bin/activate && python run.py

.PHONY: run-release
run-release: install-release
	source .venv/bin/activate && python run.py

.PHONY: clean
clean:
	find . -type f -name "*py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf target
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
