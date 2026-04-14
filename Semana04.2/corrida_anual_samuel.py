# A cidade está prestes a sediar a Corrida Anual dos Campeões, 
# e os organizadores precisam saber se você está preparado para participar.
# Um programa fará 5 perguntas sobre sua preparação:
# Você treinou regularmente nas últimas semanas?
# Participou de treinos longos (acima de 10 km)?
# Seguiu uma dieta especial para a corrida?
# Já competiu em provas oficiais neste ano?
# Conta com acompanhamento de treinador ou equipe?
# De acordo com suas respostas "Sim" ou "Não", o sistema deve classificá-lo:
# 2 respostas positivas → Você é classificado como Participante 
# Casual (ainda precisa de mais treino).
# 3 ou 4 respostas positivas → Você é classificado como Atleta Competitivo 
# (tem boas chances de se destacar).
# 5 respostas positivas → Você é classificado como Atleta de Elite 
# (pronto para o pódio!).
# Menos de 2 respostas positivas → Você é classificado como Não Preparado 
# (talvez seja melhor assistir da arquibancada este ano).

perguntas = [
    "Você treinou regularmente nas últimas semanas? ",
    "Participou de treinos longos (acima de 10 km)? ",
    "Seguiu uma dieta especial para a corrida? ",
    "Já competiu em provas oficiais neste ano? ",
    "Conta com acompanhamento de treinador ou equipe? "
]

positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta).lower()
    
    if resposta == "sim":
        positivas += 1

if positivas == 5:
    print("\nAtleta de Elite, pronto para o pódio!")
elif positivas == 3 or positivas == 4:
    print("\nAtleta Competitivo, tem boas chances de se destacar!")
elif positivas == 2:
    print("\nParticipante Casual, ainda precisa de mais tempo!")
else:
    print("\nNão Preparado!" \
    " Talvez seja melhor assistir da arquibancada esse ano.")