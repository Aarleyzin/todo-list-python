class TodoList:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, tarefa):
        status = "Pendente"
        self.tarefas.append({"tarefa": tarefa, "status": status})
        print(f"\nTarefa '{tarefa}' adicionada com sucesso!")
        
    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada!")
            return
        
        print("\nLista de Tarefas:")
        for i, item in enumerate(self.tarefas, 1):
            print(f"{i}. {item['tarefa']} - Status: {item['status']}")
            
    def concluir_tarefa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            self.tarefas[indice-1]["status"] = "Concluída"
            print(f"\nTarefa '{self.tarefas[indice-1]['tarefa']}' marcada como concluída!")
        else:
            print("\nÍndice inválido!")
            
    def remover_tarefa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice-1)
            print(f"\nTarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
        else:
            print("\nÍndice inválido!")

def menu():
    print("\n=== Menu da Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    todo_list = TodoList()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            tarefa = input("\nDigite a nova tarefa: ")
            todo_list.adicionar_tarefa(tarefa)
            
        elif opcao == "2":
            todo_list.listar_tarefas()
            
        elif opcao == "3":
            todo_list.listar_tarefas()
            try:
                indice = int(input("\nDigite o número da tarefa a ser concluída: "))
                todo_list.concluir_tarefa(indice)
            except ValueError:
                print("\nPor favor, digite um número válido!")
                
        elif opcao == "4":
            todo_list.listar_tarefas()
            try:
                indice = int(input("\nDigite o número da tarefa a ser removida: "))
                todo_list.remover_tarefa(indice)
            except ValueError:
                print("\nPor favor, digite um número válido!")
                
        elif opcao == "5":
            print("\nObrigado por usar o programa! Até mais!")
            break
            
        else:
            print("\nOpção inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()
