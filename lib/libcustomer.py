#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

from lib.libdata import *
from lib.libutils import *
from lib.libetl import *

class CustomerDatabase(DatabaseBase):
# {
	def __init__(self, database="marketplace"):
		super().__init__()
		self.connect_loop(database)

	def get_all_customers(self):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = "SELECT * FROM customer;"

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def get_customer_by_id(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""SELECT * FROM customer as c
		WHERE c.id_customer = '{id}';"""

		curr.execute(sql_query)
		result = curr.fetchall()
		self.close()

		if not result:
			return -1

		return result

	def create_customer(self, customer):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""INSERT INTO customer (id_customer, name, phone)
		values	(nextval('cid_seq'), '{customer['name']}', '{customer['phone']}');"""

		try:
			curr.execute(sql_query)
			conn.commit()
		except Exception as e:
			print(str(e))
			self.close()
			return -1
		
		self.close()
		return 0
	
	def update_customer(self, customer):
		conn = self.db()
		conn.commit()
		curr = self.cursor()
		rc = -1

		sql_query = f"""UPDATE customer
		SET name = '{customer['name']}', phone = '{customer['phone']}'
		WHERE id_customer = '{customer['id_customer']}';"""

		try:
			curr.execute(sql_query)
			conn.commit()
			rc = curr.rowcount
		except Exception as e:
			print(str(e))
		
		self.close()
		return rc

	def delete_customer(self, id):
		conn = self.db()
		conn.commit()
		curr = self.cursor()

		sql_query = f"""DELETE from customer where id_customer = '{id}';"""

		curr.execute(sql_query)
		rows_deleted = curr.rowcount
		conn.commit()
		self.close()

		return rows_deleted
# }

def customer_all_get():
# {
	pd = CustomerDatabase()
	customers = pd.get_all_customers()
	customers_etl = []

	if customers == -1:
		return []

	for c in customers:
		customers_etl.append(etl_customer(c))

	return customers_etl
# }

def customer_get(id):
# {
	pd = CustomerDatabase()
	product = pd.get_customer_by_id(id)

	return product
# }

def customer_delete(id):
# {
	pd = CustomerDatabase()
	rd = pd.delete_customer(id)

	return rd
# }

def customer_post(product):
# {
	pd = CustomerDatabase()
	return pd.create_customer(product.__dict__)
# }

def customer_update(product):
	pd = CustomerDatabase()

	return pd.update_customer(product.__dict__)