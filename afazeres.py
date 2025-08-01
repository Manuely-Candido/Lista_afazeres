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
        #cont = 0
        for tarefa in lista_tarefas:
            print(tarefa) #print(f"{cont} - {tarefa})
            #cont +=1
        

    elif lista == 3:
        print("Você escolheu o número 3")
        for tarefa in lista_tarefas:
            print (tarefa)
            concluido = input("Qual das tarefas você quer marcar concluída?: ")
            lista_tarefas[concluido] = lista_tarefas[concluido] + "( x )"
          

    elif lista == 4:
        print("Você escolheu o número 4")
        #lista_tarefas()
        item_removido = input("Qual tarefa voce deseja remover: ")
        #lista_tarefas.pop(item_removido)
        lista_tarefas.remove(item_removido)
        print(lista_tarefas)

    elif lista == 0:
        print("Você escolheu sair")
        break