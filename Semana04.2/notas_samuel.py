# Faça um algoritmo que leia as duas notas parciais obtidas por um aluno
# numa disciplina ao longo de um semestre, e calcule a sua média. A
# atribuição de conceitos obedece à tabela abaixo:
#     Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0                      A
#       Entre 7.5 e 9.0                        B
#       Entre 6.0 e 7.5                        C
#       Entre 4.0 e 6.0                        D
#       Entre 4.0 e zero                      E
# O algoritmo deve mostrar as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

while True:
    n1 = float(input("\n1º Nota: "))
    n2 = float(input("2º Nota: "))
    media = (n1 + n2) / 2
    if media >= 9 and media <= 10:
        print(f"\nNota 1: {n1:.1f}")
        print(f"Nota 2: {n2:.1f}")
        print(f"Nota final: {media:.1f}")
        print("Conceito: A")
        print("PARABÉNS, VOCÊ FOI APROVADO!")
    elif media >= 7.5 and media <= 8.9:
        print(f"\nNota 1: {n1:.1f}")
        print(f"Nota 2: {n2:.1f}")
        print(f"Nota final: {media:.1f}")
        print("Conceito: B")
        print("PARABÉNS, VOCÊ FOI APROVADO!")
    elif media >= 6 and media <= 7.4:
        print(f"\nNota 1: {n1:.1f}")
        print(f"Nota 2: {n2:.1f}")
        print(f"Nota final: {media:.1f}")
        print("Conceito: C")
        print("PARABÉNS, VOCÊ FOI APROVADO!")

    elif media >= 4 and media <= 5.9:
        print(f"\nNota 1: {n1:.1f}")
        print(f"Nota 2: {n2:.1f}")
        print(f"Nota final: {media:.1f}")
        print("Conceito: D")
        print("SE DEDIQUE MAIS, VOCÊ FOI REPROVADO!")
    else:
        print(f"\nNota 1: {n1:.1f}")
        print(f"Nota 2: {n2:.1f}")
        print(f"Nota final: {media:.1f}")
        print("Conceito: E")
        print("SE DEDIQUE MAIS, VOCÊ FOI REPROVADO!")

    opcao = str(input("\nQuer calcular novamente? ")).strip().lower()
    if opcao in ["s","sim"]:
        continue
    else:
        print("ENCERRANDO...")
        break
