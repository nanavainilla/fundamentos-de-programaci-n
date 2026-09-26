import time
import os
import pdb  #modulo estaandar para depuracion tecnica 

# CREACION DE LOS ARCHIVOS 

def crear_archivos_iniciales():
    """ crea los archivos de texto requeridos por el sistema si no existen previamente,
    organizando el catalogo de Disney+ por año, estilo, historial y reportes.
    """
    archivos = {
        "peliculas_por_ano.txt": (
            "==================================================\n"
            "        CATALOGO DISNEY+ POR AÑO DE ESTRENO       \n"
            "==================================================\n\n"
            "[ DECADA 1930 - 1950 ]\n"
            "- Blancanieves y los siete enanos (1937)\n"
            "- Pinocho (1940)\n"
            "- Cenicienta (1950)\n\n"
            "[ DECADA 1990 ]\n"
            "- El Rey León (1994)\n"
            "- Toy Story (1995)\n"
            "- Mulan (1998)\n\n"
            "[ DECADA 2000 - 2010 ]\n"
            "- Buscando a Nemo (2003)\n"
            "- Los Increíbles (2004)\n"
            "- Up: Una aventura de altura (2009)\n\n"
            "[ DECADA 2020 - ACTUALIDAD ]\n"
            "- Soul (2020)\n"
            "- Red (2022)\n"
            "- Intensamente 2 (2024)\n"
        ),
        "peliculas_por_estilo.txt": (
            "==================================================\n"
            "       CATALOGO DISNEY+ POR ESTILO Y GENERO      \n"
            "==================================================\n\n"
            "[ ANIMACION CLASICA 2D ]\n"
            "- Hércules\n"
            "- La Sirenita\n"
            "- Tarzán\n\n"
            "[ ANIMACION 3D / PIXAR ]\n"
            "- WALL-E\n"
            "- Coco\n"
            "- Elemental\n\n"
            "[ LIVE-ACTION ]\n"
            "- Piratas del Caribe: La maldición del Perla Negra\n"
            "- Alicia en el país de las maravillas\n"
            "- Juego de Gemelas\n\n"
            "[ Universo Marvel ]\n"
            "- Avengers: Endgame\n"
            "- Spider-Man: No Way Home\n\n"
            "[ Saga Star Wars ]\n"
            "- Star Wars: Una nueva esperanza\n"
            "- The Mandalorian\n"
        ),
        "historial_vistos.txt": (
            "==================================================\n"
            "      HISTORIAL DE REGISTROS DE VISUALIZACION     \n"
            "==================================================\n\n"
            "Fecha: 10/09/2026 | Usuario: U-101 | Género: Animación 3D | Minutos vistos: 120.0\n"
            "Fecha: 15/09/2026 | Usuario: U-102 | Género: Marvel | Minutos vistos: 180.0\n"
        ),
        "reporte_recomendaciones.txt": (
            "==================================================\n"
            "       REPORTE GENERAL DE RECOMENDACIONES         \n"
            "==================================================\n\n"
        )
    }

    for nombre_archivo, contenido in archivos.items():
        if not os.path.exists(nombre_archivo):
            try:
                with open(nombre_archivo, "w", encoding="utf-8") as f:
                    f.write(contenido)
            except IOError as e:
                print(f"[-] ERRORRR al inicializar el archivo '{nombre_archivo}': {e}")


# ==========================================
# REQUERIMIENTO 3: Pantalla de Carga
# ==========================================
def pantalla_de_carga():
    """
    Genera una pausa interactiva de carga del sistema (máximo 5 segundos),
    mostrando un aviso dinámico en consola antes de dar paso a la pantalla principal.
    """
    print("\n[+] INICIANDO EL SISTEMA DE RECOMENDACION DE DISNEY+...")
    for i in range(1, 6):
        print(f"cargando modulos, bases de datos y catalogos... {i * 20}%")
        time.sleep(1)  # Pausa total de 5 segundos
    print("[+] ¡CARGA COMPLETADA CON EXITO!\n")


# INICIO Y EJECUCION DEL PROGRAMA

# inicializar los archivos del sistema 
crear_archivos_iniciales()

# identificar al usuario 
nickname = input("Ingrese su nombre o nickname de usuario: ").strip()

# bienvenida dinamica 
mensaje_bienvenida = "*** BIENVENIDO/A AL SISTEMA DE RECOMENDACION DE DISNEY+, " + nickname.upper() + " ***"
print("\n" + "=" * len(mensaje_bienvenida))
print(mensaje_bienvenida)
print("=" * len(mensaje_bienvenida) + "\n")

# ejecucion de la pantalla de carga 
pantalla_de_carga()

# captura de fecha estructurada en upla
while True:
    try:
        fecha_input = input("ingrese la fecha de operacion (día/mes/año): ").strip()
        partes_fecha = fecha_input.split('/')
        if len(partes_fecha) == 3 and all(p.isdigit() for p in partes_fecha):
            dia, mes, anio = partes_fecha
            # Se almacena estrictamente en una tupla bajo la sintaxis requerida
            Fecha = (dia.zfill(2), mes.zfill(2), anio)
            print(f"[+] fecha registrada en tupla correctamente: fecha = {Fecha}\n")
            break
        else:
            print("[-] formato incorrecto. debe ingresar dia/mes/año numerico (ej. 25/09/2026).")
    except Exception as e:
        print(f"[-] ERRORRRR en la entrada de datos: {e}")

# menu como Matriz
# las opciones del menu ajustadas estrictamente a tus indicaciones
matriz_menu = [
    ["1", "empezar la encuesta de recomendacion"],
    ["2", "ingresar otro usuario"],
    ["3", "no deseo hacer la encuesta"],
    ["4", "salir del programa"]
]

