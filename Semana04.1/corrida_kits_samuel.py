# Durante a inscrição, o atleta pode escolher entre 3 kits diferentes.
# Faça um algoritmo que leia a opção escolhida e o valor que o atleta está 
# entregando em R$ e mostre o que ele receberá:
# 1 → Kit Básico: Número de peito + medalha - R$100,00
# 2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00
# 3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00

# Ao final apresente se o valor foi suficiente, caso foi suficiente, apresente a 
# categoria do atleta e o troco (se houver), caso contrário apresente uma mensagem 
# informando a falta do valor.

while True:

    print("\n1 → Kit Básico: Número de peito + medalha - R$100,00")
    print("2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00")
    print("3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00")

    opcao = int(input("\nQual opção você deseja? "))

    if opcao not in [1,2,3]:
        print("Opação inválida!")
        break

    valor = float(input("Digite o valor que você irá entregar: "))

    if opcao == 1:
        if valor == 100:
            print("Você ganhará o Kit Básico (Número de peito + medalha)!")
        elif valor < 100:
            falta = 100 - valor
            print(f"Faltam R$ {falta:.2f}!")
        elif  valor > 100:
            sobra = valor - 100
            print("Você ganhará o Kit Básico (Número de peito + medalha)!")
            print(f"Sobrou: R$ {sobra:.2f}")
    
    elif opcao == 2:
        if valor == 120:
            print("Você ganhará o Kit Plus (Número de peito + medalha + camiseta)!")
        elif valor < 120:
            falta = 120 - valor
            print(f"Faltam: R$ {falta:.2f}!")
        elif valor > 120:
            sobra = valor - 120
            print("Você ganhará o Kit Plus (Número de peito + medalha + camiseta)!")
            print(f"Sobrou: R$ {sobra:.2f}!")

    elif opcao == 3:
        if valor == 150:
            print("Você ganhará o Kit Premium (Número de peito + medalha + camiseta + squeeze + boné)!")
        elif valor < 150:
            falta = 150 - valor
            print(f"Faltam R$ {falta:.2f}!")
        elif valor > 150:
            sobra = valor - 150
            print("Você ganhará o Kit Premium (Número de peito + medalha + camiseta + squeeze + boné)!")
            print(f"Sobrou R$ {sobra:.2f}")

    continuar = str(input("\nDeseja comprar novamente? ")).strip().lower()
    if continuar in ["s","sim"]:
        continue
    else:
        print("\nEncerrando...")
        break

        
        






