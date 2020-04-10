import sqlite3, conexao_factory


class ClienteRepository:
    @staticmethod
    def listar_clientes():
        conexao = conexao_factory.Conexao().conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM cliente')
            print(cursor.fetchall())
        finally:
            conexao.close()

    @staticmethod
    def inserir_cliente(cliente):
        conexao = conexao_factory.Conexao().conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO cliente (nome, idade) VALUES (?, ?)', 
                           (cliente.nome, cliente.idade))
        finally:
            conexao.commit()
            conexao.close()

    @staticmethod
    def editar_cliente(id_cliente, cliente):
        conexao = conexao_factory.Conexao().conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute('UPDATE cliente SET nome=?, idade=? WHERE id=?', 
                           (cliente.nome, cliente.idade, id_cliente))
        finally:
            conexao.commit()
            conexao.close()

    @staticmethod
    def remover_cliente(id_cliente):
        conexao = conexao_factory.Conexao().conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM cliente WHERE id=?', (id_cliente,))
        finally:
            conexao.commit()
            conexao.close()
