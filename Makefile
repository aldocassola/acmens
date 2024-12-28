#
# SPDX-License-Identifier: AGPL-3.0-only
#
# Copyright © 2020-2022 siddharth ravikumar <s@ricketyspace.net>
#
VENV_DIR=.venv
VENV=virtualenv

fmt:
	black acmensse.py setup.py
.PHONY: fmt

venv:
	test -d ${VENV_DIR} || ${VENV} --python=python3 ${VENV_DIR}
.PHONY: venv

editable:
	@python3 -m pip install --editable .
	@pip install -U pip black twine
.PHONY: editable

build:
	@python3 -m build
.PHONY: build

upload:
	@python3 -m twine upload -r acmensse -s -i \
		'6EF4 5AA3 7C1F F642 5620 B7E2 8545 3F6B 2786 0675' \
		dist/*.tar.gz
	@python3 -m twine upload -r acmensse -s -i \
		'6EF4 5AA3 7C1F F642 5620 B7E2 8545 3F6B 2786 0675' \
		dist/*.whl
.PHONY: upload

clean:
	@python3 setup.py clean
	@rm -rf build/ dist/ *.egg-info __pycache__/
	@find . -name '*.pyc' -exec rm -f {} +
.PHONY: clean
