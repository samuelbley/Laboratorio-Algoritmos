# Faça um algoritmo que peça dois números para o usuário 
# (o primeiro sempre será menor que o segundo), 
# posteriormente apresente somente os números pares no 
# intervalo entre os dois número. 

num1 = int(input("Primeiro número (O 1º deve ser menor que o segundo!): "))
num2 = int(input("Segundo número: "))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)