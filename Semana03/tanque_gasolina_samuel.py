#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo 
#para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros
#ele conseguiu colocar no tanque.

print("Use '.' ao invés de ','!")
quantoColocar = float(input("Quantos reais de gasolina você quer colocar?"))
preco = float(input("Qual é o preço do litro da gasolina?"))
litros = quantoColocar / preco
if quantoColocar == 0:
    print("Com 0 reais você não consegue colocar nada de gasolina :/")
else:
    print(f"Você consegue colocar {litros:.2f} litros!",sep="")
