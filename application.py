'''
APLICACIÓN PARA LA ADMINSITRACIÓN DE BASES DE DATOS EN UN ENTORNO CLI
@author: EDWIN ARIZA <me@edwinariza.com>
@copyright: GNU Public License 
'''

import pymysql  
import getpass
import os
from start.welcome import Welcome
from plugins.theme.bcolors import Bcolors
from core.menu import Menu
from core.pantalla import Pantalla

# INICIAMOS LA VISTA DE BIENVENIDA
ostart = Welcome()
ostart.start()
# OBJETO PANTALLA
opantalla = Pantalla()

# SOLICITAMOS UN ENTER PARA CONTINUAR
tecla = input(f"{Bcolors.WARNING}Presiona cualquier tecla para continuar...{Bcolors.END}")
# LIMPIAMOS LA PANTALLA CUANDO SE PRESIONE CUALQUIER TECLA
opantalla.limpiar()

# GENERAMOS EL MENU DE LA APLICACION 
omenu = Menu()
opcion_menu = omenu.mostrar()

# ACCIONES ASOCIADAS A OPCIÓN DE MENÚ SELECCIONADA
if opcion_menu == 1:
    confirmacion = False  # PERMITE SABER SI EL USUARIO CONFIRMO Y SI NO SE REPITE
    host = input(f"{Bcolors.WARNING}HOST DB: {Bcolors.END}")
    usuario = input(f"{Bcolors.WARNING}USUARIO BD: {Bcolors.END}")
    # clave = input(f"{Bcolors.WARNING}CLAVE BD: {Bcolors.END}")
    clave = getpass.getpass(f"{Bcolors.WARNING}CLAVE BD: {Bcolors.END}")
    base_datos = input(f"{Bcolors.WARNING}NOMBRE BD: {Bcolors.END}")
    # LIMPIAMOS LA PANTALLA
    opantalla.limpiar()
    # CONFIRMAMOS LA OPCIÓN SELECCIONADA
    print("¿Estas seguro que los datos de configuración son los indicados a continuación?")
    print(f"{Bcolors.WARNING}HOST DB    {Bcolors.END}======> {Bcolors.BOLD}{host}{Bcolors.END}")
    print(f"{Bcolors.WARNING}USUARIO DB {Bcolors.END}======> {Bcolors.BOLD}{usuario}{Bcolors.END}")
    # print(f"{Bcolors.WARNING}CLAVE DB   {Bcolors.END}======> {Bcolors.BOLD}{clave}{Bcolors.END}")
    print(f"{Bcolors.WARNING}NOMBRE DB  {Bcolors.END}======> {Bcolors.BOLD}{base_datos}{Bcolors.END}")
    # CICLO DE COMPROBACIÓN DE SELECCIÓN CORRECTA: 
    confirma = None
    while confirma not in ("Y","y","N","n"):
        confirma = input("Confirmas (Y/y/N/n): ")
    # IMPRIMIR LO QUE EL USUARIO SELECCIONO -- DIEGO 
    if confirma == "Y" or confirma == "y": 
        opantalla.limpiar()
        print("Confirmado") 
    else: 
        opantalla.limpiar()
        pass # TODO

# OPCIÓN 2 SELECCIONADA
elif opcion_menu == 2:
    # IMPRIMIR LOS AUTORES  -- MIGUEL 
    autores = ("EDWIN ALONSO ARIZA CÁCERES") 
    print(f"AUTORES: \n{autores}") 

# OPCIÓN 3 SELECCIONADA
elif opcion_menu == 3:
    # VARIABLE licencia  string  Creative Commons
    licencia = "GNU Public License" 
    print(licencia) 
    
# OPCIÓN 4 SELECCIONADA
else:
    print("Cerrando la aplicación.")
    # SALIMOS DE LA APLICACIÓN
    exit(0) 