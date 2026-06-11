# Faça um algoritmo que receba um valor 
# e apresente o dobro e o triplo do valor.
# Utilize duas funções para realizar os cálculos

def pedirvalor():
    valor = float(input("Digite um valor: "))
    print("Valor digitado: ", valor)

    return valor

def dobro(valor):
    dobro = valor*2
    print("Dobro: ", dobro)

def triplo(valor):
    triplo = valor*3
    print("Triplo: ", triplo)


def main():
    valor = pedirvalor()
    dobro(valor)
    triplo(valor)

main()