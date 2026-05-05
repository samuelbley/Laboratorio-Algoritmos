soma = 0
menos30 = 0
entre = 0

for i in range(7):
    t = float(input("tempo: "))
    soma = soma + t

    if t < 30:
        menos30 = menos30 + 1

    if t >= 30 and t <= 60:
        entre = entre + 1

media = soma / 7
porc = (entre / 7) * 100

print("media:", media)
print("menos de 30:", menos30)
print("entre 30 e 60:", porc, "%")