# Faça um algoritmo que leia 10 números inteiros e ao final apresente:
# Quantidade de números pares digitados
# Quantidade de números ímpares digitados
# Quantidade de zeros digitados
contagemO = 0
contagemPar = 0
contagemImpar = 0

for i in range(1,11):
    nume = int(input(f"Digte o {i}º número: "))
    if nume == 0:
        contagemO+=1
    elif nume % 2 == 0:
        contagemPar+=1
    else:
        contagemImpar+=1

print(f"\nTotal de zeros digitados: {contagemO}")
print(f"Total de números pares digitados: {contagemPar}")
print(f"Total de números ímpares digitados:{contagemImpar}")

    