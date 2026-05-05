distotal = 500
percorrido = 0
ultimoskm = 80
hora = 1

while percorrido < distotal:
    if distotal - percorrido < ultimoskm:
        kmrodado = distotal - percorrido
        percorrido+=kmrodado
        faltam = distotal-percorrido
        print(f"O caminhão percorreu os restantes {kmrodado} km. Faltam {faltam} km.")
    else:
        kmrodado = ultimoskm
        percorrido+=kmrodado
        faltam = distotal-percorrido
        print(f"Hora {hora}: o caminhão percorreu {kmrodado} km. Faltam {faltam} km.")
        hora += 1

print("Entrega concluída com sucesso!")