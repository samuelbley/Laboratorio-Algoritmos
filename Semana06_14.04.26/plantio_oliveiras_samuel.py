# 3 Faça um programa que receba o número total 
# de oliveiras para serem plantadas e o número 
# de fileiras disponíveis no campo experimental 
# da faculdade. O programa deve calcular quantas 
# oliveiras ficarão em cada fileira e se haverá 
# sobra de mudas, mostre a quantidade de sobras.

totalOli = int(input("Número de mudas: "))
totalFil = int(input("Número de fileiras: "))
if totalOli % totalFil == 0:
    porfileira = totalOli//totalFil
    print("Mudas por fileiras: ", porfileira)
    print("Não haverá sobras!")
else:
    porfileira = totalOli//totalFil
    resto = totalOli%totalFil
    print("Mudas por fileiras: ", porfileira)
    if resto==1:
        print(f"Sobras: {resto} muda")
    else:
        print(f"Sobras: {resto} mudas")


