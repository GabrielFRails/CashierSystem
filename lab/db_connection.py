from lib.libdata import DatabaseBase

querry_create_table = """CREATE TABLE ProductType (
	idType INTEGER NOT NULL,
	description CHARACTER VARYING,
	CONSTRAINT ProductType_pkey PRIMARY KEY (idType)
);"""

querry_insert = """INSERT INTO ProductType (idType, description)
values	(001, 'Beverages'),
	(002, 'Cereals'),
	(003, 'Canned goods'),
	(004, 'Cold'),
	(005, 'Cleanup');"""

db = DatabaseBase()
db.connect_loop("csystem")
conn = db.db()
curr = db.cursor()
curr.execute("DROP TABLE IF EXISTS ProductType")
curr.execute(querry_create_table)
conn.commit()

curr.execute(querry_insert)

curr.execute("SELECT * FROM ProductType")
result = curr.fetchall()
print(result)

