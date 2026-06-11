# Faça um algoritmo para calcular a média entre duas 
# notas de um aluno. O algoritmo deve conter:
# Uma função que recebe dois valores e retorna a média
# E uma função que recebe a média e apresente se o aluno foi ou não aprovado.

def notas():
    vetornotas=[]
    for i in range(1,3):
        nota = float(input(f"Digite a {i}ª Nota: "))
        vetornotas.append(nota)
    
    return vetornotas

def calcularmedia(vetornotas):
    soma = sum(vetornotas)
    media = soma/len(vetornotas)

    return media

def aprovação(media):
    if media>=7:
        print("Aprovado")
    else:
        print("Reprovado")

def main():
    vetornotas = notas()
    media = calcularmedia(vetornotas)
    aprovação(media)

main()