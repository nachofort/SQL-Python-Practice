#librerias

import random
from openpyxl import Workbook
from openpyxl.styles import Font
from colorama import init, Fore, Style
import pygame

#Definiciones


def Valida(minimo,maximo):  #Valida el número introducido
    opcion=0
    while True:
        try:
            opcion=int(input(f"Escribe un número entre {minimo} y {maximo}: "))
            if minimo <= opcion <= maximo:
                break
            else:
                print(Fore.RED + f"¡Opción fuera de rango! Por favor, introduce un número entre {minimo} y {maximo}.")
        except ValueError:
             print(Fore.RED + "¡Entrada inválida! Por favor, introduce un número entero.")
    return opcion


def Menu():
    print("\n" + Fore.CYAN + Style.BRIGHT + "="*30)
    print(Fore.CYAN + Style.BRIGHT + "\n     MENÚ PRINCIPAL    ")
    print("\n" + Fore.CYAN + Style.BRIGHT + "="*30)
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")
    
    opcion=Valida(1, 4)
    return opcion

def Submenu():
    print("\n----SELECCIONA DIFICULTAD----")
    print("1. Facil(20 intentos)")
    print("2. Medio(12 intentos)")
    print("3. Dificil(5 intentos)")
    print("4. Volver al menú principal")
  
    subopcion=Valida(1, 4)
    return subopcion
    
def juego_solitario(n): #Modo 1 jugador
    print(Fore.CYAN + "\n ---MODO SOLITARIO---")
    jugador1=input("Escribe tu nombre: ")
    numero1=random.randint(1,1000)

    print(Fore.MAGENTA + f"Adivina el número que estoy pensando entre el 1 al 1000, tienes {n} intentos: ")
    for i in range(n):
        
        intentos_restantes=n-i
        print(f"Te quedan {Fore.YELLOW}{intentos_restantes} intentos.")

        numero2 = Valida(1,1000)
        
        if numero2 < numero1:
            print(Fore.YELLOW + "El número es mayor")
            
        elif numero2 > numero1:
            print(Fore.YELLOW + "El número es menor")
            
        else: #Si gana el jugador
            print(Fore.GREEN + Style.BRIGHT + f"¡Felicidades {jugador1}! Has adivinado el número {numero1}.")
            return {"jugador1": jugador1, "jugador2": "CPU", "ganador": jugador1, "intentos": i+1}

    #Si gana la consola
    print(Fore.RED + f"Lo siento, no has adivinado el número. Era {numero1}.")
    return {"jugador1": jugador1, "jugador2": "CPU", "ganador": "CPU", "intentos": n}

def juego_multiplayer(n): #Modo 2 jugadores
    print(Fore.CYAN + "\n ---MODO 2 JUGADORES---")
    jugador1=input("Escribe tu nombre Jugador 1: ")
    jugador2=input("Escribe tu nombre Jugador 2: ")

    print(f"{jugador1}, escribe un número entre 1 y 1000: ")
    numero1=Valida(1,1000)

    print("\n" * 50) #Ocultar el número
    print(Fore.MAGENTA + "¡NUMERO OCULTO!")

    
    print(f"{jugador2}, te toca adivinar. Tienes {n} intentos: ")
    for i in range(n):

        intentos_restantes=n-i
        print(f"Te quedan {Fore.YELLOW}{intentos_restantes} intentos.")
        
        numero2=Valida(1,1000)
        
        if numero2 < numero1:
            print(Fore.YELLOW + "El número es mayor")
            
        elif numero2 > numero1:
            print(Fore.YELLOW + "El número es menor")
            
        else: #Si gana el jugador2
            print(Fore.GREEN + Style.BRIGHT + f"¡Felicidades {jugador2}! Has adivinado el número {numero1}.")
            return {"jugador1": jugador1,"jugador2": jugador2, "ganador": jugador2, "intentos": i+1}

    #Si gana el jugador1
    print(Fore.RED + f"Lo siento, no has adivinado el número. Era {numero1}.")
    print(Fore.GREEN + f"¡Felicidades {jugador1}! Has ganado la partida.")
    
    return {"jugador1": jugador1, "jugador2": jugador2, "ganador": jugador1, "intentos": n}
    
def mostrar_pantalla(historial): #Estadísticas
    if not historial:
        print("No hay partidas registradas todavía.")
        return
    print ("HISTORIAL DE PARTIDAS")
    print ("-" * 60)
    print ("Jugador1, Jugador2, Ganador, Intentos")
    for p in historial:
        print(f"> {p['jugador1']} , {p['jugador2']}, {p['ganador']}, {p['intentos']}")

def guardar_excel(historial): #Necesario para el autoguardado en el Excel

    if not historial:
        return

    wb = Workbook()
    hoja= wb.active
    hoja.title = "Resultados"

    headers = ["jugador1", "jugador2", "ganador", "intentos"]
    hoja.append(headers)

    for celda in hoja[1]:
        celda.font= Font(bold=True)

    for p in historial:
        fila = [p["jugador1"], p["jugador2"], p["ganador"], p["intentos"]]
        hoja.append(fila)

    try:
        wb.save("Estadisticas_juego.xlsx")
        print(Fore.GREEN + "\n Partida guardada en Excel automáticamente")
    except:
        print(Fore.RED + "\n AVISO: No se puede guardar porque tiene el Excel abierto. Inténtelo con el Excel cerrado")
        