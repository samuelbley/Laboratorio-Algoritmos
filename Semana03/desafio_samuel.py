nome = str(input("Olá, bem vindo ao sistema da loja! Qual é o seu nome? "))
print(f"\n{nome}, essa é nossa tabela de descontos:\n" \
"\nAcima de 200 reais no dinheiro - 15%\n" \
"Acima de 200 reias no cartão - 5%\n" \
"Abaixo de 200 reais no dinheiro - 10%\n" \
"Abaixo de 200 reais no cartão - sem desconto")
valCompra = float(input("\nValor da compra: "))
print("Forma de pagamento.\n1 - Dinheiro\n2 - Cartão")
formaPag = int(input("\nQual será a forma de pagamento? "))
d15 = (valCompra*15)/(100)
d10 = (valCompra*10)/(100)
d5 = (valCompra*5)/(100)

if valCompra>200 and formaPag == 1:
    valorF = valCompra - d15
    print(f"\nVocê recebeu 15% de desconto, portanto, o valor final é de: {valorF:.2f} reais!")
elif valCompra>200 and formaPag == 2:
    valorF = valCompra - d5
    print(f"\nVocê recebeu 5% de desconto, portanto, o valor final é de: {valorF:.2f} reais!")
elif valCompra<=200 and formaPag == 1:
    valorF = valCompra - d10
    print(f"\nVocê recebeu 10% de desconto, portanto, o valor final é de: {valorF:.2f} reais!")
elif valCompra<=200 and formaPag == 2:
    valorF = valCompra 
    print("Sem desconto!")

print(f"\nCliente: {nome}")
print(f"Valor da Compra: R$ {valCompra}")
print(f"Valor com desconto: R$ {valorF}")

 

 