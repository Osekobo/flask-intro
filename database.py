import psycopg2

conn = psycopg2.connect(user="postgres", password="12039",host="localhost", port="5432", database="lelo")

cur = conn.cursor()

cur.execute("select * from boy")
data = cur.fetchall()
print(data)
