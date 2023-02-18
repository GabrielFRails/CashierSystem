#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

import psycopg2 as psg2
import time

class DatabaseBase:
# {
	def __init__(self):
		self.__host = "localhost"
		self.__user = "postgres"
		self.__password = "postgres"
	
	def connect(self, database):
		print(f"Connecting in \nHost: {self.__host} \nUser: {self.__user} \nPassword: {self.__password}")
		db = psg2.connect(host=self.__host, database=database, user=self.__user, password=self.__password)
		self.postgress_instance = db
	
	def connect_loop(self, database="postgress"):
		if not database:
			return -1
	
		while True:
			try:
				self.connect(database)
				print("Connection ok")
				break
			except Exception as e:
				print(f"Fail to connect to {self.__user}:{self.__host}")
				print(f"Fail reason {str(e)}")

				# TODO Search for the object istance
				# if isinstance(self.postgress_instance, ):
				# 	del self.postgress_instance
				
				self.postgress_instance = None
				time.sleep(2)
				continue
	
	def db(self):
		return self.postgress_instance
	
	def cursor(self):
		conn = self.postgress_instance
		curr = conn.cursor()
		return curr
	
	def close(self):
		conn = self.postgress_instance
		conn.close()
# }
