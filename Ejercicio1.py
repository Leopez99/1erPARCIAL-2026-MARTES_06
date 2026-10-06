class Pokemon:
    def __init__(self, nombre, tipo, nivel = 1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        #Incrementa el nivel en 1, siempre que no supere el nivel 100
        NIVEL_MAXIMO = 100

        if self.nivel >= NIVEL_MAXIMO:
            raise ValueError("El Pokemon ya alcanzo el nivel maximo (100).")

        self.nivel = self.nivel + 1


    def __str__(self):
        return ("Nombre: " + self.nombre
                + ", Tipo: " + self.tipo
                + ", Nivel:" + str(self.nivel))

    
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) >= 6:
            raise ValueError("No se puede tener mas de 6 pokemones")
        else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0

        suma_niveles = 0

        for pokemon in self.equipo:
            suma_niveles += pokemon.nivel

        return suma_niveles / len(self.equipo)




