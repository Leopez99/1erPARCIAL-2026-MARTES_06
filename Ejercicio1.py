class Pokemon:
    """Un Pokemon con su nombre, su tipo y su nivel (entre 1 y 100)."""

    def __init__(self, nombre, tipo, nivel = 1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        """Incrementa el nivel en 1, siempre que no supere el nivel 100."""
        NIVEL_MAXIMO = 100

        if self.nivel >= NIVEL_MAXIMO:
            raise ValueError("El Pokemon ya alcanzo el nivel maximo (100).")

        self.nivel = self.nivel + 1


    def __str__(self):
        return ("Nombre: " + self.nombre
                + ", Tipo: " + self.tipo
                + ", Nivel:" + str(self.nivel))



