# Declaración de un string
my_str = "Hola, Mundo!"

# Funciones útiles para strings
print(my_str.upper())        # Convertir a mayúsculas
print(my_str.lower())        # Convertir a minúsculas
print(my_str.count('o'))     # Contar ocurrencias de un carácter
print(my_str.find('Mundo'))  # Encontrar la posición de un substring
print(my_str.replace('Mundo', 'Python'))  # Reemplazar un substring

# Concatenación de strings
name = "Ana"
greeting = "Hola, " + name + "!"
print(greeting)

# Uso de f-strings
print(f"Hola, {greeting}!")