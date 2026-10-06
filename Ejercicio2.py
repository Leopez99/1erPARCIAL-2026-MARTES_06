class PokemonNode:
    def __init__(self, nombre, siguiente):
        self.nombre = nombre
        self.siguiente = None

    def buscar_pokemon(nodo, nombre_pokemon):
        if nodo is None:
            return False
        if nodo.nombre == nombre_pokemon:
            return True

        # Caso recursivo: no era el nodo actual, se sigue con el siguiente.
        return PokemonNode.buscar_pokemon(nodo.siguiente, nombre_pokemon)

"""
Teoria: Cual es el tiempo de ejecucion estimado de la funcion buscar_pokemon()?
Es O(n), o sea tiempo lineal, donde n es la cantidad de nodos de la lista.

la funcion va nodo por nodo, comparando el nombre. 
En cada paso hace una comparacion y se llama a si misma con el siguiente nodo.
"""