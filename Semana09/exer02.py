# Crie um programa que calcule e exiba na tela a média 
# aritmética de um conjunto de 10 números lidos do 
# usuário utilizando o laço de repetição for.
total = 0
for nume in range(1,11):
    numeros = int(input(f"Digite o {nume}º número: "))
    total = total + numeros
print("Média dos números digitados: ", total/10)