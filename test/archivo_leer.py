# LEEMOS EL ARCHIVO
archivo = open("README.md", "r") 
data = archivo.read()
print(data)
archivo.close()