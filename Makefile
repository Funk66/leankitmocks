.PHONY: install clean

install:
	if [ ! -d env ]; then python3 -m venv env; fi
	env/bin/python setup.py develop

publish:
	python3 setup.py sdist upload -r pypi

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.ropeproject' -exec rm -rf {} +
