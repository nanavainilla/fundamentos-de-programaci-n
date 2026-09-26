#ACTIVIDAD SEMANA 1
#TEMA 1-4
#Desarrollar una calculadora que registre el tiempo diario de que una persona dedica a distintas plataformas digitales. 
#El programa debe capturar los datos, procesarlos y mostrar un resumen claro y ordenado de los resultados. 

#- Entrada - Proceso - Salida 

#CODIGO

nombre = input("Escribe tu nombre: ")

redes = float(input("Horas en redes sociales: "))
msj = float(input("Horas en mensajes: "))
series = float(input("Horas viendo series: "))
videos = float(input("Horas viendo videos: "))
gaming = float(input("Horas jugando videojuegos: "))

total = redes + msj + series + videos + gaming

porcentaje = total / 24 * 100

print("Nombre:", nombre)
print("Tiempo total:", total, "horas")
print("Porcentaje del día:", porcentaje, "%")