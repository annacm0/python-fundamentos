# Exercício 4: Calculando o IMC (Índice de Massa Corporal)

peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso normal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")