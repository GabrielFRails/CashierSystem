#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from lib.libdata import *
from lib.libutils import *
from lib.libetl import *
from lib.libproduct import product_price_get

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

		sql_query = f"""INSERT INTO cart (id_cart, sum, discount, final_price, id_customer, cart_status)
		values	(nextval('cartid_seq'), 0, 0, 0, {cart['id_customer']}, 'open');"""

		try:
			curr.execute(sql_query)
			conn.commit()
		except Exception as e:
			print(str(e))
			self.close()
			return -1
		
		self.close()
		return 0
	
	def update_cart(self, cart):
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

	def add_discount(self, id_cart, discount):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE cart
		SET discount = {discount}
		WHERE id_cart = {id_cart};"""

		try:
			curr.execute(sql_query)
			conn.commit()
			rc = curr.rowcount
		except Exception as e:
			print(str(e))
		
		self.close()
		return rc

	def set_final_price(self, id_cart, final_price):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE cart
		SET final_price = {final_price}
		WHERE id_cart = {id_cart};"""

		try:
			curr.execute(sql_query)
			conn.commit()
			rc = curr.rowcount
		except Exception as e:
			print(str(e))
		
		self.close()
		return rc

	def close_cart(self, id_cart):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE cart
		SET cart_status = 'closed'
		WHERE id_cart = {id_cart};"""

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

	def add_cart_product(self, id_cart, id_product, quantity):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""
			INSERT INTO cart_products (id_cart, id_product, quantity)
			values ({id_cart}, {id_product}, {quantity})
		"""

		try:
			curr.execute(sql_query)
			conn.commit()
		except Exception as e:
			print(str(e))
			self.close()
			return -1
		
		self.close()
		return 0

	def get_cart_products(self, id_cart):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""SELECT * FROM cart_products as c
		WHERE c.id_cart = '{id_cart}';"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result
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
# {
	cd = CartDatabase()

	return cd.update_cart(cart.__dict__)
# }

def cart_add_discount(id_cart, discount):
	cd = CartDatabase()

	cd.add_discount(id_cart, discount)

def cart_add_sum(id_cart, sum, discount):
	cd = CartDatabase()

	if discount > 0:
		sum = sum - (sum * discount / 100)

	return cd.set_final_price(id_cart, sum)

def cart_productlist(id_cart, id_product, quantity):
# {
	cd = CartDatabase()

	return cd.add_cart_product(id_cart, id_product, quantity)
# }

def cart_products_get(id_cart):
# {
	cd = CartDatabase()

	return cd.get_cart_products(id_cart)
# }

def cart_calculate_sum(product_list):
# {
	sum = 0
	for p in product_list:
		id_product = p.get('id_product')
		p_price = product_price_get(id_product)
		p_final_price = p_price * float(p.get('product_quantity'))

		sum = sum + p_final_price

	return sum
# }

def cart_close(id_cart):
# {
	cd = CartDatabase()

	return cd.close_cart(id_cart)
# }