from .animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje = None, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "padrera", genero, True, 4)
        Mamifero.caballos += 1
        return caballo

    @staticmethod 
    def crearLeon(nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return leon
    
    def cantidadMamiferos():
        return len(Mamifero.listado)
    
    def serPelaje(self, newPelaje):
        self._pelaje = newPelaje
    def isPelaje(self):
        return self._pelaje
    
    def setPatas(self, newPatas):
        self._patas = newPatas
    def getPatas(self):
        return self._patas
    