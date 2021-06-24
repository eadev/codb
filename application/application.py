'''
APLICACIÓN PARA LA ADMINSITRACIÓN DE BASES DE DATOS EN UN ENTORNO CLI
@author: EDWIN ARIZA <me@edwinariza.com>
@copyright: GNU Public License 
'''
import pymysql  
import stdiomask
import os
from tabulate import tabulate
from start.welcome import Welcome
from plugins.theme.bcolors import Bcolors
from core.menu import Menu
from core.pantalla import Pantalla
from conf.usuario import Usuario

'''
METODO INICIAL DE EJECUCIÓN
'''
def main():
    # OBJETO PANTALLA
    opantalla = Pantalla()
    # LIMPIAMOS LA PANTALLA
    opantalla.limpiar()
    # INICIAMOS LA VISTA DE BIENVENIDA
    ostart = Welcome()
    ostart.start()

    # PALABRAS RESERVADAS DE LA APLICACIÓN 
    palabras_reservadas = ('exit', 'clear')
    # SOLICITAMOS UN ENTER PARA CONTINUAR
    tecla = input(f"{Bcolors.WARNING}Presiona [ENTER] para continuar...{Bcolors.END}")
    # LIMPIAMOS LA PANTALLA CUANDO SE PRESIONE CUALQUIER TECLA
    opantalla.limpiar()

    # GENERAMOS EL MENU DE LA APLICACION 
    omenu = Menu()
    # CREAMOS EL OBJETO USUARIO
    ousuario = Usuario()
    opcion_menu = 1
    # CICLO PARA MANTENER LA APLICACIÓN ABIERTA
    while opcion_menu != 4:
        # MOSTRAMOS EL MENÚ DE OPCIONES
        opcion_menu = omenu.mostrar()
        # ACCIONES ASOCIADAS A OPCIÓN DE MENÚ SELECCIONADA
        if opcion_menu == 1:
            # MOSTRAMOS LAS BASES DE DATOS GUARDADAS
            opantalla.limpiar()
            opcion = ousuario.bases_datos_disponibles()
            if opcion == 0:
                confirmacion = False  # PERMITE SABER SI EL USUARIO CONFIRMO Y SI NO SE REPITE
                host = input(f"{Bcolors.WARNING}HOST DB: {Bcolors.END}")
                usuario = input(f"{Bcolors.WARNING}USUARIO BD: {Bcolors.END}")
                # clave = input(f"{Bcolors.WARNING}CLAVE BD: {Bcolors.END}")
                clave = stdiomask.getpass(prompt=f"{Bcolors.WARNING}CLAVE BD: {Bcolors.END}", mask='*')
                base_datos = input(f"{Bcolors.WARNING}NOMBRE BD: {Bcolors.END}")
                etiqueta = input(f"{Bcolors.WARNING}ETIQUETA (opcional, almacena los datos): {Bcolors.END}")
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
                while confirma not in ("S","s","N","n"):
                    confirma = input("Confirmas (S/s/N/n): ")
                # REGISTRAMOS LOS DATOS DE CONEXIÓN EN LOS ARCHIVOS DE CONFIGURACIÓN
                if etiqueta.strip() != "":
                    ousuario.establecer_home()
                    ousuario.crear_config()
                    ousuario.agregar_database(host, usuario, clave, base_datos, etiqueta)
                opantalla.limpiar()
            else:
                opantalla.limpiar()
                etiqueta = opcion['etiqueta']
                print(f"Cargando la conexión {Bcolors.BOLD}{etiqueta.upper()}{Bcolors.END}...")
                host = opcion['host']
                usuario =  opcion['usuario']
                clave = opcion['clave']
                base_datos = opcion['base_datos']

            # CONECTAR A LA BASE DE DATOS  
            try:
                connection = pymysql.connect(host=host,
                                        user=usuario,
                                        password=clave,
                                        database=base_datos,
                                        cursorclass=pymysql.cursors.DictCursor)
                print(f"Conectados a la base de datos {Bcolors.BOLD}{base_datos}{Bcolors.END} con el usuario {Bcolors.BOLD}{usuario}{Bcolors.END}.")
                # GENERAR UN CURSOR PARA RECORRER LA BASE DE DATOS
                cursor = connection.cursor()
                # SENTENCIA SQL A EJECUTAR
                sql = ""
                # EJECUTAMOS LA CARGA DE LAS SENTENCIAS SQL O COMANDOS
                while sql != 'exit':
                    sql = input(f"{Bcolors.WARNING}SQL/>:{Bcolors.OKBLUE} ")
                    if (sql.strip()).lower() not in palabras_reservadas:
                        try:
                            #EJECUTAR LA SENTENCIA SQL
                            respuesta = cursor.execute(sql)
                            # REFLEJAMOS LOS CAMBIOS EN LA BASE DE DATOS
                            connection.commit()
                            # OBTENER EL RESULTADO
                            datos = cursor.fetchall()  
                            # IMPRIMIR EL RESULTADO
                            if len(datos) > 0:
                                print(Bcolors.OKCYAN+tabulate(datos, headers="keys", tablefmt="fancy_grid")+Bcolors.END)
                            print(Bcolors.WARNING+"\n>> "+Bcolors.OKCYAN+f"Filas Afectadas: {respuesta}"+Bcolors.END+"\n")
                        except pymysql.Error as e:
                            print(Bcolors.FAIL+Bcolors.BOLD+f"Error {e.args[0]}:"+Bcolors.END+Bcolors.FAIL+ f" {e.args[1]}"+Bcolors.END)
                    elif (sql.strip()).lower() == 'clear':
                        opantalla.limpiar()
                # CERRAMOS LA CONEXIÓN A LA BASE DE DATOS
                connection.close()
            except pymysql.Error as e:
                print(Bcolors.FAIL+ Bcolors.BOLD + f"Error {e.args[0]}:" + Bcolors.END+Bcolors.FAIL + f" {e.args[1]}"+Bcolors.END)
                tecla = input(f"{Bcolors.WARNING}Presiona [ENTER] para continuar...{Bcolors.END}")

        # OPCIÓN 2 SELECCIONADA
        elif opcion_menu == 2:
            opantalla.limpiar()
            # IMPRIMIR LOS AUTORES 
            autores = ("EDWIN ALONSO ARIZA CÁCERES <me@edwinariza.com>") 
            print(f"{Bcolors.BOLD}AUTORES: {Bcolors.END}\n{autores}") 
            tecla = input(f"{Bcolors.WARNING}Presiona [ENTER] para continuar...{Bcolors.END}")

        # OPCIÓN 3 SELECCIONADA
        elif opcion_menu == 3:
            opantalla.limpiar()
            # VARIABLE licencia 
            licencia = "License :: OSI Approved :: MIT License" 
            print(licencia) 
            tecla = input(f"{Bcolors.WARNING}Presiona [ENTER] para continuar...{Bcolors.END}")
            
        # OPCIÓN 4 SELECCIONADA
        else:
            opantalla.limpiar()
            print(f"{Bcolors.OKBLUE}Bye, see you soon.{Bcolors.END}")
            tecla = input(f"{Bcolors.WARNING}Presiona [ENTER] para salir...{Bcolors.END}")
            # SALIMOS DE LA APLICACIÓN
            exit(0) 
    

# PERMITE LA EJECUCIÓN INDIVIDUAL
if __name__ == '__main__':
    main()