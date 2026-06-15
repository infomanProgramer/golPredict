from usuarios import Usuario
from utils import show_edit_menu
from utils import get_new_field_value
from paintmenu import PaintMenu
from partidos import Partidos
from pronosticos import Pronostico

def user_operations():
    listar_usuarios = "1"
    agregar_usuario = "2"
    eliminar_usuario = "3"
    editar_usuario = "4"
    volver = "5"  
    usuario = Usuario()
    paintmenu = PaintMenu()
    nombre = ""
    while True:
        opcion = paintmenu.user_operations()
        if opcion == listar_usuarios:
            usuario.show_all()
        if opcion == agregar_usuario:
            nombre = input("Ingrese el nombre del usuario: ")
            usuario.create(nombre, "0")
            usuario.save()
        if opcion == eliminar_usuario:
            usuario.show_all()
            _id = int(input("Ingrese el ID del usuario a eliminar: "))
            usuario.delete_by_id(_id)
        if opcion == editar_usuario:
            usuario.show_all()
            id_user = int(input("Ingrese el ID del usuario a editar: "))
            usuario.show_by_id(id_user)
            print("Seleccione el número del campo a editar:")
            number_of_field_selected = show_edit_menu("USUARIO", usuario.get_fields())
            value_and_type_of_field = usuario.get_properties_of_field_by_id_selected(id_user, number_of_field_selected)
            new_value_of_field = get_new_field_value(value_and_type_of_field)
            usuario.edit_by_id(id_user, value_and_type_of_field, new_value_of_field)
        if opcion == volver:
            break

def partidos_operations():
    paintmenu = PaintMenu()
    partidos = Partidos()
    listar_partidos = "1"
    agregar_partido = "2"
    eliminar_partido = "3"
    editar_partido = "4"
    finalizar_partido = "5"
    volver = "6"
    while True:
        opcion = paintmenu.partidos_operations()
        if opcion == listar_partidos:
            partidos.show_all()
        elif opcion == agregar_partido:
            partidos.set_equipo_A()
            partidos.set_equipo_B()
            partidos.set_fecha()
            partidos.set_goles_A()
            partidos.set_goles_B()
            partidos.set_estado()
            partidos.save()
        elif opcion == eliminar_partido:
            partidos.show_all()
            id_partido = int(input("Ingrese el ID del partido a eliminar: "))
            partidos.delete_by_id(id_partido)
        elif opcion == editar_partido:
            partidos.show_all()
            id_partido = input("Ingrese el ID del partido a editar: ")
            partidos.show_by_id(id_partido)
            print("Seleccione el número del campo a editar:")
            number_of_field_selected = show_edit_menu("PARTIDO", partidos.get_fields())
            value_and_type_of_field = partidos.get_properties_of_field_by_id_selected(id_partido, number_of_field_selected)
            new_value_of_field = get_new_field_value(value_and_type_of_field)
            partidos.edit_by_id(id_partido, value_and_type_of_field, new_value_of_field)
        elif opcion == finalizar_partido:
            partidos.show_all()
            id_partido = input("Ingrese el ID del partido a finalizar: ")
            partidos.end_game(id_partido)
        elif opcion == volver:
            break

def pronosticos_operations():
    paintmenu = PaintMenu()
    pronosticos = Pronostico()
    listar_pronosticos = "1"
    agregar_pronostico = "2"
    eliminar_pronostico = "3"
    editar_pronostico = "4"
    volver = "5"
    while True:
        opcion = paintmenu.pronostico_operations()
        if opcion == listar_pronosticos:
            pronosticos.show_all()
        elif opcion == agregar_pronostico:
            pronosticos.set_usuario_id()
            pronosticos.set_partido_id()
            pronosticos.set_goles_A()
            pronosticos.set_goles_B()
            pronosticos.save()
        elif opcion == eliminar_pronostico:
            pronosticos.show_all()
            id_pronostico = int(input("Ingrese el ID del pronostico a eliminar: "))
            pronosticos.delete_by_id(id_pronostico)
        elif opcion == editar_pronostico:
            print("Opcion no disponible")
        elif opcion == volver:
            break

def main():
    paintmenu = PaintMenu()
    user_option_selected = "1"
    partidos_option_selected = "2"
    pronostiocos_option_selected = "3"
    while True:
        opcion = paintmenu.show_main_menu()  
        if opcion == user_option_selected:
            user_operations()
        elif opcion == partidos_option_selected:
            partidos_operations()
        elif opcion == pronostiocos_option_selected:
            pronosticos_operations()
        else:
            print("Error! Opcion invalida")

if __name__ == "__main__":
    main()

