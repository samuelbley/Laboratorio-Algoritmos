#5 - Uma determinada loja de roupas dá 18% de desconto no valor de 
#fábrica de cada peça para ser vendida. Faça um algoritmo em Python que leia o preço de venda de uma 
#peça e apresenta o valor final.

val_fabrica = float(input("Qual é o valor de fábrica da peça de roupa?"))
desconto = (val_fabrica*18)/100 
val_final = val_fabrica - desconto
print("O valor final de peça de roupa é",val_final,"reais")