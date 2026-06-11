# Faça um algoritmo que leia cinco notas e faça a média das notas, 
# após isso informe a situação do aluno: 
# >= 7 			Aprovado 
# 4 <= e < 7 	Recuperação 
# < 4 			Reprovado 
# Utilize três funções para apresentar a situação do aluno.

# Faça um algoritmo que leia cinco notas e faça a média.
# Após isso informe a situação do aluno.

def lernotas():
    notas = []

    for i in range(1, 6):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)

    return notas


def situacao(notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        resultado = "Aprovado"
    elif media >= 4:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"

    return media, resultado


def mostrarresultado(media, resultado):
    print(f"Média: {media:.2f}")
    print(f"Situação: {resultado}")


def main():
    notas = lernotas()
    media, resultado = situacao(notas)
    mostrarresultado(media, resultado)

main()