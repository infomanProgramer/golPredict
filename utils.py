from datetime import date

def show_edit_menu(nombre_tabla, campos):
    cont = 0
    print(f"********* EDITAR {nombre_tabla} *********")
    print()
    for campo in campos:
        cont += 1
        print(f"    {cont}. {campo["name"]}")
    print(f"    {cont + 1}. Volver")
    print()
    print("****************************************")
    seleccion = input("Seleccione el campo a editar: ")
    return seleccion

def get_new_field_value(value_and_type_of_field):
    message = f"Cambiar {value_and_type_of_field['name_of_field']} = {value_and_type_of_field['value_of_field']} por: "
    if value_and_type_of_field["type_of_field"] == "date":
        print(message)
        year = input("  Ingrese el año: ")
        month = input("  Ingrese el mes: ")
        day = input("  Ingrese el día: ")
        new_value = date(int(year), int(month), int(day))
    else:
        new_value = input(message)
    return new_value