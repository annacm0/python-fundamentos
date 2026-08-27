# Exercício 6: Controle de acesso ao escritório

hora_atual = int(input("Digite a hora atual (0-23): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado")