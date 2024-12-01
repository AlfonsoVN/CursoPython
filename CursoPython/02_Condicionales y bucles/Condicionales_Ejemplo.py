# Programa para clasificar números como pares o impares y contar hasta un número dado

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando un bucle for para clasificar números
for number in numbers:
    if number % 2 == 0:
        print(f"{number} es par")
    else:
        print(f"{number} es impar")

# Usando un bucle while para contar hasta un número dado
count = 0
max_count = 5

while count <= max_count:
    print(f"Contador: {count}")
    count += 1