#Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do 
#valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num = float(input("Digite o número que você quer saber o dobro:"))
if num==0:
    print("O número zero não possui dobro!")
elif num>0:
    dobro = num*2
    print("O dobro do número ",num," é ",dobro,"!",sep="")
elif num<0:
    print("O número ",num," é negativo, portanto, ele é inválido!",sep="")
