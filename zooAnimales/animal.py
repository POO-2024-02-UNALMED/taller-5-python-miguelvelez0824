class Animal:
    totalAnimales = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.totalAnimales += 1

    def movimiento(self):
        return("desplazarse")
    
    @staticmethod
    def totalPorTipo():
        from .mamifero import Mamifero
        from .anfibio import Anfibio
        from .ave import Ave
        from .pez import Pez
        from .reptil import Reptil
        mensaje = f"Mamiferos : {len(Mamifero.listado)}\nAves : {len(Ave.listado)}\nReptiles : {len(Reptil.listado)}\nPeces : {len(Pez.listado)}\nAnfibios : {len(Anfibio.listado)}"
        return mensaje

    def __str__(self):
        if self._zona == None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getnombre()}, en el {self._zona.getZoo().getNombre()}."
        
    def getTotalAnimales(self):
        return Animal.totalAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, newNombre):
        self._nombre = newNombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self, newEdad):
        self._edad = newEdad
    
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,newHabitat):
        self._habitat = newHabitat

    def getGenero(self):
        return self._genero
    def setGenero(self, newGenero):
        self._genero = newGenero

    def getZona(self):
        return self._zona
    def setZona(self, newZona):
        self._zona = newZona