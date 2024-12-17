from .animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
    
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, nuevoColorPlumas):
        self._colorPlumas = nuevoColorPlumas
    
    def movimiento(self):
        return "volar"
    
    @staticmethod
    def crearAguila(nombreAguila, edadAguila, generoAguila):
        aguila = Ave(nombreAguila, edadAguila, "montañas", generoAguila, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila
    
    @staticmethod
    def crearHalcon(nombreHalcon, edadHalcon, generoHalcon):
        halcon = Ave(nombreHalcon, edadHalcon, "montañas", generoHalcon, "café glorioso")
        Ave.halcones += 1
        return halcon
    