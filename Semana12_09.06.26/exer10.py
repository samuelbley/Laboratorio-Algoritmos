# Verificar lote na lista de inspeção. Crie um array 
# com 5 códigos de lote (inteiros). Depois, peça um 
# código e verifique se ele está presente no array 
# (informar “encontrado”/“não encontrado”).

def criacaolote():
    lote=[10,20,30,40,50]
    return lote

def verificacaolote(lote):
    while True:
        numerolote = int(input("\nDigite o número do lote: "))
        if numerolote in lote:
            print(" "*10,"Lote encontrado!")
            break
        else:
            print(" "*10,"Lote não encontrado!")
            continue

def main():
    lote = criacaolote()
    verificacaolote(lote)

main()
