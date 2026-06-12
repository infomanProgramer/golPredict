import conexionBd

class Pronostico:
    def __init__(self, usuario_id, partido_id, goles_A, goles_B, puntos):
        self.usuario_id = usuario_id
        self.partido_id = partido_id
        self.goles_A = goles_A
        self.goles_B = goles_B
        self.puntos = puntos
    
    def save(self):
        conn = conexionBd.ConexionBd()
        conn.ejecutar(f"INSERT INTO pronosticos (usuario_id, partido_id, goles_A, goles_B, puntos) VALUES ({self.usuario_id}, {self.partido_id}, {self.goles_A}, {self.goles_B}, {self.puntos})")
        conn.close()
    
    def get_all(self):
        conn = conexionBd.ConexionBd()
        conn.ejecutar("SELECT * FROM pronosticos")
        return conn.fetchall()
