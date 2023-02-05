from lib.libapi import product, product_type, customer

def etl_product(p):
# {
	data = product()

	data.id_product = p[0]
	data.cod_product = p[1]
	data.description = p[2]
	data.unit = p[3]
	data.price = float(p[4])
	data.id_type = p[5]

	return data
# }

def etl_product_type(p):
# {
	data = product_type()

	data.id_type = p[0]
	data.description = p[1]

	return data

def etl_customer(c):
# {
	data = customer()

	data.id_customer = c[0]
	data.name = c[1]
	data.phone = c[2]

	return data
# }