soma = 0
novo = 999
velho = 0
atac10k = 0
atac = 0
defe = 0

for i in range(10):
    idade = int(input("idade: "))
    pos = input("posicao (A/D): ")
    sal = float(input("salario: "))

    soma = soma + sal

    if idade < novo:
        novo = idade

    if idade > velho:
        velho = idade

    if pos == "A":
        atac = atac + 1
        if sal <= 10000:
            atac10k = atac10k + 1
    else:
        defe = defe + 1

media = soma / 10

print("media salario:", media)
print("mais novo:", novo)
print("mais velho:", velho)
print("atacantes ate 10k:", atac10k)
print("atacantes:", atac)
print("defensores:", defe)