# Declaración de un diccionario
student = {
    "nombre": "Carlos",
    "edad": 22, 
    "curso": "Python"
    }

# Funciones útiles para diccionarios
print(student["nombre"])  # Acceder a un valor por clave
student["edad"] = 23      # Modificar un valor
print(student)
student["nota"] = 9.5     # Añadir un nuevo par clave-valor
print(student)
del student["curso"]      # Eliminar un par clave-valor
print(student)
print(student.keys())     # Obtener todas las claves
print(student.values())   # Obtener todos los valores

# Recorrer un diccionario
for key, value in student.items():
    print(f"{key}: {value}")