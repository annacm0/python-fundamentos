# Exercício 8: Calculando pedágio

distancia_percorrida = float(input("Digite a distância percorrida(km): "))

if distancia_percorrida <= 100:
    print("O valor do pedágio é de R$ 10,00.")
elif 100 < distancia_percorrida <= 200:
    print("O valor do pedágio é de R$ 20,00.")
else:
    print("O valor do pedágio é de R$ 30,00.")
