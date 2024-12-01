# Función que retorna múltiples valores
def calculate(a, b):
    """
    Esta función recibe dos números y retorna su suma, resta, multiplicación y división.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero no permitida"
    return suma, resta, multiplicacion, division

# Llamada a la función y desempaquetado de los valores retornados
sum_result, sub_result, mul_result, div_result = calculate(10, 5)
print(f"Suma: {sum_result}, Resta: {sub_result}, Multiplicación: {mul_result}, División: {div_result}")


# Función lambda para sumar dos números
sum_lambda = lambda x, y: x + y

# Uso de la función lambda
print(f"La suma de 5 y 3 es: {sum_lambda(5, 3)}")