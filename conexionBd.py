import sqlite3

class ConexionBd:
    def __init__(self):
        self.conn = sqlite3.connect("Mundial2026_Pronosticos.db")
        self.cursor = self.conn.cursor()

    def ejecutar(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
