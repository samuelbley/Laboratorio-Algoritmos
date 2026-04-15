# 7 Faça um programa que peça para 15 
# estudantes da faculdade informarem 
# a sua idade. Ao final, calcule a 
# média da turma e classifique:
# Entre 0 e 25 → turma jovem;
# Entre 26 e 60 → turma adulta;
# Acima de 60 → turma idosa.

soma = 0
for estudantes in range(1, 16):
    idade = int(input(f"Idade estudante {estudantes}: "))
    soma = soma + idade

media = soma // 15
print("Média da turma: ",media," anos")
if media < 26: #JOVEM
    print("Turma Jovem!")
if media > 25 and media < 61: #ADULTA
    print("Turma Adulta!")
if media > 60: #IDOSA
    print("Turma Idosa!")