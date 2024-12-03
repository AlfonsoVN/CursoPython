# Declaración de un set
colors = {"rojo", "verde", "azul"}

# Funciones útiles para sets
colors.add("amarillo")  # Añadir un elemento
print(colors)
colors.remove("verde")  # Eliminar un elemento
print(colors)
print("rojo" in colors)  # Comprobar si un elemento está en el set
print(len(colors))       # Longitud del set

# Operaciones con sets
other_colors = {"negro", "blanco", "rojo"}
print(colors.union(other_colors))  # Unión de sets
print(colors.intersection(other_colors))  # Intersección de sets
