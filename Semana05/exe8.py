caixa = float(input("dinheiro em caixa: "))
op = 0

while op != 4:
    print("\n1 venda")
    print("2 retirar")
    print("3 ver caixa")
    print("4 sair")

    op = int(input("op: "))

    if op == 1:
        v = float(input("valor venda: "))
        caixa = caixa + v

    if op == 2:
        r = float(input("retirar: "))
        if r <= caixa:
            caixa = caixa - r
        else:
            print("sem dinheiro")

    if op == 3:
        print("caixa:", caixa)

    if op == 4:
        print("fim")