# Leia um array com 8 valores de produção de azeitonas em kg. 
# Calcule a média e exiba quais produções ficaram acima da média.

def lerproducao():
    producao = []

    for i in range(1, 9):
        prod = float(input(f"Digite o valor da {i}ª produção (Kg): "))
        producao.append(prod)

    return producao


def calcularmedia(producao):
    soma = sum(producao)
    media = soma / len(producao)

    return media


def acimamedia(producao, media):
    print(f"Média: {media:.2f} Kg")
    print("Produções acima da média:")

    for valor in producao:
        if valor > media:
            print(f"{valor} Kg")


def main():
    producao = lerproducao()
    media = calcularmedia(producao)
    acimamedia(producao, media)

main()