class Nodo:

    __empleado : object
    __siguiente : object

    def __init__(self, empleado):
        self.__empleado = empleado
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__empleado