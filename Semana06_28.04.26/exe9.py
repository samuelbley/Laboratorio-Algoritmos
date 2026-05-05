idade = int(input("idade: "))
while idade < 0 or idade > 150:
    idade = int(input("idade invalida: "))

sal = float(input("salario: "))
while sal <= 0:
    sal = float(input("salario invalido: "))

sexo = input("sexo (f/m): ")
while sexo != "f" and sexo != "m":
    sexo = input("sexo invalido: ")

ec = input("estado civil (s/c/v/d): ")
while ec != "s" and ec != "c" and ec != "v" and ec != "d":
    ec = input("estado civil invalido: ")

print("dados corretos")