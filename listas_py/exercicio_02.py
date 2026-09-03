# Adicionando itens à lista

linguagens = ["Python", "JavaScript", "Java"]
print(linguagens)

nova_linguagem = input("Digite o nome de uma nova linguagem: ")
print(nova_linguagem)

linguagens.append(nova_linguagem)
print(linguagens)

total_de_linguagens = len(linguagens)
print("Total de linguagens: ", total_de_linguagens)