from conexionBd import ConexionBd

class Usuario:
    def __init__(self):
        self.nombre = None
        self.password = None
    
    def create(self, nombre, password):
        self.nombre = nombre
        self.password = password

    def get_all(self):
        conn = ConexionBd()
        resultado = conn.ejecutar("SELECT * FROM usuarios")
        conn.close()
        for usuario in resultado:
            print(usuario[1])
    
    def save(self):
        conn = ConexionBd()
        conn.ejecutar("INSERT INTO usuarios (nombre, password) VALUES ('"+str(self.nombre)+"', '"+str(self.password)+"')")
        conn.close()
    
    def delete(self, nombre):
        conn = ConexionBd()
        conn.ejecutar("DELETE FROM usuarios WHERE nombre = '"+str(nombre)+"'")
        conn.close()