import unittest
from menu import menuOpciones
from manejadorEmpleados import controlEmpleados

def test():
    listaempleados = controlEmpleados()
    listaempleados.cargarEmpleados()
    menu = menuOpciones()
    menu.opciones(listaempleados)


if __name__ == "__main__":
    test()