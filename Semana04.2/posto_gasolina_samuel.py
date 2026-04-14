# Um posto de gasolina deseja calcular descontos para seus clientes:
# Se o cliente abastecer 20 litros ou mais e o valor total for maior 
# que R$ 100,00, ele recebe 10% de desconto.
# Caso abasteça pelo menos 20 litros mas o valor total seja menor 
# ou igual a R$ 100,00, o desconto é de 5%.
# Caso contrário, não há desconto.
# O programa deve ler a quantidade de litros e o valor total, e informar 
# o desconto aplicado e o valor final.

litros = float(input("\nQuantos litros de gasolina você deseja abastecer? "))
valorG = float(input("Qual é valor do litro da gasolina? "))
valorTotal = litros * valorG
d10 = 0.1*valorTotal 
d5 = 0.05*valorTotal

# ABASTECER 20 LITROS OU MAIS E O VALOR MAIOR QUE 100 - 10%
if litros >= 20 and valorTotal > 100:
    valorF = valorTotal-d10
    print(f"Litros: {litros:.2f}")
    print(f"Valor Total: R$ {valorTotal:.2f}")
    print(f"Desconto: R$ {d10:.2f}")
    print(f"Valor Final: R$ {valorF:.2f}")
# ABASTECER 20 LITROS OU MAIS E O VALOR MENOR OU IGUAL A 100 - 5%
elif litros >= 20 and valorTotal <= 100:
    valorF = valorTotal-d5
    print(f"Litros: R$ {litros:.2f}")
    print(f"Valor Total: R$ {valorTotal:.2f}")
    print(f"Desconto: R$ {d5:.2f}")
    print(f"Valor Final: R$ {valorF:.2f}")

else:
    print(f"Litros: R$ {litros:.2f}")
    print(f"Valor Total: R$ {valorTotal:.2f}")
    
