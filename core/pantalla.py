import os
class Pantalla:
    def limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')