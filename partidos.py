import conexionBd

class Partido:
    def __init__(self, equipo_A, equipo_B, fecha, goles_A, goles_B, estado):
        self.equipo_A = equipo_A
        self.equipo_B = equipo_B
        self.fecha = fecha
        self.goles_A = goles_A
        self.goles_B = goles_B
        self.estado = estado

    def save(self):
        conn = conexionBd.ConexionBd()
        conn.ejecutar(f"INSERT INTO partidos (equipo_A, equipo_B, fecha, goles_A, goles_B, estado) VALUES ('{self.equipo_A}', '{self.equipo_B}', '{self.fecha}', '{self.goles_A}', '{self.goles_B}', '{self.estado}')")
        conn.close()
    
    def get_all(self):
        conn = conexionBd.ConexionBd()
        conn.ejecutar("SELECT * FROM partidos")
        return conn.fetchall()
    
    def get_by_id(self, id):
        conn = conexionBd.ConexionBd()
        conn.ejecutar(f"SELECT * FROM partidos WHERE id = {id}")
        return conn.fetchone()
    