CODE = server

.PHONY: lint format

lint:
	black --line-length=100 --skip-string-normalization --check $(CODE)
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)

format:
	isort --profile black $(CODE)
	black --line-length=100 --skip-string-normalization $(CODE)
	unify --in-place --recursive $(CODE)

install_web:
	npm i

collect:
	./node_modules/.bin/webpack --config webpack.config.js
	./manage.py collectstatic --no-input
