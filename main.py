from usuarios import Usuario

def showMainMenu():
    print("******* MENU PRINCIPAL *********")
    print("")
    print("     1. Usuarios")
    print("     2. Partidos")
    print("     3. Pronosticos")
    print("")
    print("********************************")
    opcion = input("Seleccione una opcion: ")
    return opcion

def showUsersMenu():
    print("********* USUARIOS *************")
    print("")
    print("     1. Listar usuarios")
    print("     2. Agregar usuario")
    print("     3. Eliminar usuario")
    print("     4. Editar usuario")
    print("     5. Volver")
    print("")
    print("********************************")
    opcion = input("Seleccione una opcion: ")
    return opcion

def showOperationsUsers():
    listar_usuarios = "1"
    agregar_usuario = "2"
    eliminar_usuario = "3"
    editar_usuario = "4"
    volver = "5"  
    usuario = Usuario()
    nombre = ""
    while True:
        opcion = showUsersMenu()
        if opcion == listar_usuarios:
            usuario.get_all()
        if opcion == agregar_usuario:
            nombre = input("Ingrese el nombre del usuario: ")
            usuario.create(nombre, "0")
            usuario.save()
        if opcion == eliminar_usuario:
            usuario.get_all()
            nombre = input("Ingrese el nombre del usuario a eliminar: ")
            usuario.delete(nombre)
        if opcion == editar_usuario:
            #usuario.update()
            pass
        if opcion == volver:
            break
    
def main():
    while True:
        opcion = showMainMenu()  
        if opcion == "1":
            showOperationsUsers()
        elif opcion == "2":
            print("Partidos")
        elif opcion == "3":
            print("Pronosticos")
            break
        else:
            print("Error! Opcion invalida")

if __name__ == "__main__":
    main()

