#8 Suponha que no Recanto Maestro a plantação A 
# de oliveiras tenha 80.000 mudas com crescimento 
# anual de 3% e a plantação B tenha 200.000 mudas 
# com crescimento anual de 1,5%. Faça um programa que 
# calcule e escreva o número de anos necessários para 
# que a plantação A ultrapasse ou iguale a plantação B, 
# mantidas as taxas de crescimento. Ao final apresente 
# em quantos anos isso ocorreu.

plantA = 80000
plantB = 200000
crescA = 0.03
crescB = 0.015
anos = 0

while plantA < plantB:
    plantA += plantA * crescA
    plantB += plantB * crescB
    anos += 1

print(f"Plantação A: {plantA:.2f}")
print(f"Plantação B: {plantB:.2F}")
print(f"Serão necessários {anos} anos.")    
   