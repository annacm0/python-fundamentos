# Separando números pares

numeros = [12, 5, 8, 3, 20, 17, 4, 10]
print("Números originais:", numeros)

numeros_pares = []

for numero in numeros:
    if numero %2 == 0:
        numeros_pares.append(numero)

print("Números pares:", numeros_pares)