# Faça um algoritmo que leia 10 valores distintos e 
# insira em um vetor. Ao final apresente somente os 
# valores pares e suas respectivas posições

vetor = []
for i in range(1,11):
    numVetor = int(input(f"Digite o {i}º valor: "))
    vetor.append(numVetor)

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print("Valor:", vetor[i], "Posição:", i) 