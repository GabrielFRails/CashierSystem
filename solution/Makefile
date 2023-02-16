#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

install_requirements:
	pip install -r ./requirements.txt

runall: rm_log_dir create_log_dir runserver

runserver:
	cd ../scripts && \
	chmod +x runapis.sh && \
	./runapis.sh

create_log_dir:
	mkdir ../log

rm_log_dir:
	sudo rm -f -r ../log

start_database:
	cd ../scripts/sql && \
	psql -U postgres -h localhost -c "CREATE DATABASE marketplace;" && \
	psql -U postgres -h localhost -d marketplace -a -f create_product_data.sql && \
	psql -U postgres -h localhost -d marketplace -a -f create_cart_data.sql

cleandata:
	psql -U postgres -h localhost -c "DROP DATABASE marketplace;"

restart_database: cleandata start_database

log:
	cd ../log/ && \
	tail -f *api.log