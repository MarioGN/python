import sqlite3


conn = sqlite3.connect('database.db') # auto commit -> isolation_level=None
cursor = conn.cursor()

nome = 'JOSÉ DA SILVA'
# cursor.execute('UPDATE cliente SET nome=? WHERE id=3', (nome,))
cursor.execute('UPDATE cliente SET nome=:nome WHERE id=3', {'nome': nome})

# read
cursor.execute('SELECT * FROM cliente')
print(cursor.fetchall())


# manipulando múltiplas linhas
cursor.executemany('INSERT INTO cliente (nome, idade) VALUES (?, ?)',
                (
                    ('AUGUSTO', 40),
                    ('MARIA', 49),
                    ('PEDRO', 29),
                    ('FABIO', 20)
                ))

# read
cursor.execute('SELECT * FROM cliente')
print(cursor.fetchall())

cursor.close()