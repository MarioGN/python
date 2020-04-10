import sqlite3


conn = sqlite3.connect('database.db') # auto commit -> isolation_level=None
cursor = conn.cursor()

# insert
cursor.execute('INSERT INTO cliente (nome, idade) VALUES ("Augusto", 30)')


# read
cursor.execute('SELECT * FROM cliente')
print(cursor.fetchall())


# recuperando o id do último registro inserido
print(cursor.lastrowid)


# update
cursor.execute('UPDATE cliente SET nome="Mario Neto" WHERE id=2')


# delete
cursor.execute('DELETE FROM cliente WHERE id=3')


# read
cursor.execute('SELECT * FROM cliente')
print(cursor.fetchall())


print('Conexão realizada...')
# conn.commit()
conn.close()

# transação
try:
    conn.begin()
    cursor.execute('INSERT INTO cliente (nome, idade) VALUES ("Augusto", 30)')
    cursor.execute('INSERT INTO cliente (nome, idade) VALUES ("Augusto", 30)')
    conn.commit()
except:
    conn.rollback()
