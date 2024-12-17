from .animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado(self)
    
    def setColorPiel(self, newColor):
        self._colorPiel = newColor
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, newVeneno):
        self._venenoso = newVeneno
    def isVenenoso(self):
        return self._venenoso
    
    def cantidadAnfibios():
        return len(Anfibio.listado)
    
    def movimiento():
        return "saltar"
    
    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana
    
    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra