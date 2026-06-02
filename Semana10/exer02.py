# Faça um algoritmo que leia 10 valores distintos
# e insira em um vetor. Ao final apresente quantos
# e quais valores digitados são maiores que 100.

vetor = []
for i in range(1,11):
    num = int(input(f"Digite o {i}º Número: "))
    vetor.append(num)
maiorescem = []
maiorCem=0
for num in vetor:
    if num > 100:
        maiorCem+=1
        maiorescem.append(num)
print("\nVetor: ",vetor)
print("Número de valores maiores que cem: ",maiorCem)
print("Maiores que cem: ",maiorescem)
