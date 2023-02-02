#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

install_requirements:
	pip install -r ./requirements.txt

runserver:
	cd ../scripts && \
	chmod +x runapis.sh && \
	./runapis.sh

start_database:
	cd ../scripts/sql && \
	psql -U postgres -h localhost -c "CREATE DATABASE marketplace;" && \
	psql -U postgres -h localhost -d marketplace -a -f create_product_data.sql && \
	psql -U postgres -h localhost -d marketplace -a -f create_cart_data.sql

cleandata:
	psql -U postgres -h localhost -c "DROP DATABASE marketplace;"

log:
	cd ../log/api/ && \
	tail -f *api.log