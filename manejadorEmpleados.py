from zope.interface import implementer
import csv
from claseEmpleado import Empleado
from claseLista import Lista

from posicionInvalida import PosicionInvalidaException
from interfaceR import IEmpleado


@implementer(IEmpleado)
class controlEmpleados:
    __empleados: list

    def __init__(self):
        self.__empleados = Lista()
        self.__len = 3

    def cargarEmpleados(self):
        archivo = open('empleados.csv')
        reader = csv.reader(archivo, delimiter=';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                dni = str(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                telefono = str(fila[3])
                empleado = Empleado(dni, nombre, direccion, telefono)
                self.agregarElemento(empleado)
        archivo.close

    def agregarElemento(self, empleado):
        self.__empleados.agregarEmpleado(empleado)

    def insertarElemento(self, empleado, posicion):
        if posicion < 0 or posicion > self.__empleados.getTope():  # self.__len:
            raise PosicionInvalidaException("La posicion no es valida")
        else:
            self.__empleados.insertarEmpleado(posicion, empleado)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion > self.__empleados.getTope():
            raise PosicionInvalidaException("La posicion no es valida")
        else:
            return self.__empleados.mostrarEmpleado(posicion)

    def mostrarLista(self):
        self.__empleados.listarDatosEmpleados()