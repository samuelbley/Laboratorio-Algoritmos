# O mercado QUIOSQUE está com uma promoção, 
# comprando até 12 laranjas, o preço unitário é 
# R$0,40, caso compre mais que 12 o valor cai para 
# R$0,25. Faça um programa que leia o total de laranjas 
# compradas e mostre o valor ao final da execução. Faça 
# uma função que receba o total de laranjas e retorne o 
# valor total da compra.

# Promoção das laranjas

def lerquantidade():
    quantidadelaranjas = int(input("Digite a quantidade de laranjas: "))
    return quantidadelaranjas


def calcularvalor(quantidadelaranjas):
    if quantidadelaranjas <= 12:
        valor = quantidadelaranjas * 0.40
        print(f"Valor total da compra: R$ {valor:.2f}")
    else:
        valor = quantidadelaranjas * 0.25
        print(f"Valor total da compra: R$ {valor:.2f}")

    return valor


def main():
    quantidadelaranjas = lerquantidade()
    valor = calcularvalor(quantidadelaranjas)

main()