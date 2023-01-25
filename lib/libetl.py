from lib.libapi import product

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