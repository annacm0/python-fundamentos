# Exercício 3: Temperatura dos servidores

tempertura_atual = float(input("Informe a temperatura atual do servidor em °C: "))

if tempertura_atual <= 25:
    print("A temperatura do servidor está dentro do limite seguro.")
else:
    print("Alerta! Temperatura acima do limite seguro.")