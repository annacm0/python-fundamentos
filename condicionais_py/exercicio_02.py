# Exercício 2: Calculando o tempo total de projeto

atividade_A = int(input("Informe os dias para atividade A: "))
atividade_B = int(input("Informe os dias para atividade B: "))    
atividade_C = int(input("Informe os dias para atividade C: "))

if (atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0):
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total necessário para concluir as atividades é: {tempo_total} dias.")
else: 
    print("Erro: Os dias não podem ser negativos.")