PYTHON ?= python

.PHONY: check

check:
	$(PYTHON) scripts/check_all.py
