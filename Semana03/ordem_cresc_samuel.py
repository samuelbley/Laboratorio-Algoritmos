#Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.
n1 = int(input("Qual é o primeiro número?"))
n2 = int(input("Qual é o segundo número?"))

if n1==n2:
    print("Os números são iguais!")
elif n1<n2:
    print("Primeiro número: ",n1,"\n","Segundo número: ",n2,sep="")
    print(n1,"\n",n2, sep="")
else:
    print("Primeiro número : ",n1,"\n","Segundo número: ",n2,sep="")
    print(n2,"\n",n1, sep="")