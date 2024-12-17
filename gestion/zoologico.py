
class Zoologico:
    def __init__(self, nombre = None, ubicacion = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, newZona):
        self._zonas.append(newZona)
    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        cont = 0

        for zona in self._zonas:
            cont += zona.cantidadAnimales()
        
        return cont
    
    def setNombre(self, newNombre):
        self._nombre = newNombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, newUbicacion):
        self._ubicacion = newUbicacion
    def getUbicacion(self):
        return self._ubicacion