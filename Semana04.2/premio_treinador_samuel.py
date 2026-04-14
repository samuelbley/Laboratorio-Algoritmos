# Uma equipe de corrida deseja premiar seus treinadores.
# Faça um programa que leia o nome do treinador, seu salário atual e o tempo 
# de serviço na equipe (em anos).
# Se o treinador tem 5 anos ou mais de experiência e recebe até 
# R$ 2.000,00, ele terá um aumento de 10%.
# Nos demais casos, o aumento será de 5%.
# Exiba o nome do treinador, o aumento concedido e o novo salário.

nomeTre = str(input("Qual é o nome do treinador? "))
salarioA = float(input("Qual é o salário atual dele? "))
tempoS = int(input("Quanto tempo de serviço ele tem? "))

if tempoS >= 5 and salarioA <= 2000:
    aumento = 0.1*salarioA
    salariocA = salarioA + aumento
    print("Treinador",nomeTre)
    print(f"Aumento de 10%, ou seja: R$ {aumento:.2f}")
    print(f"O salário dele ficou em R$ {salariocA:.2f}")
else:
    aumento = (0.05)*salarioA
    salariocA = salarioA + aumento
    print("Treinador",nomeTre)
    print(f"Aumento de 5%, ou seja: R$ {aumento:.2f}")
    print(f"O salário dele ficou em R$ {salariocA:.2f}!")