from conexionBd import ConexionBd

class Usuario:

    fields = [
        {"name": "nombre", "type": "text"},
        {"name": "password", "type": "text"}
    ]

    def __init__(self):
        self.nombre = None
        self.password = None
    
    def create(self, nombre, password):
        self.nombre = nombre
        self.password = password

    def get_fields(self):
        return self.fields

    def show_all(self):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT * FROM usuarios")
            conn.close()
            for usuario in resultado:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}")
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
    
    def show_by_id(self, id):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT * FROM usuarios WHERE id = "+str(id))
            conn.close()
            for usuario in resultado:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}")
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
    
    def get_properties_of_field_by_id_selected(self, id, number_of_field):
        number_of_field = int(number_of_field)
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT "+self.fields[number_of_field - 1]["name"]+" FROM usuarios WHERE id = "+str(id))
            conn.close()
            return {
                "name_of_field": self.fields[number_of_field - 1]["name"],
                "type_of_field": self.fields[number_of_field - 1]["type"],
                "value_of_field": str(resultado[0][0])
            }
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
    
    
    def edit_by_id(self, id_user, value_and_type_of_value, new_value_of_field):
        query = ""
        if value_and_type_of_value["type_of_field"] == 'text':
            query = "UPDATE usuarios SET "+value_and_type_of_value["name_of_field"]+" = '"+str(new_value_of_field)+"' WHERE id = "+str(id_user)
        else:
            query = "UPDATE usuarios SET "+value_and_type_of_value["name_of_field"]+" = "+str(new_value_of_field)+" WHERE id = "+str(id_user)

        try:
            conn = ConexionBd()
            conn.ejecutar(query)
            conn.close()
            print("Usuario editado correctamente")
        except Exception as e:
            print(f"Error al editar usuario: {e}")

    def save(self):
        try:
            conn = ConexionBd()
            conn.ejecutar("INSERT INTO usuarios (nombre, password) VALUES ('"+str(self.nombre)+"', '"+str(self.password)+"')")
            conn.close()
            print("Usuario agregado correctamente")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
    
    def delete_by_nombre(self, nombre):
        try:
            conn = ConexionBd()
            conn.ejecutar("DELETE FROM usuarios WHERE nombre = '"+str(nombre)+"'")
            conn.close()
            print("Usuario eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
    
    def delete_by_id(self, id):
        try:
            conn = ConexionBd()
            conn.ejecutar("DELETE FROM usuarios WHERE id = "+str(id))
            conn.close()
            print("Usuario eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")