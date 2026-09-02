# Utilidade do continue em laços

livros = [

    {"nome": "1984", "estoque": 5},

    {"nome": "Dom Casmurro", "estoque": 0},

    {"nome": "O Pequeno Príncipe", "estoque": 3},

    {"nome": "O Hobbit", "estoque": 0},

    {"nome": "Orgulho e Preconceito", "estoque": 2}

]

for livro in livros:
    if livro["estoque"] == 0:
        continue  # Pula para a próxima iteração se o estoque for zero
    print(f"Livro em disponível: {livro['nome']}")