# Faça um algoritmo que apresente o seguinte menu:
# 1 - Sacar dinheiro
# 2 - Depositar dinheiro
# 3 - Mostrar saldo
# 4 - Sair
# O saldo inicial da conta é 0. O sistema deve ter 4 funções: 
# Mostrar o menu; sacar; depositar; saldo

def menu():
    print("\n1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))
    return opcao


def sacar(saldo):
    valor = float(input("Digite o valor do saque: "))

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor

    return saldo


def depositar(saldo):
    valor = float(input("Digite o valor do depósito: "))
    saldo += valor

    return saldo


def mostrarsaldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0

    while True:
        opcao = menu()

        if opcao == 1:
            saldo = sacar(saldo)

        elif opcao == 2:
            saldo = depositar(saldo)

        elif opcao == 3:
            mostrarsaldo(saldo)

        elif opcao == 4:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


main()