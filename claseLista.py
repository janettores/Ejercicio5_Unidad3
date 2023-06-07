from zope.interface import implementer

from interfaceR import IEmpleado
from claseNodo import Nodo


# @implementer(IEmpleado)

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def agregarEmpleado(self, Empleado):
        nodo = Nodo(Empleado)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def listarDatosEmpleados(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def insertarEmpleado(self, posicion, empleado):
        nuevo = Nodo(empleado)
        contador = 0
        if self.__comienzo == None:
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        elif (contador == posicion):
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            p = self.__comienzo
            anterior = self.__comienzo
            while (p != None) and (posicion > contador):
                anterior = p
                p = p.getSiguiente()
                contador += 1
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(p)
            # print("El elemento ha sido insertado en el lugar que corrseponde")

    def mostrarEmpleado(self, posicion):
        contador = 0
        aux = self.__comienzo
        while aux != None and contador != posicion:
            aux = aux.getSiguiente()
            contador += 1
        if contador == posicion:
            return aux.getDato()

    def getTope(self):
        return self.__tope

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato