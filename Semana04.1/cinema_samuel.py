# Um cinema está automatizando a venda de ingressos.
# O sistema deve ler o valor base do ingresso e a opção escolhida pelo cliente:
# Ingresso normal (valor cheio)
# Estudante (50% de desconto)
# Criança até 12 anos (paga 40% do valor)
# Idoso (paga 60% do valor)
# O programa deve calcular e mostrar o valor a ser pago.

ingresso = float(input("OLÁ, qual é o valor do ingresso? "))
print("\nTipos de ingressos:" \
"\n1- Ingresso normal (valor cheio)" \
"\n2- Estudante (50% de desconto)" \
"\n3- Criança até 12 anos (60% de desconto)" \
"\n4- Idoso (40% de desconto)")

tipo = int(input("Digite o tipo de ingresso: "))

d50 = (50*ingresso)/100 
d60 = (60*ingresso)/100
d40 = (40*ingresso)/100

if tipo == 1:
    final = ingresso
    print(f"\nVocê pagará R$ {final:.2f}!")
elif tipo == 2:
    final = ingresso - d50
    print(f"\nVocê pagará R$ {final:.2f}!")
elif tipo == 3:
    final = ingresso - d60
    print(f"\nVocê pagará R$ {final:.2f}!")
elif tipo == 4:
    final = ingresso - d40
    print(f"\nVocê pagará R$ {final:.2f}!")


    
