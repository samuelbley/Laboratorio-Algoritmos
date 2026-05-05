cont = 0

for i in range(10):
    idade = int(input("idade: "))

    if idade >= 18:
        cont = cont + 1

print("maiores de idade:", cont)