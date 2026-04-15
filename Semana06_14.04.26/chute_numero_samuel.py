# 10 Faça um algoritmo onde uma variável contenha um 
# número de oliveiras definido por você entre 1 e 100. 
# Posteriormente, solicite ao usuário que tente adivinhar 
# esse número. Se o usuário digitar um valor menor, apresente:
# “Há mais oliveiras, tente um número maior”.
# Se digitar um valor maior, apresente:
# “Há menos oliveiras, tente um número menor”.
# Quando acertar, apresente:
# “Parabéns! Você descobriu a quantidade de oliveiras!”.

nOli = 55
chute = int(input("Tente acertar o numero de oliveiras entre 0 e 100!\nDê o seu primeiro chute: "))
if chute == nOli:
    print("Parabéns, Você descobriu a quantidade de oliveiras!")
else:
    if chute<nOli:
        print("Há mais oliveiras, tente um número maior!")
    if chute>nOli:
        print("Há menos oliveiras, tente um número menor!")  
    while (chute != nOli):
        chute = int(input("Tente novamente: "))
        if chute == nOli:
            print("Parabéns, Você descobriu a quantidade de oliveiras!")
        else:
            if chute<nOli:
                print("Há mais oliveiras, tente um número maior!")
            if chute>nOli:
                print("Há menos oliveiras, tente um número menor!")