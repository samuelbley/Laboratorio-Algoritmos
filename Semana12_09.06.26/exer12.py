# Valor por árvore (kg × preço). Leia dois arrays de 5 elementos:
# kg_colhidos (produção por árvore)
# preco_por_kg (preço do cultivar/qualidade correspondente)
# Crie um terceiro array com a multiplicação elemento a elemento 
# (valor obtido por árvore).

def lerproducaoArv():
    KGporArv = []
    for i in range(1,6):
        kgcolhido = float(input(f"{i}ª Árvore (Kg): "))
        KGporArv.append(kgcolhido)

    return KGporArv

def multiplicarpreco(KGporArv):
    totalxKG = []
    soma = 0
    precoporkg = float(input("\nDigite o preço por kg: "))
    print("\n")
    for i in range(0,5):
        soma = KGporArv[i]*precoporkg
        totalxKG.append(soma)
        print(f"{i+1}ª Árvore: R$ {totalxKG[i]}")
    

def main():
    KGporArv = lerproducaoArv()
    multiplicarpreco(KGporArv)
main()