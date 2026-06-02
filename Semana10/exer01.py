# Faça um algoritmo que preencha um vetor de 8 elementos inteiros. 
# Mostre os valores do vetor e informe:
# Quantos números são maior que 30
# Somar estes números. 
# Somar todos os números.

vetor = []

for i in range(8):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

print("Valores do vetor:", vetor)

quantidade = 0
soma_maiores = 0
soma_total = 0

for numero in vetor:
    soma_total += numero

    if numero > 30:
        quantidade += 1
        soma_maiores += numero

print("Quantidade maiores que 30:", quantidade)
print("Soma dos maiores que 30:", soma_maiores)
print("Soma de todos os números:", soma_total)










