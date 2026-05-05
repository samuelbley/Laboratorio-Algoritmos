cont = 0

for i in range(10):
    temp = float(input("temp: "))

    if temp >= 15 and temp <= 25:
        cont = cont + 1

print("entre 15 e 25:", cont)