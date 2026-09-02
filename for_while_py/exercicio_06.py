# Entendendo o uso do break

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

livro_encontrado = "O Hobbit"

for livro in livros:
    if livro == livro_encontrado:
        print(f"Livro encontrado: {livro}")
        break  # Interrompe o loop após encontrar o livro