# ciclo principal 'while' para el control del menu
while True:
    print("\n" + "=" * 55)
    print("           MENU PRINCIPAL DE OPCIONES - DISNEY+          ")
    print("=" * 55)
    
    # Despliegue visual del menú en representación de matriz
    for fila in matriz_menu:
        print(f"  [ opcion {fila[0]} ]  -->  {fila[1]}")
    print("=" * 55)

    # control de inactividad del usuario
    # ciclo 'for' para simular/medir el tiempo limite de inactividad de 10 min

    print("\n(*) tienes hasta 10 minutos de inactividad permitidos")
    for minuto in range(1, 11):
        pass

    opcion = input("\nseleccione el numero de la opcion deseada (1-4): ").strip()


    # EVALUAR RECOMENDACION
    
    if opcion == "1":
        print("\n--- EVALUAR RECOMENDACION DE CONTENIDO ---")
        id_del_usuario = input("ingrese el ID de usuario a evaluar: ").strip()

        # control de excepciones try-except
        try:
            
            afinidad = float(input("ingrese la afinidad al genero de la pelicula (0-100): "))
            minutos_vistos = float(input("ingrese los minutos vistos en el genero: "))
        except ValueError:
            print("[-] erorrrrr: debe ingresar valores numericos validos para afinidad y minutos")
            continue

        print("\n--- preferencias especificas del contenido ---")
        actor = input("al usuario le gusta el actor/actriz principal? (s/n): ").strip().lower()
        director = input("al usuario le gusta el director? (s/n): ").strip().lower()
        estilo = input("el estilo o epoca (ej. animado, live-action, 90s) coincide? (s/n): ").strip().lower()
        año = input("a el usuario le interesan las películas de ese año? (s/n): ").strip().lower()

        # ponderacion del calculo
        preferencia = 0.60
        tiempo_consumido = 0.40

        puntaje_final = (afinidad * preferencia) + (minutos_vistos * tiempo_consumido)

        print(f"\n[+] puntaje final calculado: {puntaje_final:.2f}")

        # evaluacion con condicionales
        if puntaje_final >= 70:
            dictamen = "altamente recomendado"
        elif puntaje_final >= 40:
            dictamen = "recomendacion moderada"
        else:
            dictamen = "no recomendado"

        print(f"[+] resultado: {dictamen}")

        # consulta rapida de los archivos creados
        print("\n[+] consultando catalogos recomendados de Disney+ (lectura de archivos)...")
        try:
            with open("peliculas_por_estilo.txt", "r", encoding="utf-8") as file_estilo:
                print("\n" + file_estilo.read()[:300] + "\n... [catalogo recortado por vista previa]")
        except FileNotFoundError:
            print("[-] el archivo de catalogo por estilo no fue encontrado.")

        #tupla fecha
        try:
            fecha_formateada = f"{Fecha[0]}/{Fecha[1]}/{Fecha[2]}"
            registro = f"fecha: {fecha_formateada} | ID usuario: {id_del_usuario} | puntaje: {puntaje_final:.2f} | dictamen: {dictamen}\n"
            
            with open("reporte_recomendaciones.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(registro)
            print("[+] registro guardado automáticamente en 'reporte_recomendaciones.txt' con la tupla fecha.")
        except IOError as e:
            print(f"[-] errorrr al intentar escribir en el archivo de reporte: {e}")

    # ----------------------------------------------------
    # INGRESAR OTRO USUARIO
    # ----------------------------------------------------
    elif opcion == "2":
        print("\n--- INGRESAR OTRO USUARIO ---")
        nuevo_nickname = input("ingrese el nuevo nombre o nickname de usuario: ").strip()
        if nuevo_nickname:
            nickname = nuevo_nickname
            mensaje_bienvenida = "*** NAVEGANDO COMO: " + nickname.upper() + " ***"
            print("\n" + "=" * len(mensaje_bienvenida))
            print(mensaje_bienvenida)
            print("=" * len(mensaje_bienvenida))
            
            # registro en historial_vistos con la tupla fecha
            try:
                with open("historial_vistos.txt", "a", encoding="utf-8") as h_file:
                    h_file.write(f"fecha: {Fecha[0]}/{Fecha[1]}/{Fecha[2]} | nuevo usuario ingresado: {nickname}\n")
                print(f"[+] cambio de usuario registrado en 'historial_vistos.txt'.")
            except Exception as e:
                print(f"[-] errorrr al guardar nuevo usuario: {e}")

    # ----------------------------------------------------
    # NO DESEO HACER LA ENCUESTA
    # ----------------------------------------------------
    elif opcion == "3":
        print("\n--- ENCUESTA OMITIDA ---")
        print("entendido, se omitira la evaluacion de recomendacion por el momento")
        
        # Modo opcional de depuración técnica (Requerimiento 9)
        print("\n[!] ejecutando verificacion de sistema / PDB Debugging opcional...")
        print("instruccion PDB: escriba 'c' y presione enter para continuar.")
        pdb.set_trace()

    # ----------------------------------------------------
    # SALIR DEL PROGRAMA
    # ----------------------------------------------------
    elif opcion == "4":
        print(f"\n¡gracias por utilizar el sistema de recomendacion de Disney+, {nickname}!")
        break

    else:
        print("\n[-] opcion no valida, favor de seleccionar una opcion de la matriz (1-4).")

    # pregunta de continuidad para el ciclo while
    print("\n" + "-" * 55)
    respuesta = input("desea continuar en el menu principal? (escriba 'si' para continuar o 'no' para salir): ").strip().lower()
    if respuesta == "no":
        print(f"\ncerrando sesion del usuario '{nickname}'... ¡hasta pronto!")
        break
    elif respuesta != "si":
        print("\n[!] respuesta no valida, regresando al menu principal")