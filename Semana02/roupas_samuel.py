#1 - Uma determinada loja de roupas acrescenta 30% no valor de fábrica de cada peça para 
# ser vendida. Faça um algoritmo em 
# Python que leia o preço de fábrica de uma peça e apresenta o valor final.

val_fabrica = float(input("Qual é o valor de fábrica?"))
acrescimo = (val_fabrica * 30)/100
val_final = val_fabrica + acrescimo
print("O valor final do produto é ",val_final,"reais!")


