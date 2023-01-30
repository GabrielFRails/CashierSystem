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
		WHERE p.id_product = '{id}';"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def create_product(self, product, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""INSERT INTO product (id_product, cod_product, description, unit, price, id_type)
		values	('{id}', {product['cod_product']}, '{product['description']}', {product['unit']}, {product['price']}, {product['id_type']});"""

		try:
			curr.execute(sql_query)
			conn.commit()
		except Exception as e:
			print(str(e))
			self.close()
			return -1
		
		self.close()
		return 0
	
	def update_product(self, product):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE product
		SET description = '{product['description']}', unit = {product['unit']}, price = {product['price']}
		WHERE id_product = '{product['id_product']}';"""

		try:
			curr.execute(sql_query)
			conn.commit()
			rc = curr.rowcount
		except Exception as e:
			print(str(e))
		
		self.close()
		return rc

	def delete_product(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""DELETE from product where id_product = '{id}';"""

		curr.execute(sql_query)
		rows_deleted = curr.rowcount
		conn.commit()
		self.close()

		return rows_deleted
# }

def product_all_types_get():
# {
    pd = ProductDatabase()
    product_types = pd.get_all_product_types()

    return product_types
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

def product_delete(id):
# {
	pd = ProductDatabase()
	rd = pd.delete_product(id)

	return rd
# }

def product_post(product):
# {
	pd = ProductDatabase()

	id = 'CS_%s_TYPE%s' % (utils_generate_id(), product.id_type)

	return pd.create_product(product.__dict__, id)
# }

def product_update(product):
	pd = ProductDatabase()

	return pd.update_product(product.__dict__)