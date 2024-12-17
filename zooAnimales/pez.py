from .animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas = None, cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)
    
    def setColorEscamas(self, newColor):
        self._colorEscamas = newColor
    def getColorescamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, newCantidad):
        self._cantidadAletas = newCantidad
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def movimiento():
        return "nadar"
    
    def cantidadPeces():
        return len(Pez.listado)
    
    def crearSalmon(nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return salmon
    
    def crearBacalao(nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return bacalao