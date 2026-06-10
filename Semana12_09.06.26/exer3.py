# Últimas colheitas invertidas. Peça 5 valores de produção 
# (kg de azeitona) informados pelo usuário, armazene em um 
# array e imprima na ordem inversa.

def lerproducoes():
    vetorproducao = []
    for i in range(1,6):
        prod = float(input(f"Digite a {i} Producão (Kg): "))
        vetorproducao.append(prod)
    
    return vetorproducao

def inverterproducoes(vetorproducao):
    for i in range(len(vetorproducao)-1, -1, -1):
        print(vetorproducao[i])

    return i

def main():
    vetorproducao = lerproducoes()
    i = inverterproducoes(vetorproducao)

main()
