#EJERCICIO 1

total_cuenta_str = int(input("ingrese el total de la cuenta:"))
porcentaje_propina_str = int(input("ingrese el porcentaje de propina que desea dejar:"))
personas_que_pagarán_str = int(input("ingrese el total de personas que pagarán la cuenta:"))

monto_de_propina = total_cuenta_str * porcentaje_propina_str / 100
total_cuenta_con_propina = total_cuenta_str * (1 + porcentaje_propina_str)/100
monto_por_persona = total_cuenta_con_propina / personas_que_pagarán_str

print("monto_de_propina:", monto_de_propina)
print("total_cuenta_con_propina:", total_cuenta_con_propina)
print("monto_por_persona:", monto_por_persona)

#EJERCICIO 2 
total_de_minutos_str = int(input("ingrese el total de minutos que deseé transformar:"))
días = total_de_minutos_str // 1440
horas = (total_de_minutos_str % 1440) // 60
minutos = total_de_minutos_str % 60

print("días:", días)
print("horas:", horas)
print("minutos:", minutos)


#EJERCICIO 3
parcial_1_str = int(input("ingrese su calificación del parcial 1:"))
parcial_2_str = int(input("ingrese su calificación del parcial 2:"))
parcial_3_str = int(input("ingrese su calificación del parcial 3:"))

parcial_1 = parcial_1_str * 0.3 
parcial_2 = parcial_2_str * 0.3 
parcial_3 = parcial_3_str * 0.4

calificación_final = parcial_1 + parcial_2 + parcial_3

print("calificación_final:", calificación_final)

#EJERCICIO 4
cantidad_peso_mexicano_str = float(input("ingrese la cantidad de pesos mexicanos que deseé convertir:"))
tipo_de_cambio_usa_str = float(input("ingrese el tipo de cambio de pesos mexicanos a dólares:"))
tipo_de_cambio_euro_str = float(input("ingrese el tipo de cambio de pesos mexicanos a euros:"))

DOLARES = cantidad_peso_mexicano_str / tipo_de_cambio_usa_str
EUROS = cantidad_peso_mexicano_str / tipo_de_cambio_euro_str

DOLARES = round(DOLARES, 2)
EUROS = round(EUROS, 2)

print(cantidad_peso_mexicano_str, "pesos mexicanos equivalen a")
print("USA:", DOLARES)
print("EUR:", EUROS)
