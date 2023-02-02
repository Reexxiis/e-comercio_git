from BD_ECOMERCE.conexion import connection
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print("&&                                     &&")
            print("&&    -Gestion de la Base de Datos-    &&")
            print("&&                                     &&")
            print("&& 1.- Listar Tecnicos Registrados.    &&")
            print("&&                                     &&")
            print("&& 2.- Agregar un Nuevo Usuario.       &&")
            print("&&                                     &&")
            print("&& 3.- Actualizar Info de un Usuario.  &&")
            print("&&                                     &&")
            print("&& 4.- Eliminar un Usuario.            &&")
            print("&&                                     &&")
            print("&& 5.- Salir.                          &&")
            print("&&                                     &&")
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

            opcion = int(input("Selecciona la Operacion a Realizar: "))

            if opcion < 1 or opcion > 5:
                print("Opcion Invalida, Vuelve a ingresar la Opcion Correctamente.")

            elif opcion == 5:
                continuar = False
                print("Hasta Pronto!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    online = connection()

    if opcion == 1:
        try:
            tecnicos = online.listar_tecnicos()
            if len(tecnicos) > 0:
                funciones.listar_tecnicos(tecnicos)

            else:
                print("No se Encontraron Elementos para Mostrar.")

        except:
            print("Ocurrio un Error Inesperado.")

    elif opcion == 2:
        tecnicos = funciones.add_tecnico()
        try:
            tecnicos = online.add_tecnico()
            funciones.add_tecnico()
            print("Registro Realizado con Exito.")
        except:
            print("Error 404")


    elif opcion == 3:
        print("")

    elif opcion == 4:
        print("")

    elif opcion == 5:
        print("Hasta Pronto!")
        exit()

menuPrincipal()