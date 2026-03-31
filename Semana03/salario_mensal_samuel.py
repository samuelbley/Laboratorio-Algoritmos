#Faça um algoritmo para calcular o salário mensal de um funcionário. Sabe-se que o funcionário recebe 
#R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final. 
#Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o 
#resultado da multiplicação.

hrs = int(input("Qual foi o total de horas que você trabalhou esse mês?"))
salario = hrs * 35
if  salario < 1000:
    salario = salario + 300
    print("Seu salário foi inferior a 1000 reais, portanto você recebeu um adicional de 300 reais!")
    print("Com o adicional seu salário ficou igual a:", salario,"reais.")
else:
    print("Seu salário é de", salario, "reais!")



