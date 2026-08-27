# Exercício 7: Classificando estudantes por média

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media_final = (primeira_nota + segunda_nota + terceira_nota) / 3

if media_final >= 7:
    print("Aprovado")
elif 5 <= media_final < 7:
    print("Recuperação")
else:
    print("Reprovado")
