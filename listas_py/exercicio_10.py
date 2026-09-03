# Cadastro de participantes

participantes = []

while True:
    nome_participante = input("Digite o nome de um participante ou 'sair' para encerrar: ")

    if nome_participante == "sair":
        break

    participantes.append(nome_participante)

print("\nParticipantes cadastrados:")

for participante in participantes:
    print(participante)

total_de_participantes = len(participantes)

print("Total de participantes:", total_de_participantes)
