# Exercício 1: Comparando vendas de frutas

macas = int(input("Digite a quantidade de maças vendidas:"))
bananas = int(input("Digite a quantidade de bananas vendidas:"))

if macas > bananas:
    print("Você vendeu mais maças do que bananas.")
elif bananas > macas:
    print("Você vendeu mais bananas do que maças.")
else:
    print("Você vendeu a mesma quantidade de maças e bananas.")

