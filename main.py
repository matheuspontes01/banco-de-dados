import psycopg2

#connect to the db
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="85016244",
    host="170.239.226.80",
    port="5432"
)
print("Conexao estabelecida com sucesso!")

#cursor
cur = conn.cursor()

cur.execute("""CREATE TABLE teste (
    id_teste serial primary key,
    nome_teste varchar(100)
);""")


#commit the transiction
conn.commit()

#close cursor
cur.close()
conn.close()