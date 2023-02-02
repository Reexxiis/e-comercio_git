import mysql.connector
from mysql.connector import Error

class connection():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'tecnicos'
            )
        except Error as ex:
            print("Error durante la Conexion: {0}".format(ex))


    def listar_tecnicos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM tecnico ORDER BY ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar la conexion.")