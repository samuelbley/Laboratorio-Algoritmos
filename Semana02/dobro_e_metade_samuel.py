#2 - Crie um algoritmo para exibir o dobro e a metade de um número.
# Utilize a função input.

num = float(input("Qual é o número que você deseja descobrir o dobro e a metade?"))

if num == 0:
    print("Não existe metade ou dobro de 0.")
else:
    print("Dobro: ", num * 2)
    print("Metade: ", num / 2)
