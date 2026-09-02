# Exercício 5: Controlando o orçamento mensal

despesas_mensais = float(input("Digite o total de despesas do mês (R$): "))

if despesas_mensais <= 3000:
    print("As despesas estão dentro do orçamento.")
else:
    print("Alerta! As despesas estão acima do orçamento.")