# Uma empresa de pesquisa deseja saber qual jornal é mais 
# lido em Santa Maria (A, B ou C). Faça um algoritmo que
# leia a opinião de 20 pessoas, ao final mostre a porcentagem 
# de cada uma das revistas, em ordem crescente.

qtA = 0
qtB = 0
qtC = 0 

for pessoas in range(20):
    jornal = str(input("Qual jornal você lê (A,B ou C)? "))
    if jornal in ['A','a']:
        qtA+=1
    elif jornal in ['B','b']:
        qtB+=1
    elif jornal in ['C','c']:
        qtC+=1

porA = (qtA*100)/20
porB = (qtB*100)/20
porC = (qtC*100)/20 

if porA <= porB and porA <= porC:

    if porB <= porC:
        print("A", porA)
        print("B", porB)
        print("C", porC)
    else:
        print("A", porA)
        print("C", porC)
        print("B", porB)

elif porB <= porA and porB <= porC:

    if porA <= porC:
        print("B", porB)
        print("A", porA)
        print("C", porC)
    else:
        print("B", porB)
        print("C", porC)
        print("A", porA)

else:

    if porA <= porB:
        print("C", porC)
        print("A", porA)
        print("B", porB)
    else:
        print("C", porC)
        print("B", porB)
        print("A", porA)
     







