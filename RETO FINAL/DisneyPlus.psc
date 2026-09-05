Algoritmo DisneyPlus
	preferencia <- 0.60
	tiempo_consumido <- 0.40
	continuar <- 's'
	Mientras continuar='s' Hacer
		Escribir 'ID de usuario:'
		Leer id_usuario
		Escribir 'Afinidad (0-100):'
		Leer afinidad
		Escribir 'Minutos vistos:'
		Leer minutos_vistos
		puntaje <- (afinidad*preferencia)+(minutos_vistos*tiempo_consumido)
		Si puntaje>=70 Entonces
			Escribir 'Puntaje: ', puntaje, ' - Altamente recomendado'
		SiNo
			Si puntaje>=40 Entonces
				Escribir 'Puntaje: ', puntaje, ' - Recomendación moderada'
			SiNo
				Escribir 'Puntaje: ', puntaje, ' - No recomendado'
			FinSi
		FinSi
		Escribir '¿Evaluar otro? (s/n):'
		Leer continuar
	FinMientras
	Escribir '¡Gracias por usar el sistema!'
FinAlgoritmo
