#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

install_requirements:
	pip install -r ./requirements.txt

runserver:
	cd ../server && \
	uvicorn server:app --reload --host 0.0.0.0 --port 4200