# Foi realizada uma pesquisa de algumas características físicas da população 
# de um certa região. Foram entrevistadas 15 pessoas e coletados os seguintes dados:  
# a- sexo: M (masculino) e F (feminino)
# b- cor dos olhos: A (azuis), V (verdes) e C (castanhos)
# c- cor dos cabelos: L (loiros), C (castanhos) e P (pretos)
# d- idade
# Deseja-se saber:
# A maior idade do grupo
# A quantidade de indivíduos cuja idade está entre 18 e 35 anos e que 
# tenham olhos verdes e cabelos pretos.
# A porcentagem de pessoas com os olhos azuis, verdes e castanhos
# A porcentagem de Loiros, Castanhos e Pretos.
# A porcentagem de pessoas do sexo masculino e feminino

e18e35verdPreto = 0
OAzul = 0
OVerde = 0
OCast = 0
CLoi = 0
CCast = 0
CPret = 0
SMasc = 0
SFem = 0

for entrevista in range(1,16):
    print(f"\n{entrevista}º entrevistado")
    sexo = str(input("Qual é o seu sexo?(Masculino/Feminino) ")).strip().lower()
    if sexo in ["masculino"]:
        SMasc+=1
    else:
        SFem+=1
    
    CorOl = str(input("Qual é a cor do seus olhos?(Azul/Verde/Castanho) ")).strip().lower()
    if CorOl in ["azul"]:
        OAzul+=1
    elif CorOl in ["verde"]:
        OVerde+=1
    elif CorOl in ["castanho"]:
        OCast+=1
    
    CorCab = str(input("Qual é a cor dos seus cabelos?(Loiro/Castanho/Preto) ")).strip().lower()
    if CorCab in ["loiro"]:
        CLoi+=1
    elif CorCab in ["castanho"]:
        CCast+=1
    elif CorCab in ["preto"]:
        CPret+=1

    idade = int(input("Qual é a sua idade? "))
    if entrevista == 1:
        Midade = idade
    elif Midade > idade:
        Midade=Midade
    elif idade > Midade:
        Midade=idade 
    
    # A quantidade de indivíduos cuja idade está entre 18 e 35 anos 
    # e que tenham olhos verdes e cabelos pretos.
    if idade > 18 and idade < 35 and CorOl in ["verde"] and CorCab in ["preto"]:
        e18e35verdPreto+=1



# A maior idade do grupo
# A quantidade de indivíduos cuja idade está entre 18 e 35 anos e que 
# tenham olhos verdes e cabelos pretos.
# A porcentagem de pessoas com os olhos azuis, verdes e castanhos
# A porcentagem de Loiros, Castanhos e Pretos.
# A porcentagem de pessoas do sexo masculino e feminino

porOAz = (OAzul*100)/15
porOVe = (OVerde*100)/15
porOCa = (OCast*100)/15

porCLo = (CLoi*100)/15
porCCa = (CCast*100)/15
porCPr = (CPret*100)/15

porHo = (SMasc*100)/15
porMu = (SFem*100)/15

print("\nA maior idade do grupo: ", Midade)
print("A quantidade de indivíduos cuja idade está entre 18 e 35 anos e que " \
"tenham olhos verdes e cabelos pretos: ", e18e35verdPreto)

print("A porcentagem de pessoas com olhos azuis: ",porOAz)
print("A porcentagem de pessoas com olhos verdes: ",porOVe)
print("A porcentagem de pessoas com olhos castanhos: ",porOCa)

print("A porcentagem de pessoas com cabelos loiros: ", porCLo)
print("A porcentagem de pessoas com cabelos castanhos: ", porCCa)
print("A porcentagem de pessoas com cabelos pretos: ", porCPr)

print("A porcentagem de pessoas do sexo masculino: ", porHo)
print("A porcentagem de pessoas do sexo feminino: ", porMu)
