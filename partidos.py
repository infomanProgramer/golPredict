from conexionBd import ConexionBd
from datetime import date

class Partidos:

    fields = [
        {"name": "equipo_A", "type": "text"},
        {"name": "equipo_B", "type": "text"},
        {"name": "fecha", "type": "date"},
        {"name": "goles_A", "type": "integer"},
        {"name": "goles_B", "type": "integer"},
        {"name": "estado", "type": "text"}
    ]
    
    def __init__(self):
        self.equipo_A = None
        self.equipo_B = None
        self.fecha = None
        self.goles_A = None
        self.goles_B = None
        self.estado = None
    
    def create(self, equipo_A, equipo_B, fecha, goles_A, goles_B, estado):
        self.equipo_A = equipo_A
        self.equipo_B = equipo_B
        self.fecha = fecha
        self.goles_A = goles_A
        self.goles_B = goles_B
        self.estado = estado
    
    def get_fields(self):
        return self.fields
    
    def set_equipo_A(self):
        equipo_A = input("Ingrese el nombre del equipo A: ")
        self.equipo_A = equipo_A
    
    def set_equipo_B(self):
        equipo_B = input("Ingrese el nombre del equipo B: ")
        self.equipo_B = equipo_B
    
    def set_fecha(self):
        print("Ingrese la fecha del partido en formato YYYY/MM/DD: ")
        year = input("  Ingrese el año: ")
        month = input("  Ingrese el mes: ")
        day = input("  Ingrese el día: ")
        self.fecha = date(int(year), int(month), int(day))
    
    def set_goles_A(self):
        goles_A = input("Ingrese los goles del equipo A: ")
        if goles_A == "":
            self.goles_A = "0"
        else:
            self.goles_A = goles_A
        
    
    def set_goles_B(self):
        goles_B = input("Ingrese los goles del equipo B: ")
        if goles_B == "":
            self.goles_B = "0"
        else:
            self.goles_B = goles_B
    
    def set_estado(self, estado = "pendiente"):
        self.estado = estado

    def save(self):
        try:
            conn = ConexionBd()
            conn.ejecutar(f"INSERT INTO partidos (equipo_A, equipo_B, fecha, goles_A, goles_B, estado) VALUES ('{self.equipo_A}', '{self.equipo_B}', '{self.fecha}', {self.goles_A}, {self.goles_B}, '{self.estado}')")
            conn.close()
        except Exception as e:
            print(f"Error al guardar partido: {e}")
    
    def show_all(self):
        try:
            conn = ConexionBd()
            partidos = conn.ejecutar("SELECT id, fecha, equipo_A, equipo_B, goles_A, goles_B, estado FROM partidos order by id desc")
            conn.close()
            for partido in partidos:
                print(f"ID: {partido[0]} - fecha: {partido[1]}: A-{partido[2]}({partido[4]}) vs B-{partido[3]}({partido[5]}) - estado: {partido[6]}")
        except Exception as e:
            print(f"Error al mostrar partidos: {e}")
        return partidos

    def show_only_pendientes(self):
        try:
            conn = ConexionBd()
            partidos = conn.ejecutar("SELECT id, fecha, equipo_A, equipo_B, goles_A, goles_B, estado FROM partidos where estado = 'pendiente' order by id desc")
            conn.close()
            for partido in partidos:
                print(f"ID: {partido[0]} - fecha: {partido[1]}: A-{partido[2]}({partido[4]}) vs B-{partido[3]}({partido[5]}) - estado: {partido[6]}")
        except Exception as e:
            print(f"Error al mostrar partidos: {e}")
        return partidos
    
    def show_by_id(self, id):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT id, fecha, equipo_A, equipo_B, goles_A, goles_B, estado FROM partidos WHERE id = "+str(id))
            conn.close()
            for partido in resultado:
                print(f"ID: {partido[0]}")
                print(f"Fecha: {partido[1]}")
                print(f"Equipo_A: {partido[2]}")
                print(f"Equipo_B: {partido[3]}")
                print(f"Goles_A: {partido[4]}")
                print(f"Goles_B: {partido[5]}")
                print(f"Estado: {partido[6]}")
        except Exception as e:
            print(f"Error al mostrar partido: {e}")
    
    def get_by_id(self, id):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar(f"SELECT * FROM partidos WHERE id = {id}")
            conn.close()
            for partido in resultado:
                return partido
        except Exception as e:
            print(f"Error al obtener partido: {e}")
    
    def delete_by_id(self, id):
        try:
            conn = ConexionBd()
            conn.ejecutar(f"DELETE FROM partidos WHERE id = {id}")
            conn.close()
            print("Partido eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar partido: {e}")
    
    def get_properties_of_field_by_id_selected(self, id, number_of_field):
        number_of_field = int(number_of_field)
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT "+self.fields[number_of_field - 1]["name"]+" FROM partidos WHERE id = "+str(id))
            conn.close()
            return {
                "name_of_field": self.fields[number_of_field - 1]["name"],
                "type_of_field": self.fields[number_of_field - 1]["type"],
                "value_of_field": str(resultado[0][0])
            }
        except Exception as e:
            print(f"Error al listar usuarios: {e}")

    def edit_by_id(self, id_partido, value_and_type_of_value, new_value_of_field):
        query = ""
        if value_and_type_of_value["type_of_field"] == 'text' or value_and_type_of_value["type_of_field"] == 'date':
            query = "UPDATE partidos SET "+value_and_type_of_value["name_of_field"]+" = '"+str(new_value_of_field)+"' WHERE id = "+str(id_partido)
        else:
            query = "UPDATE partidos SET "+value_and_type_of_value["name_of_field"]+" = "+str(new_value_of_field)+" WHERE id = "+str(id_partido)

        try:
            conn = ConexionBd()
            conn.ejecutar(query)
            conn.close()
            print("Partido editado correctamente")
        except Exception as e:
            print(f"Error al editar partido: {e}")
    
    def end_game(self, id_partido):
        try:
            conn = ConexionBd()
            conn.ejecutar("UPDATE partidos SET estado = 'finalizado' WHERE id = "+str(id_partido))
            conn.close()
            print("Partido finalizado correctamente")
        except Exception as e:
            print(f"Error al finalizar partido: {e}")
    
    
    