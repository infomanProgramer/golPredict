from conexionBd import ConexionBd
from partidos import Partidos
from usuarios import Usuario
class Pronostico:

    fields = [
        {"name": "usuario_id", "type": "integer"},
        {"name": "partido_id", "type": "integer"},
        {"name": "goles_A", "type": "integer"},
        {"name": "goles_B", "type": "integer"},
        {"name": "puntos", "type": "integer"}
    ]

    partidos = Partidos()
    usuarios = Usuario()

    def __init__(self):
        self.usuario_id = None
        self.partido_id = None
        self.goles_A = None
        self.goles_B = None
        self.puntos = None
    
    def get_fields(self):
        return self.fields
    
    def set_usuario_id(self):
        self.usuarios.show_all()
        self.usuario_id = int(input("Seleccionar usuario ID: "))
    
    def set_partido_id(self):
        self.partidos.show_only_pendientes()
        self.partido_id = int(input("Seleccionar partido ID: "))
    
    def set_goles_A(self):
        partido = self.partidos.get_by_id(self.partido_id)
        self.goles_A = int(input(f"Ingresar goles del equipo A ({partido[1]}): "))
    
    def set_goles_B(self):
        partido = self.partidos.get_by_id(self.partido_id)
        self.goles_B = int(input(f"Ingresar goles del equipo B ({partido[2]}): "))
    
    def set_puntos(self, puntos):
        self.puntos = puntos

    def save(self):
        try:
            conn = ConexionBd()
            conn.ejecutar(f"INSERT INTO pronosticos (usuario_id, partido_id, goles_A, goles_B) VALUES ({self.usuario_id}, {self.partido_id}, {self.goles_A}, {self.goles_B})")
            conn.close()
            print("Pronóstico guardado correctamente")
        except Exception as e:
            print(f"Error al guardar el pronóstico: {e}")
    
    def show_all(self):
        query = """
            select 
                p.id, 
                u.nombre,
                pa.equipo_A, 
                p.goles_A,
                pa.equipo_B, 
                p.goles_B 
            from pronosticos p
            inner join usuarios u on u.id = p.usuario_id
            inner join partidos pa on pa.id = p.partido_id
            order by p.id desc;
        """
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar(query)
            conn.close()
            for pronostico in resultado:
                print(f"ID: {pronostico[0]}, Usuario: {pronostico[1]}, A: {pronostico[2]}({pronostico[3]}) vs B: {pronostico[4]}({pronostico[5]})")
        except Exception as e:
            print(f"Error al obtener los pronósticos: {e}")

    def delete_by_id(self, id):
        try:
            conn = ConexionBd()
            conn.ejecutar(f"DELETE FROM pronosticos WHERE id = {id}")
            conn.close()
            print("Pronóstico eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar el pronóstico: {e}")
    
    def show_by_id(self, id):
        query = f"SELECT * FROM pronosticos WHERE id = {id}"
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar(query)
            conn.close()
            for pronostico in resultado:
                print(f"ID: {pronostico[0]}")
                print(f"Usuario: {pronostico[1]}")
                print(f"Equipo A: {pronostico[2]}")
                print(f"Goles A: {pronostico[3]}")
                print(f"Equipo B: {pronostico[4]}")
                print(f"Goles B: {pronostico[5]}")
        except Exception as e:
            print(f"Error al obtener el pronóstico: {e}")

