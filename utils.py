
def generate_edit_menu(nombre_tabla, campos):
    cont = 0
    print(f"********* EDITAR {nombre_tabla} *********")
    print()
    for campo in campos:
        cont += 1
        print(f"    {cont}. {campo}")
    print(f"    {cont + 1}. Volver")
    print()
    print("****************************************")
    seleccion = input("Seleccione el campo a editar: ")
    return seleccion