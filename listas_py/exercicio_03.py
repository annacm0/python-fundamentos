# Removendo itens de uma lista

tarefas = ["Estudar Python", "Fazer exercícios", "Ler documentação", "Atualizar GitHub", "Revisar conteúdo"]

print(tarefas)

tarefa_concluida = input("Qual dessas tarefas você concluiu? ")

tarefas.remove(tarefa_concluida)
print(tarefas)

tarefas_restantes = len(tarefas)
print("Tarefas restantes: ", tarefas_restantes)



