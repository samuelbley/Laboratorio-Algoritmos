# Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre
# seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura):
# Homens: (72.7 ∗ h) − 58
# Mulheres: (62, 1 ∗ h) − 44, 7

sexo = str(input("Olá, qual é o seu sexo? ")).strip().lower()
h = float(input("Qual é a sua altura? "))
pesoH = (72.7*h)-(58)
pesoM = (62.1*h)-(44.7)
if sexo == 'feminino':
    print(f"Seu peso ideal é: {pesoM:.2f} kg!", sep="")
if sexo == 'masculino':
    print(f"Seu peso ideal é: {pesoH:.2f} kg!", sep="")
