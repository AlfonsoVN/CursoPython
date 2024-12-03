# Ejemplo de uso de break
print("Ejemplo de uso de break:")
for i in range(10):
    if i == 5:
        break  # Termina el bucle cuando i es igual a 5
    print(i)
# Salida: 0 1 2 3 4

# Ejemplo de uso de continue
print("\nEjemplo de uso de continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta a la siguiente iteración si i es par
    print(i)
# Salida: 1 3 5 7 9

# Ejemplo de uso de pass
print("\nEjemplo de uso de pass:")
for i in range(10):
    if i % 2 == 0:
        pass  # No realiza ninguna acción, solo un marcador de posición
    else:
        print(i)
# Salida: 1 3 5 7 9
