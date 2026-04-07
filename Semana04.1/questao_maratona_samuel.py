# Durante uma prova de corrida de rua, os atletas 
# responderam a uma pergunta de conhecimento esportivo.
# A questão era: “Qual é a distância oficial de uma maratona?”
# Alternativas:
# A) 21 km
# B) 42,195 km
# C) 10 km
# D) 5 km
# O sistema deve ler a alternativa assinalada e 
# informar se o atleta acertou ou errou.
# (Resposta correta: letra B)
while True:
    print("\nQual é a distância oficial de uma maratona?\n"
    "\nAlternativas:\n"
    "A) 21 km\n"
    "B) 42,195 km\n"
    "C) 10 km\n"
    "D) 5 km\n")
    alternativa = str(input("RESPOSTA: ")).strip().lower()

    if alternativa == "b":
        print("Resposta correta!")
    else:
        print("Resposta Incorreta!")
    
    opcao = str(input("\nTentar Novamente? ")).strip().lower()

    if opcao in ["sim" , "s"]:
        continue
    else:
        print("\nENCERRANDO...")
        break
