# Faça um programa que converta da notação de 24 horas 
# para a notação de 12 horas. Por exemplo, o programa deve 
# converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e 
# uma para a saída. 
# O sistema deve receber um valor de hora entre 0 e 23 e de minutos entre 0 e 59.

def converterhora(hora, minuto):

    if hora == 0:
        hora12 = 12
        periodo = "A.M."

    elif hora < 12:
        hora12 = hora
        periodo = "A.M."

    elif hora == 12:
        hora12 = 12
        periodo = "P.M."

    else:
        hora12 = hora - 12
        periodo = "P.M."

    return hora12, minuto, periodo


def mostrarhora(hora12, minuto, periodo):
    print(f"Horário: {hora12}:{minuto:02d} {periodo}")


def main():
    hora = int(input("Digite a hora (0 a 23): "))
    minuto = int(input("Digite os minutos (0 a 59): "))

    hora12, minuto, periodo = converterhora(hora, minuto)

    mostrarhora(hora12, minuto, periodo)


main()