from lib.libdata import *
from lib.libutils import *
from lib.libetl import *

class CartDatabase(DatabaseBase):
# {
	def __init__(self, database="marketplace"):
		super().__init__()
		self.connect_loop(database)

	def get_all_carts(self):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = "SELECT * FROM cart;"

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()
		rc = curr.rowcount
		print(rc)

		if not result:
			return -1

		return result

	def get_cart_by_id(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""SELECT * FROM cart as c
		WHERE c.id_cart = '{id}';"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def create_cart(self, cart):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""INSERT INTO cart (id_cart, sum, discount, final_price, id_customer)
		values	(nextval('cartid_seq'), 0, 0, 0, {cart['id_customer']});"""

		try:
			curr.execute(sql_query)
			conn.commit()
		except Exception as e:
			print(str(e))
			self.close()
			return -1
		
		self.close()
		return 0
	
	def update_product(self, cart):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE cart
		SET sum = '{cart['sum']}', discount = {cart['discount']}, final_price = {cart['final_price']}
		WHERE id_cart = '{cart['id_cart']}';"""

		try:
			curr.execute(sql_query)
			conn.commit()
			rc = curr.rowcount
		except Exception as e:
			print(str(e))
		
		self.close()
		return rc

	def delete_cart(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""DELETE from cart where id_cart = '{id}';"""

		curr.execute(sql_query)
		rows_deleted = curr.rowcount
		conn.commit()
		self.close()

		return rows_deleted
# }

def cart_all_get() -> list:
# {
	cd = CartDatabase()
	carts = cd.get_all_carts()
	carts_etl = []

	if carts == -1:
		return []

	for c in carts:
		carts_etl.append(etl_cart(c))

	return carts_etl
# }

def cart_get(id):
# {
	cd = CartDatabase()
	product = cd.get_cart_by_id(id)

	return product
# }

def cart_delete(id):
# {
	cd = CartDatabase()
	rd = cd.delete_cart(id)

	return rd
# }

def cart_post(cart):
# {
	cd = CartDatabase()
	return cd.create_cart(cart.__dict__)
# }

def cart_update(cart):
	cd = CartDatabase()

	return cd.update_cart(cart.__dict__)