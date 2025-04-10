import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="database123", port=5432)

cur = conn.cursor()

# escrever qualquer comando aq
cur.execute("SELECT * FROM CLIENTE;")

print(cur.fetchall())

# fim dos comandos
conn.commit()

cur.close()
conn.close()