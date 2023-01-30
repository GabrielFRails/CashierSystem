from lib.libdata import *
from lib.libutils import *
from lib.libetl import *

class ProductTypeDatabase(DatabaseBase):
    def __init__(self, database="market_place"):
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

        sql_query = f"""SELECT * FROM product_type p WHERE p.id_type = '{id}';"""

        curr.execute(sql_query)
        result = curr. fetchall()
        self.close()

        if not result:
            return -1

        return result

    def create_product_type(self, product_type, id):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = f"""INSERT INTO product_type (id_type, description)
        values ('{id}', {product_type['description']});"""

        try:
            curr.execute(sql_query)
            conn.commit()
        except Exception as e:
            print(str(e))
            self.close()
            return -1

        self.close()
    
    def update_product_type(self, product_type):
        conn = self.db()
        conn.commit()
        surr = self.cursor()

        sql_query = f"""UPDATE product_type
        SET description = '{product_type['description']}
        WHERE id_type = '{product_type['id_type']}';"""

        try:
            curr.execute(sql_query)
            conn.commit()
        except Exception as e:
            print(str(e))
            self.close()
            return -1

        self.close()
        return 0

    def delete_product_type(self, id):
        conn = self.db()
        conn.commit()
        curr = self.cursor()

        sql_query = f"""DELETE from product_type where id_type = '{id}';"""

        curr.execute(sql_query)
        rows_deleted = curr.rowcount
        conn.commit()
        self.close()
        self.close()

        return rows_deleted

def product_type_get(id):
# {
    ptd = ProductTypeDatabase()

    product_type = ptd.get_product_type_by_id(id)
    return product_type
# }

def product_type_all_get():
    pd = ProductTypeDatabase()
    product_types = pd.get_all_product_types()
    product_types_etl = []

    for p in product_types:
        product_types_etl.append(etl_product_type(p))

    return product_types_etl

def product_type_delete(id):
    pd = ProductTypeDatabase()
    rd = pd.delete_product_type(id)

    return rd

def product_type_post(product):
    pd = ProductTypeDatabase()

    id = 'CS_%s_TYPE%s' % (utils_generate_id())

    return pd.create_product_type(product_type.__dict__, id)

def product_type_update(product_type):
    pd = ProductTypeDatabase()

    return pd.update_product_type(product_type.__dict__)
