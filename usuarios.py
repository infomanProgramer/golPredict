from conexionBd import ConexionBd

class Usuario:

    campos = [
        {"name": "nombre", "type": "text"},
        {"name": "password", "type": "text"}
    ]

    def __init__(self):
        self.nombre = None
        self.password = None

    def get_campos(self):
        return self.campos
    
    def create(self, nombre, password):
        self.nombre = nombre
        self.password = password

    def get_all(self):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT * FROM usuarios")
            conn.close()
            for usuario in resultado:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}")
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
    
    def get_by_id(self, id):
        try:
            conn = ConexionBd()
            resultado = conn.ejecutar("SELECT * FROM usuarios WHERE id = "+str(id))
            conn.close()
            for usuario in resultado:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}")
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
    
    def edit_by_id(self, id):
        try:
            conn = ConexionBd()
            conn.ejecutar("UPDATE usuarios SET nombre = '"+str(self.nombre)+"', password = '"+str(self.password)+"' WHERE id = "+str(id))
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