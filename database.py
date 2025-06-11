import psycopg2

conn = psycopg2.connect(user="postgres", password="12039",
                        host="localhost", port="5432", database="postgres")

cur = conn.cursor()

cur.execute("select * from products")
data = cur.fetchall()
print(data)


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


def get_sales():
    query = "select * from sales"
    cur.execute(query)
    sales = cur.fetchall()
    return sales


def insert_products(values):
    insert_query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert_query, values)
    conn.commit()


def insert_products(values):
    cur.execute(
        f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()


def insert_sales(values):
    insert_sales = "insert into sales(pid,quantity,created_at)values(%s,%s,%s)"
    cur.execute(insert_sales, values)
    conn.commit()
