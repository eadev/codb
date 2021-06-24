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
            print(f"{Bcolors.BOLD}CODB - DATABASE ADMINISTRATOR TOOL  -  BY EDWIN ARIZA{Bcolors.END}\n")
            print("Opciones disponibles:") 
            print(f"{Bcolors.BOLD}1.{Bcolors.END} Conectar a la base de datos.")
            print(f"{Bcolors.BOLD}2.{Bcolors.END} Autor.")
            print(f"{Bcolors.BOLD}3.{Bcolors.END} Licencia.")
            print(f"{Bcolors.BOLD}4.{Bcolors.END} Salir.")
            try:
                opcion_menu = int(input("¿Qué opción eliges? (1-4): "))
            except:
                # SI EL CARACTER NO NÚMERICO EL SISTEMA VA A GENERAR UN ERROR
                # CON ESTO O DEJAMOS PASAR PARA VOLVER A PEDIR LA OPCION.
                pass
        return opcion_menu