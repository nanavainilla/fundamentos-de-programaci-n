import pdb
precio = 45
descuento = 0.12

#incorrecto, por que no debe de ser 12, sino .12, ya que es porcentaje 
#total = precio - descuento 
#print (f"total: ${total: .2f}") # resultado = 33.00 MAL

#corregido 
total = precio * 0.12
pdb.set_trace()
descuento = precio - total
print ("total a pagar: $", descuento) 