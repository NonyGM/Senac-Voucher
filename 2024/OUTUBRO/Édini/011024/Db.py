import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def conectar(self):
        self.conn =  sqlite3.connect("self.db_name")
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()
    
    def executar(self, query, parametros = None):
        if parametros:
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)
        

    def fetchAll (self):
        return self.cursor.fetchall()
    