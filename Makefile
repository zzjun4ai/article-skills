PYTHON ?= python

.PHONY: check

check:
	$(PYTHON) -m unittest discover -s skills/data-to-nature-figure/tests -t skills/data-to-nature-figure -v
