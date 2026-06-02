# Faça um algoritmo que leia e tenha um 
# vetor e apresente o seguinte menu:
# 	1 - Inserir item
# 	2 - Retirar item
# 	3 - Listar itens (um elemento por linha)
# 	4 - Retirar todos os itens
# 	5 - Sair

vetor = []

while True:
    print("\nMENU")
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = input("Digite o item: ")
        vetor.append(item)

    elif opcao == 2:
        item = input("Digite o item para remover: ")

        if item in vetor:
            vetor.remove(item)
            print("Item removido.")
        else:
            print("Item não encontrado.")

    elif opcao == 3:
        print("\nItens do vetor:")
        
        if len(vetor) == 0:
            print("Vetor vazio.")
        else:
            for item in vetor:
                print(item)

    elif opcao == 4:
        vetor.clear()
        print("Todos os itens foram removidos.")

    elif opcao == 5:
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")