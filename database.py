import psycopg2
from datetime import datetime

conn = psycopg2.connect(user="postgres", password="12039",
                        host="localhost", port="5432", database="my_duka")

cur = conn.cursor()

# products


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products
x = get_products()
print(x)
# sales


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


product_data = get_products()
sales_data = get_sales()

# print("Product data", product_data)
# print("Sales data", sales_data)

# method 1 inserting products
def insert_products(values):
    insert_query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert_query, values)
    conn.commit()

# method 2 inserting products
def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product_value1 = ('cup',40,80)
product_value2 = ('spoon',50,100)

insert_products(product_value1)
insert_products(product_value2)
products = get_products()
# print(products)

# inserting sales
current_datetime = str(datetime.now())
print(current_datetime)
def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity,created_at)values{values}")
    conn.commit()

sale_values = (2,8,current_datetime)    
insert_sales(sale_values)
sales = get_sales()
# print(sales)