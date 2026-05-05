ing = 100
op = 0

while op != 4:
    print("\n1 vender")
    print("2 adicionar")
    print("3 mostrar")
    print("4 sair")

    op = int(input("op: "))

    if op == 1:
        if ing > 0:
            ing = ing - 1
            print("vendido")
        else:
            print("lotado")

    if op == 2:
        x = int(input("quantos ingressos: "))
        ing = ing + x

    if op == 3:
        print("disponiveis:", ing)

    if op == 4:
        print("fim")