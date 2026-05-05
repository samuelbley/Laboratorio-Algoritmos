while True:
   print("Código","Destino","Taxa")
   print("1"," "*4,"Berlim"," 5%")
   print("2"," "*4,"Lisboa"," 7%")
   print("3"," "*4,"Paris"," 10%")

   valBaseC = float(input("Valor base da carga: "))

   if valBaseC<=1000:
      print("Esse valor é muito baixo, deve ser maior que: R$ 1000,00!")
      esc = str(input("Quer calcular novamente? ")).strip().lower()
      if esc in ["s","sim"]:
         continue
      else:
         break

   destino = int(input("Código do destino: "))

   if destino not in [1,2,3]:
      print("Código inválido, tente novamente!")
      continue
   
   if destino == 1:
      taxa = valBaseC*0.05
      valfinal = valBaseC + taxa
      print("Valor total da carga: ",valfinal)
   
   if destino == 2:
      taxa = valBaseC * 0.07
      valfinal = valBaseC + taxa
      print("Valor total da carga: ",valfinal)
   
   if destino == 3:
      taxa = valBaseC*0.1
      valfinal = valBaseC + taxa
      print("Valor total da carga: ",valfinal)
      if valfinal<=10000:
         print("Nós não realizaremos a carga a Paris pois o valor é inferior a R$ 10000,00!")

   esc = str(input("Quer calcular novamente? ")).strip().lower()
   
   if esc in ["s","sim"]:
      continue
   else:
      break
              

