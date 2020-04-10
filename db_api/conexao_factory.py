import sqlite3


class Conexao:
    @staticmethod
    def conectar():
        db = sqlite3.connect('database.db')
        return db
