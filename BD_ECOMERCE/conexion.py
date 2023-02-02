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
                cursor.execute("SELECT * FROM tecnico")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    def add_tecnico(self, tecnico):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO tecnico (nombre, apellido, num_local, telefono, direccion) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
                #insert_datos = cursor.execute(datos.format(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5] ))
                cursor.execute(sql.format(tecnico[0], tecnico[1], tecnico[2], tecnico[3], tecnico[4], tecnico[5]))
                self.conexion.commit()
                print("Datos Registrados Exitosamente.")
            except:
                print("No se Agregaron los Datos Correctamente.")