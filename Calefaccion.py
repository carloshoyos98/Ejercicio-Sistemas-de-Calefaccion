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

# La clase Sensor también será una interfaz para otras clases.


class Sensor(metaclass=ABCMeta):

    @abstractmethod
    def leer(self):
        pass

# La clase SistemaCalefaccion será la clase principal, que no debe depender
# de las imlpementaciones de Calefaccion y Sensor.


class SistemaCalefaccion():

    # Definimos los atributos de la clase

    def __init__(self, calefaccion, sensor):
        self.calefaccion = calefaccion
        self.sensor = sensor
        self.temperaturaObjetivo = None

    def on(self, temperaturaObjetivo):

        self.temperaturaObjetivo = temperaturaObjetivo

        while(self.__sensor.leer() < self.temperaturaObjetivo) & (self.__calefaccion.combustible > 0):
            self.__calefaccion.encender()
            print('Quedan : ', self.__calefaccion.combustible)

        self.off()

    def off(self):
        self.__calefaccion.apagar()
