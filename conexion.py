import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'tecnicos'
    )

    if conexion.is_connected():
        print("Conexion Exitosa.")
        infoServer = conexion.get_server_info()
        print("Info del servidor:", infoServer)
except Error as ex:
    print("Error durante la Conexion.", ex)

finally:
    if conexion.is_connected():
        conexion.close()    # se cierra la conexion a la BD
        print("La conexion ha finalizado exitosamente")