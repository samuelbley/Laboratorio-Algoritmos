# Utilizando a estrutura de repetição for, faça um programa 
# em python que receba 10 números e conte quantos deles estão 
# no intervalo [10,20] e quantos deles estão fora do intervalo, 
# escrevendo estas informações.

numentre = 0
numfora = 0 
for receber in range(1,11):
    num = int(input(f"Digite o {receber}º número: "))
    if num >= 10 and num <= 20:
        numentre += 1
    elif num < 10 or num > 20:
        numfora += 1
print("Quantidade de números digitados entre 10 e 20: ", numentre)
print("Quantidade de números digitados fora do intervalo [10,20]: ", numfora)







