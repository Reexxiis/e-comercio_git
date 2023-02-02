

def listar_tecnicos(tecnicos):
    print("Lista de Tecnicos Registrados: ")
    for tec in tecnicos:
        datos = "ID: {0} | Nombre: {1} | Apellido: {2} | Num. Local: {3} | Telefono: {4} | Direccion: {5} |"
        print(datos.format(tec[0], tec[1], tec[2], tec[3], tec[4], tec[5]))

print(" ")


"""def addTecnico(tecnicos):
    print("Ingresa los Datos del Nuevo Usuario: ")
    nombre = str(input("Ingresa el Nombre de Usuario: "))
    apellido = str(input(f"Introduce el Apellido de {nombre}: "))
    num_local = int(input(f"Introduce el Numero de Local de {nombre, apellido}: "))
    telefono = str(input("Introduce el Numero de Telefono: "))
    direccion = str(input("Introduce la Direccion: "))
"""
