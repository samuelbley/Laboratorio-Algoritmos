# Escreva um programa que imprima na tela a sequência de Fibonacci 
# até o décimo termo utilizando o laço de repetição for.

n1 = 0
n2 = 1
for i in range(10):
    print(n1)
    soma = n1 + n2
    n1 = n2
    n2 = soma