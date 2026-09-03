# Verificando um item na lista

usuarios = ["Ana", "Carlos", "Mariana", "Pedro", "Lucas"]

print(usuarios)

usuario_verificar = input("Digite o nome de um usuário para verificar se ele está na lista: ")

if usuario_verificar in usuarios:
    print("Usuário encontrado.")
else:   
    print("Usuário não encontrado")