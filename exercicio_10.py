# Exercício 10: Aprovando empréstimo

renda_mensal = float(input("Digite o valor da sua renda mensal(R$): "))
valor_parcela_desejada = float(input("Digite o valor da parcela desejada(R$): "))

if renda_mensal > 2000 and valor_parcela_desejada <= 0.3 * renda_mensal:
    print("Empréstmo aprovado")
elif renda_mensal <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")