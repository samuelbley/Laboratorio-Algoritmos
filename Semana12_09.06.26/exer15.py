def inserir_lote(lotes):
    codigo = int(input("Digite o código do lote: "))

    if codigo % 2 != 0:
        print("Erro! O código do lote deve ser par.")
    else:
        lotes.append(codigo)
        print("Lote inserido com sucesso!")


def listar_lotes(lotes):
    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")
    else:
        print("Lotes cadastrados:")
        for i in range(len(lotes)):
            print(lotes[i])


def retirar_lote(lotes):
    codigo = int(input("Digite o código do lote que deseja retirar: "))

    if codigo in lotes:
        lotes.remove(codigo)
        print("Lote retirado com sucesso!")
    else:
        print("Lote não encontrado.")


def limpar_lotes(lotes):
    lotes.clear()
    print("Todos os lotes foram removidos.")


def contar_maior_que_x(lotes):
    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")
    else:
        x = int(input("Digite o valor de X: "))
        contador = 0

        for i in range(len(lotes)):
            if lotes[i] > x:
                contador = contador + 1

        print(f"Quantidade de lotes maiores que {x}: {contador}")


def verificar_lote(lotes):
    codigo = int(input("Digite o código que deseja verificar: "))

    if codigo in lotes:
        print("Lote encontrado!")
    else:
        print("Lote não encontrado!")


def maior_menor(lotes):
    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")
    else:
        maior = lotes[0]
        menor = lotes[0]

        for i in range(len(lotes)):
            if lotes[i] > maior:
                maior = lotes[i]

            if lotes[i] < menor:
                menor = lotes[i]

        print(f"Maior código: {maior}")
        print(f"Menor código: {menor}")


def menu():
    lotes = []
    opcao = 0

    while opcao != 8:
        print("\nMENU DE GERENCIAMENTO DE LOTES")
        print("1 - Inserir lote")
        print("2 - Listar lotes")
        print("3 - Retirar um lote")
        print("4 - Limpar todos os lotes")
        print("5 - Contar lotes maiores que X")
        print("6 - Verificar se um código está presente")
        print("7 - Encontrar maior e menor código")
        print("8 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            inserir_lote(lotes)
        elif opcao == 2:
            listar_lotes(lotes)
        elif opcao == 3:
            retirar_lote(lotes)
        elif opcao == 4:
            limpar_lotes(lotes)
        elif opcao == 5:
            contar_maior_que_x(lotes)
        elif opcao == 6:
            verificar_lote(lotes)
        elif opcao == 7:
            maior_menor(lotes)
        elif opcao == 8:
            print("Saindo do sistema...")
        else:
            print("Opção inválida!")


menu()