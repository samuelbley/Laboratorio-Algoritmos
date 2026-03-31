# Faça um algoritmo que leia o ano de nascimento de uma pessoa e verifique se
# ela pode ou não votar (desconsidere o mês de nascimento).
nome = str(input("Qual é o seu nome?"))
anoNasc = int(input("Em que ano você nasceu?"))
idade = 2026 - anoNasc
if idade >= 16:
    print("Olá ", nome, ",", " Você pode votar!", sep="")
else:
    print("Olá ", nome, ",", " Você não pode votar!", sep="")
