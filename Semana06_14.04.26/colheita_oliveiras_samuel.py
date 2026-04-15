# 1 Faça um programa que peça ao usuário para 
# informar a quantidade de oliveiras colhidas por 
# dia durante 7 dias. Ao final, 
# o programa deve mostrar:
# O total de oliveiras colhidas na semana.
# O dia com maior colheita.
# O dia com menor colheita.

valortotal = 0

for dia in range(1, 8):
    valor = float(input(f"Dia {dia}: "))
    valortotal += valor

    if dia == 1:
        maior = menor = valor
        dia_maior = dia
        dia_menor = dia
    else:
        if valor > maior:
            maior = valor
            dia_maior = dia

        if valor < menor:
            menor = valor
            dia_menor = dia

print("Total da semana:", valortotal)
print(f"Maior colheita: Dia {dia_maior} ({maior})")
print(f"Menor colheita: Dia {dia_menor} ({menor})")