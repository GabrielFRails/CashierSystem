from lib.libdata import DatabaseBase

class product_type:
	def __init__(self, tdata):
		self.id_type = tdata[0]
		self.description = tdata[1]

db = DatabaseBase()
db.connect_loop("market_place")
conn = db.db()
curr = db.cursor()
conn.commit()

curr.execute("SELECT * FROM product_type")
result = curr.fetchall()
print(result)

if result:
	for r in result:
		pt = product_type(r)
		print(pt.__dict__)