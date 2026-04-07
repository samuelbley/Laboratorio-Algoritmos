# Uma organização de corrida de rua está oferecendo 
# inscrições para a prova de 10 km com três opções de pagamento:
# À vista.
# Em 2 vezes.
# Em 3 vezes.

# O sistema deve ler o valor da inscrição, a opção de
# pagamento escolhida pelo atleta e apresentar o 
# valor de cada parcela (quando houver).

while True:
    print("\nOlá atleta!")
    valorI = float(input("Digite o valor da inscrição para a prova de 10 KM: "))
    print("\nFormas de pagamento:" \
    "\n1- À VISTA" \
    "\n2- 2 VEZES" \
    "\n3- 3 VEZES")
    formaP = int(input("Qual é a forma de pagamento? "))

    if formaP == 1:
        print(f"\nParcela única de R$ {valorI:.2f}")
    elif formaP == 2:
        valor2x = valorI/2
        print("\n2 PARCELAS")
        print(f"Valor de cada parcela: R$ {valor2x:.2f}!")
    elif formaP == 3:
        valor3x = valorI/3
        print("\n3 PARCELAS")
        print(f"Valor de cada parcela: R$ {valor3x:.2f}!")
    
    print("\n1-continuar\n2-encerrar")
    opcao = int(input("CONTINUAR? "))

    if opcao == 1:
        continue
    elif opcao == 2:
        print("\nENCERRANDO...")
        break
