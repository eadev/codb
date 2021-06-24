import pymysql
# CONECTAR A LA BASE DE DATOS
connection = pymysql.connect(host='test-db.cmsps5wd6hoj.ca-central-1.rds.amazonaws.com',
                             user='admin',
                             password='2d8JAZ9Vcy',
                             database='codb',
                             cursorclass=pymysql.cursors.DictCursor)

print("Conectados a la base de datos.")
# GENERAR UN CURSOR PARA RECORRER LA BASE DE DATOS
cursor = connection.cursor()
# SENTENCIA SQL A EJECUTAR
sql = "SELECT * FROM usuarios"
# sql = "INSERT INTO usuarios (nombre, email) VALUES ('Usuario 3','email_3@domino.com')"
# sql = "UPDATE usuarios SET nombre = 'Alonso' WHERE id = 1"
#EJECUTAR LA SENTENCIA SQL
respuesta = cursor.execute(sql)
connection.commit()
print(f"Filas Afectadas: {respuesta}")
# OBTENER EL RESULTADO
result = cursor.fetchall()  
# IMPRIMIR EL RESULTADO
print(result)