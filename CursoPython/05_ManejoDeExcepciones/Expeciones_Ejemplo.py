def divide_numbers(a, b):
    """
    Divide dos números y maneja la división por cero.
    """
    try:
        # Bloque de código que puede generar una excepción
        result = a / b
    except ZeroDivisionError:
        # Bloque de código que se ejecuta si ocurre una excepción
        return "Error: División por cero no permitida."
    else:
        # Bloque de código que se ejecuta si no ocurre ninguna excepción
        return f"El resultado de la división es: {result}"
    finally:
        # Bloque de código que se ejecuta siempre, ocurra o no una excepción
        print("Operación de división completada.")

# Ejemplo de uso de la función divide_numbers
print(divide_numbers(10, 2))  # No hay excepción, se ejecuta el bloque else
print(divide_numbers(10, 0))  # Ocurre una excepción, se ejecuta el bloque except
