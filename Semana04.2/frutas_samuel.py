# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                               Até 5 Kg                 Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre
# este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo 
# cliente.

print(" " * 17 + "Tabela de valores:")
print(" " * 10 + "Até 5 Kg" + " " * 15 + "Acima de 5 Kg")
print("-" * 55)

print(f"{'Morango':<15} R$ 2,50 por Kg     R$ 2,20 por Kg")
print(f"{'Maçã':<15} R$ 1,80 por Kg     R$ 1,50 por Kg")

morango = float(input("Kg de morango: "))
maca = float(input("Kg de maçã: "))

if morango <= 5:
    precomorango = morango * 2.50
else:
    precomorango = morango * 2.20

if maca <= 5:
    precomaca = maca * 1.80
else:
    precomaca = maca * 1.50

total = precomorango + precomaca
pesototal = morango + maca

if pesototal > 8 or total > 25:
    total = total * 0.9

print(f"Peso total: Kg {pesototal:.2f}")
print(f"Valor a pagar: R$ {total:.2f}")