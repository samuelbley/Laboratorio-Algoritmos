nome = input("Nome da transportadora: ")

saldo = float(input("Saldo inicial: "))
while saldo <= 0:
    print("Saldo inválido! Digite um valor positivo.")
    saldo = float(input("Saldo inicial: "))

caminhoes = 1

while True:
    print("\n--- MENU ---")
    print("1 - Registrar entrega realizada")
    print("2 - Adicionar caminhão à frota")
    print("3 - Ver total de caminhões")
    print("4 - Solicitar manutenção")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        saldo += 1200
        print("Entrega registrada! +R$1200")
    
    elif opcao == 2:
        if saldo >= 30000:
            saldo -= 30000
            caminhoes += 1
            print("Caminhão adicionado!")
        else:
            print("Saldo insuficiente!")

    elif opcao == 3:
        print(f"Total de caminhões: {caminhoes}")

    elif opcao == 4:
        if saldo >= 3000:
            saldo -= 3000
            print("Manutenção realizada!")
        else:
            print("Saldo insuficiente!")

    elif opcao == 5:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")

print("\n--- FINAL ---")
print(f"Transportadora: {nome}")
print(f"Saldo final: R${saldo}")
print(f"Total de caminhões: {caminhoes}")