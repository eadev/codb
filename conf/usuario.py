import os
import os.path
from os import path
import json
from plugins.theme.bcolors import Bcolors

class Usuario:
    '''
    NOS PERMITE CREAR UNA CARPETA DE CONFIGURACION 
    '''
    def establecer_home(self):
        # ARCHIVO DE CONFIGURACIÓN DE LA APLICACIÓN
        config_folder = os.path.expanduser("~") +  "/.codb/ "   
        # VERIFICAMOS SI EL DIRECTORIO EXISTE Y SI NO LO CREAMOS
        if not path.exists(config_folder):
            # CREAMOS LA CARPETA PORQUE ELARCHIVO NO EXISTE.
            os.makedirs(config_folder)    
    '''
    NOS PERMITE CREAR UN ARCHIVO DE CONFIGURACION
    '''
    def crear_config(self):
        # ARCHIVO DE CONFIGURACIÓN DE LA APLICACIÓN
        usuario_config = os.path.expanduser("~") +  "/.codb/config"
        if not path.exists(usuario_config):
            # CREAMOS LA CARPETA PORQUE ELARCHIVO NO EXISTE.
            archivo = open(usuario_config, "w")
            archivo.close()
    '''
    NOS PERMITE AGREGAR UNA NUEVA BASE DE DATOS
    '''
    def agregar_database(self, host, usuario, clave , base_datos, etiqueta):
        usuario_config = os.path.expanduser("~") +  "/.codb/config"
        # LEEMOS EL ARCHIVO
        archivo = open(usuario_config, "r")
        data = archivo.read()
        archivo.close()
        # PROCESAMOS EL CONTENIDO 
        if len(data) > 0:
            data = json.loads(data)
        else: 
            data = []
        # GENERAMOS EL ITEM DE LA NUEVA BASE DE DATOS
        nueva_bd = { "host":host, "usuario": usuario, "clave": clave, "base_datos": base_datos, "etiqueta": etiqueta }
        # AGREGAOS LA NUEVA BASE DE DATOS AL REGISTRO DEL USUARIO
        data.append(nueva_bd)
        data = json.dumps(data, indent = 4)
        # GUARDAMOS LOS REGISTROS JSON.
        archivo = open(usuario_config, "w")
        archivo.write(data)
        archivo.close()
    '''
    MOSTRAMOS LAS BASES DE DATOS DISPONIBLES
    '''
    def bases_datos_disponibles(self):
        usuario_config = os.path.expanduser("~") +  "/.codb/config"
        # LEEMOS EL ARCHIVO
        archivo = open(usuario_config, "r")
        data = archivo.read()
        archivo.close()
        # PROCESAMOS EL CONTENIDO 
        opciones = []
        if len(data) > 0:
            data = json.loads(data)
            cont = 1
            print(f"{Bcolors.BOLD}Elige una conexión de las disponibles:{Bcolors.END}")
            print("0. [CREAR UNA NUEVA CONEXIÓN].")
            for item in data:
                opcion = f"{Bcolors.BOLD}{cont}{Bcolors.END}. {str(item['etiqueta']).upper()}."
                print(opcion)
                opciones.append(item)
                cont += 1
            opt = -1
            while opt < 0 or opt >= cont:
                opt = int(input("¿Cuál quieres utilizar?: "))
            if opt == 0:
                return 0
            else:
             return opciones[opt - 1]
        else: 
            return 0

if __name__ == "__main__":
    ousuario = Usuario()
    opcion = ousuario.bases_datos_disponibles()
    print(opcion)