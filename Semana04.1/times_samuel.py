# Faça um algoritmo que leia a pontuação de dois times
# em uma partida. Mostre qual time venceu, qual perdeu ou
# se houve empate.

while True:

    time1 = int(input("\nQuantos pontos o primeiro time fez? "))
    time2 = int(input("Quantos pontos o segundo time fez? "))

    if time1 > time2:
        print(f"\nO primeiro time venceu por {time1} a {time2}!")
    elif time2 > time1:
        print(f"\nO segundo time venceu por {time2} a {time1}!")
    elif time1 == time2:
        print("EMPATE!")

    print("\n1-continuar\n2-encerrar")
    opcao = int(input("CONTINUAR? "))

    if opcao == 1:
        continue
    elif opcao == 2:
        print("\nENCERRANDO...")
        break