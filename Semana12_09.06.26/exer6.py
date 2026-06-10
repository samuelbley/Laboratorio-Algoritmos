# Soma de fazendas. Crie dois arrays do mesmo tamanho 
# com produções inteiras (kg) de Fazenda A e Fazenda B. 
# Gere um terceiro array com a soma elemento a elemento 
# (produção total por posição/lote).

def lerfazendaA():
    print("\n"," "*12,"Fazenda A!")
    vetorfazendaA=[]
    for producoes in range(1,4):
        prod = int(input(f"Digite a {producoes}ª producao da fazenda A: (Kg): "))
        vetorfazendaA.append(prod)

    return vetorfazendaA

def lerfazendaB():
    print("\n"," "*12,"Fazenda B!")
    vetorfazendaB=[]
    for producoes in range(1,4):
        prod = int(input(f"Digite a {producoes}ª producao da fazenda B (Kg): "))
        vetorfazendaB.append(prod)
    
    return vetorfazendaB

def somavetores(vetorfazendaA, vetorfazendaB):
    fazendasoma=[]
    soma = 0
    print("\n")
    for i in range(0,3):
        soma = vetorfazendaA[i]+vetorfazendaB[i]
        fazendasoma.append(soma)
        print(f"Lote {i+1} total: {fazendasoma[i]}")

    return fazendasoma

def main():
    vetorfazendaA = lerfazendaA()
    vetorfazendaB = lerfazendaB()
    fazendasoma = somavetores(vetorfazendaA, vetorfazendaB)

main()