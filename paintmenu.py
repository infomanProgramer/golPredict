class PaintMenu:

    def show_opcion_volver(self, number_of_option):
        print("     "+str(number_of_option)+". Volver")
    
    def show_header_menu(self, name_of_menu):
        print("******* "+name_of_menu+" *********")
        print("")
    
    def show_footer_menu(self):
        print("")
        print("********************************")

    def get_option_selected(self):
        opcion = input("INPUT -> Seleccione una opcion = ")
        return opcion

    def show_main_menu(self):
        self.show_header_menu("MENU PRINCIPAL")
        print("     1. Usuarios")
        print("     2. Partidos")
        print("     3. Pronosticos")
        self.show_footer_menu()
        return self.get_option_selected()

    def user_operations(self):
        self.show_header_menu("USUARIOS")
        print("     1. Listar usuarios")
        print("     2. Agregar usuario")
        print("     3. Eliminar usuario")
        print("     4. Editar usuario")
        self.show_opcion_volver(5)
        self.show_footer_menu()
        return self.get_option_selected()

    def partidos_operations(self):
        self.show_header_menu("PARTIDOS")
        print("     1. Listar partidos order by fecha ASC")
        print("     2. Agregar partido")
        print("     3. Eliminar partido")
        print("     4. Editar partido")
        print("     5. Finalizar partido")
        self.show_opcion_volver(6)
        self.show_footer_menu()
        return self.get_option_selected()

    def pronostico_operations(self):
        self.show_header_menu("PRONOSTICOS")
        print("     1. Listar pronosticos")
        print("     2. Agregar pronostico")
        print("     3. Eliminar pronostico")
        print("     4. Editar pronostico")
        self.show_opcion_volver(5)
        self.show_footer_menu()
        return self.get_option_selected()