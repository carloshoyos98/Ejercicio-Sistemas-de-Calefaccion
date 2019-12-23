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

# Primera implementación de Calefaccion
# Clase Chimenea que hereda de Calefaccion


class Chimenea(Calefaccion):

    # Hay que definir todos los métodos abstractos de Calefaccion
    # para poder instanciar Chimenea

    def encender(self):
        self.quemarCombustible()
        print('Dando calor y ardiendo con todo')

    def apagar(self):
        print('Apagando la chimenea')

    def cargarCombustible(self, cantidad):
        self.combustible = cantidad

    def quemarCombustible(self):
        self.combustible -= 1

# Segunda implementación de Calefaccion, SueloRadiante


class SueloRadiante(Calefaccion):

    def encender(self):
        self.quemarCombustible()
        print('Metiendo gas a tus pies')

    def apagar(self):
        print('Apagando el suelo')

    def cargarCombustible(self, cantidad):
        self.combustible = cantidad

    def quemarCombustible(self):
        self.combustible -= 2

# Implementaciones de Sensor


class Termometro(Sensor):

    def leer(self):
        return 15


class Termostato(Sensor):

    def leer(self):
        return 15

# Ahora implementamos todo el sistema con:
# Chimenea y termostato
# Creamos un objeto de cada clase


chimenea = Chimenea()
termo = Termostato()

# Sacamos por pantalla la temperatura

print(termo.leer())

# Instanciamos el sistema de calefaccion

sistema_chimenea = SistemaCalefaccion(chimenea, termo)

# Damos valor a la cantidad de combustible

chimenea.cargarCombustible(5)

# Encendemos el sistema con la temperatura que esperamos

sistema_chimenea.on(22)
