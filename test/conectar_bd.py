import pymysql
# CONECTAR A LA BASE DE DATOS
connection = pymysql.connect(host='',
                             user='',
                             password='',
                             database='',
                             cursorclass=pymysql.cursors.DictCursor)

print("Conectados a la base de datos.")
# GENERAR UN CURSOR PARA RECORRER LA BASE DE DATOS
cursor = connection.cursor()
# SENTENCIA SQL A EJECUTAR
sql = "SELECT id, nombre, email FROM usuarios"
#EJECUTAR LA SENTENCIA SQL
cursor.execute(sql)
# OBTENER EL RESULTADO
result = cursor.fetchall()  
# IMPRIMIR EL RESULTADO
print(result)