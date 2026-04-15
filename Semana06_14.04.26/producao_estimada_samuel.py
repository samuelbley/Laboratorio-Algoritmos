# 5 Cada 100 oliveiras produzem em média 5 
# litros de azeite por ano. Escreva um 
# programa que solicite ao usuário o 
# número total de oliveiras plantadas e 
# calcule a produção anual estimada de azeite.

totalOli = int(input("Total de oliveiras plantadas: "))
if totalOli == 100:
    print("A produção anual estimada é de 5 LITROS!")
elif totalOli > 100:
    producao = totalOli/100
    producaot = producao*5
    print(f"A produção anual estimada é de {producaot:.2f} LITROS!")
else:
    print("A produção anual estimada é menor que 5 LITROS!")
        