# DISEÑADOR - ESNEYDER 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
opcion_menu = 0

print(f"{bcolors.OKBLUE}Bienvenidos a CODB, sistema de gestión de base de datos..\n {bcolors.WARNING}") 
print(f"{bcolors.OKBLUE}Indicanos tus datos para conectarnos y así ejecuta sentencias.\n {bcolors.WARNING}") 
while opcion_menu != 4:
    # MENU PARA LA SELEECIÓN DE LAS OPCIONES -- SERGIO
    print("Menú para la seleccion de opciones:") 
    print("1. Conectar a la base de datos.")
    print("2. Autores.")
    print("3. Licencia.")
    print("4. Salir.")
    opcion_menu = int(input("¿Qué opción eliges? (1-4):"))

    if opcion_menu == 1:
        host = input("Host BD:")
        confirmacion = False  # PERMITE SABER SI EL USUARIO CONFIRMO Y SI NO SE REPITE
        usuario = input("Usuario BD:")
        clave = input("Clave BD:")
        base_datos = input("Nombre BD:")

        print("Estas seguro que los datos de configuración son:")

        print(f"Host ======> {host}")
        print(f"Usuario ======> {usuario}")
        print(f"Clave ======> {clave}")
        print(f"Base de Datos ======> {base_datos}")
        # CICLO DE COMPROBACIÓN DE SELECCIÓN CORRECTA: - ROSEMBERGTH
        confirma = None
        while confirma not in ("Y","y","N","n"):
            confirma = input("Confirmas (Y/y/N/n): ")
        # IMPRIMIR LO QUE EL USUARIO SELECCIONO -- DIEGO 
        if confirma == "Y" or confirma == "y": 
            print("Confirmado") 
        else: 
            pass # TODO
    elif opcion_menu == 2:
        # IMPRIMIR LOS AUTORES  -- MIGUEL 
        autor1 = ("JORGE ENRIQUE GONZALEZ GRANADOS") 
        autor2 = ("ROSENBERGTH") 
        autor3 = ("CRISTIAN VILLALBA LOZANO") 
        autor4 = ("DIEGO SANTOS REYES") 
        autor5 = ("ESNEYDER SAAVEDRA") 
        autor6 = ("JHON JEREZ") 
        autor7 = ("SERGIO INE") 
        autor8 = ("MIGUEL ANGEL RODRIGUEZ") 
        print(f"AUTORES: \n{autor1} \n{autor2} \n{autor3} \n{autor4} \n{autor5} \n{autor6} \n{autor7} \n{autor8}") 

    elif opcion_menu == 3:
        # VARIABLE licencia  string  Creative Commons -- CRISTIAN
        licencia = "Creative Commons" 
        print(licencia) 
    else:
        print("Cerrando la aplicación.")
