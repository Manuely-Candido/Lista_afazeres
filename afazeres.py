lista_tarefas = []
while True:
    print("""
*****************************
*     LISTA                 *
*           DE              *
*              AFAZERES     *
*****************************
* 1 - iNSERIR TAREFA        *
* 2 - LISTAR TAREFA         *
* 3 - MARCAR COMO CONCLUIDO *
* 4 - REMOVER TAREFA        *
* 0 - SAIR                  *
*****************************
""")
    lista = int(input("Escolha um número: "))
    
    if lista == 1:
        print("Você escolheu a opção número 1")
        adicionartarefa = input("Adicione a tarefa: ")
        lista_tarefas.append(adicionartarefa)
        print (lista_tarefas)

    elif lista == 2:
        print("Você escolheu o número 2")
        for tarefa in lista_tarefas:
            print(tarefa)
        

    elif lista == 3:
        print("Você escolheu o número 3")
        concluido = input("Qual das tarefas você quer marcar concluída?")
        print()

    elif lista == 4:
        print("Você escolheu o número 4")
        item_removido = input("Qual tarefa voce deseja remover: ")
        lista_tarefas


        lista_tarefas.remove
    elif lista == 0:
        print("Você escolheu sair")
        break