#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
# Copyright (c) 2023 Luiza Costa <oliveiraluiza2012ufg@gmail.com>
#

from lib.libdata import *
from lib.libutils import *
from lib.libetl import *

class ProductTypeDatabase(DatabaseBase):
    def __init__(self, database="marketplace"):
        super().__init__()
        self.connect_loop(database)

    def get_all_product_types(self):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = "SELECT * FROM product_type;"

        curr.execute(sql_query)
        result = curr.fetchall()
        self.close()

        if not result:
            return -1

        return result

    def get_product_type_by_id(self, id):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = f"""SELECT * FROM product_type as pt WHERE pt.id_type = '{id}';"""

        curr.execute(sql_query)
        result = curr.fetchall()
        self.close()

        if not result:
            return -1

        return result

    def create_product_type(self, product_type):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = f"""INSERT INTO product_type (id_type, description)
        values (nextval('ptid_seq'), '{product_type['description']}');"""

        try:
            curr.execute(sql_query)
            conn.commit()
        except Exception as e:
            print(str(e))
            self.close()
            return -1

        self.close()
        return 0
    
    def update_product_type(self, product_type):
        conn = self.db()
        conn.commit()
        curr = self.cursor()
        rc = -1

        sql_query = f"""UPDATE product_type
        SET description = '{product_type['description']}'
        WHERE id_type = '{product_type['id_type']}';"""

        try:
            curr.execute(sql_query)
            conn.commit()
            rc = curr.rowcount
        except Exception as e:
            print(str(e))

        self.close()
        return rc

    def delete_product_type(self, id):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = f"""DELETE from product_type where id_type = '{id}';"""

        curr.execute(sql_query)
        rows_deleted = curr.rowcount
        conn.commit()
        self.close()

        return rows_deleted

def product_type_get(id):
# {
    ptd = ProductTypeDatabase()

    product_type = ptd.get_product_type_by_id(id)
    return product_type
# }

def product_type_all_get():
    ptd = ProductTypeDatabase()
    product_types = ptd.get_all_product_types()
    product_types_etl = []

    if product_types == -1:
        return []

    for p in product_types:
        product_types_etl.append(etl_product_type(p))

    return product_types_etl

def product_type_delete(id):
    ptd = ProductTypeDatabase()
    rd = ptd.delete_product_type(id)

    return rd

def product_type_post(product_type):
    ptd = ProductTypeDatabase()
    return ptd.create_product_type(product_type.__dict__)

def product_type_update(product_type):
    ptd = ProductTypeDatabase()

    return ptd.update_product_type(product_type.__dict__)
