from claseEmpleado import Empleado


class menuOpciones:
    __opcion: int

    def __init__(self):
        self.__opcion = 0

    def opciones(self, listaemplados):
        while self.__opcion != 4:
            print("Menu de opciones")
            print("1)- Insertar un empleado")
            print("2)- Mostrar un empleado")
            print("3)- Mostrar todos los empleados")
            print("4) SALIR")
            self.__opcion = int(input("Ingrese una opcion: "))

            if self.__opcion == 1:
                pos = int(input("Ingrese una posicion para insertar un empleado: "))
                dni = str(input("Ingrese el dni del empleado: "))
                nombre = str(input("Ingrese el nombre del empleado: "))
                direccion = str(input("Ingrese la direccion del empleado: "))
                telefono = str(input("Ingrese el telefono del empleado: "))
                empleado = Empleado(dni, nombre, direccion, telefono)
                listaemplados.insertarElemento(empleado, pos)

            elif self.__opcion == 2:
                pos = int(input("Ingrese una posicion para mostrar un empleado: "))
                print(listaemplados.mostrarElemento(pos))

            elif self.__opcion == 3:
                listaemplados.mostrarLista()