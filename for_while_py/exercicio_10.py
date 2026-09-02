# Validação de entrada para login

nome_do_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if len(nome_do_usuario) < 5:
    print("O nome de usuário deve ter pelo menos 5 caracteres.")
elif len(senha) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
else:
    print("Cadastro realizado com sucesso.")