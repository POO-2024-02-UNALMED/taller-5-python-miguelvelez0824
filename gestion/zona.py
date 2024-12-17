class Zona:
    def __init__(self, nombre = None, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def getNombre(self):
        return self._nombre
    def setNombre(self, newNombre):
        self._nombre = newNombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self, newZoo):
        self._zoo = newZoo

    def cantidadAnimales(self):
        return len(self._animales)
    
    def agregarAnimales(self, newAnimal):
        self._animales.append(newAnimal)