# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre 
# vendas expressa em porcentagem e custo, que é o 
# custo de um item antes do imposto. A função “altera” 
# o valor de custo para incluir o imposto sobre vendas.

def lerdados():
    taxaImposto = float(input("Digite a taxa de imposto (%): "))
    custo = float(input("Digite o custo do produto: "))

    return taxaImposto, custo


def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo = custo + imposto

    return custo


def mostrarresultado(custofinal):
    print(f"Valor com imposto: R$ {custofinal:.2f}")


def main():
    taxaImposto, custo = lerdados()
    custofinal = somaImposto(taxaImposto, custo)
    mostrarresultado(custofinal)

main()