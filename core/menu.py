from plugins.theme.bcolors import Bcolors 

from core.pantalla import Pantalla
class Menu():
    def mostrar(self):
        opcion_menu = 0
        # IMPORTAMOS EL OBJETO PANTALLA
        opantalla = Pantalla()
        while opcion_menu <= 0 or opcion_menu > 4:
            # LIMPIAMOS LA PANTALLA PARA GENERAR EL MENU
            opantalla.limpiar()
            # MENU PARA LA SELEECIÓN DE LAS OPCIONES -- SERGIO
            print(f"{Bcolors.BOLD}CODB - DATABASE ADMINISTRATOR TOOL  -  BY EDWIN ARIZA{Bcolors.END}")
            print("Opciones disponibles:") 
            print("1. Conectar a la base de datos.")
            print("2. Autores.")
            print("3. Licencia.")
            print("4. Salir.")
            try:
                opcion_menu = int(input("¿Qué opción eliges? (1-4):"))
            except:
                # SI EL CARACTER NO NÚMERICO EL SISTEMA VA A GENERAR UN ERROR
                # CON ESTO O DEJAMOS PASAR PARA VOLVER A PEDIR LA OPCION.
                pass
        return opcion_menu