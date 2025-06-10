import psycopg2

conn = psycopg2.connect(user="postgres", password="12039",
                        host="localhost", port="5432", database="sales")

cur = conn.cursor()

# sales
def get_sales():
    cur.execute("select * from sale")
    data = cur.fetchall()
    return data


sales_data = get_sales()
print(sales_data)
