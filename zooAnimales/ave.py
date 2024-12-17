from .animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
    
    def setColorPlumas(self, newColor):
        self._colorPlumas = newColor
    def getColorPlumas(self):
        return self._colorPlumas
    
    def movimiento():
        return "volar"
    
    def cantidadAves():
        return len(Ave.listado)
    
    @staticmethod
    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "montañas", genero, "café glorioso")
        Ave.halcones += 1
        return halcon
    
    @staticmethod
    def crearAguila(nombre, edad, genero):
        aguila = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila