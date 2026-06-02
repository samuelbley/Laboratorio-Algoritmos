# Faça um algoritmo que leia 10 valores distintos e 
# insira em um vetor A. Posteriormente crie um vetor 
# B de 10 posições e insira os valores do vetor 
# A na ordem contrária que foram inseridos.

vetorA = []
for i in range(1,11):
    numVetor = int(input(f"Digite o {i}º valor: "))
    vetorA.append(numVetor)

vetorB = []
for i in range(len(vetorA)-1, -1, -1):
    vetorB.append(vetorA[i])

print(vetorB)