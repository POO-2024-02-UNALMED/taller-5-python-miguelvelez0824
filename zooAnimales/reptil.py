from .animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas = None, largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
    
    def setColorEscamas(self, newColor):
        self._colorEscamas = newColor
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, newLargo):
        self._largoCola = newLargo
    def getLargoCola(self):
        return self._largoCola
    
    def cantidadReptiles():
        return len(Reptil.listado)
    
    def movimiento():
        return "reptar"
    
    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana
    
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente