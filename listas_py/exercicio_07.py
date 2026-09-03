# Criando uma lista com for

carrinho = []

for i in range(3):
    produto = input("Digite um produto: ")
    carrinho.append(produto)

for produto in carrinho:
    print(produto)

