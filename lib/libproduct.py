from lib.libdata import *
from lib.libutils import *
from lib.libetl import *

class ProductDatabase(DatabaseBase):
# {
	def __init__(self, database="market_place"):
		super().__init__()
		self.connect_loop(database)

	def get_all_product_types(self):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		curr.execute("SELECT * FROM product_type;")
		result = curr.fetchall()
		self.close()

		if not len(result):
			return -1
		
		return result
    
	def get_product_type(self, ptype):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""SELECT * FROM product_type as pt
		WHERE pt.description = '{ptype}';"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def get_all_products(self):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = "SELECT * FROM product;"

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def get_product_by_id(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""SELECT * FROM product as p
		WHERE p.id_product = {id};"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def put_product(self, product, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""INSERT INTO product (id_product, cod_product, description, unit, price, id_type)
		values	('{id}', {product['cod_product']}, '{product['description']}', {product['unit']}, {product['price']}, {product['id_type']});"""

		curr.execute(sql_query)
		conn.commit()
		self.close()
# }

def product_all_types_get():
# {
    pd = ProductDatabase()
    product_types = pd.get_all_product_types()

    return product_types
# }

def product_type_get(product_type):
# {
	pd = ProductDatabase()
	product_type = pd.get_product_type(product_type)

	return product_type
# }

def product_all_get():
# {
	pd = ProductDatabase()
	products = pd.get_all_products()
	products_etl = []

	for p in products:
		products_etl.append(etl_product(p))

	return products_etl
# }

def product_get(id):
# {
	pd = ProductDatabase()
	product = pd.get_product_by_id(id)

	return product
# }

def product_put(product):
# {
	pd = ProductDatabase()

	id = 'CS_%s_TYPE%s' % (utils_generate_id(), product.id_type)
	print(id)

	return pd.put_product(product.__dict__, id)
# }