import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="database123", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Cliente (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(11),
    telefone VARCHAR(15)
);
""")

cur.execute("""INSERT INTO Cliente (id, nome, cpf, telefone) VALUES
(1, 'Marcelo', '77705603759', '556398888888888');
""")

conn.commit()

cur.close()
conn.close()