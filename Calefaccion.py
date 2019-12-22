# Este Ejercico es de POO y el principio D de SOLID

from abc import ABCMeta, abstractmethod

# La clase Calefaccion que creamos seria una interfaz
# Por eso los métodos que definimos están vacíos


class Calefaccion(metaclass=ABCMeta):
    def __init__(self):
        self.combustible = None

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def cargarCombustible(self, unidades):
        pass

    @abstractmethod
    def quemarCombustible(self):
        pass
