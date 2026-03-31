# Peça o valor de uma compra.
# Se o valor for maior que R$100, aplique 10% de desconto.
# Senão, não aplique desconto.

print("Olá, se o valor da compra for acima de 100 reais você ganha 10 porcento de desconto!")
compra = float(input("Qual é o valor da compra? "))
desconto = (compra * 10)/(100)
valFinal = compra - desconto
print(f"O valor final da compra é de {valFinal:.2f} reais", sep="")
