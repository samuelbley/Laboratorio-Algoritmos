# Um engenheiro quer verificar se três forças podem manter um corpo em equilíbrio.
# Faça um programa que leia três valores correspondentes às forças.
# O sistema deve verificar se elas obedecem à condição de equilíbrio 
# (a soma de duas deve ser maior que a terceira).
# Caso positivo, classifique o equilíbrio como:
# Simétrico → três forças iguais
# Parcialmente simétrico → duas forças iguais
# Assimétrico → três forças diferentes
# Caso contrário, informe que não há equilíbrio.

f1 = float(input("Primeira força: "))
f2 = float(input("Segunda força: "))
f3 = float(input("Terceira força: "))

if (f1+f2)>f3 and (f1+f3)>f2 and (f2+f3)>f1:
    print("\nAs forças obedecem a condição de equilíbrio pois a soma de duas forças é maior que a terceira!")
    if f1==f2==f3:
        print("\nSimétrico, 3 forças iguais!")
    elif f1==f2 or f1==f3 or f2==f3:
        print("\nParcialmente simétrico, duas forças iguais!")
    else:
        print("\nAssimétrico!")
else:
    print("Não há equilíbrio! Pois a soma de duas forças não é maior que a terceira.")