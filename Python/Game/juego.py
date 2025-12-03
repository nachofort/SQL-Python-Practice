from funciones import *
from colorama import Fore


try:  #Musica Fondo
    pygame.mixer.init()
    pygame.mixer.music.load("musica1.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    MUSICA_ACTIVA = True

except:
    MUSICA_ACTIVA = False

    
def main():
    historial_partidas = []

    while True:
        opcion = Menu()

        if opcion == 1: #Solitario
            dif = Submenu()
            if dif == 4: continue
            niveles = {1: 20, 2: 12, 3: 5}
            n = niveles.get(dif, 20)

            resultado = juego_solitario(n)
            
            historial_partidas.append(resultado)
            guardar_excel(historial_partidas)

        elif opcion == 2: #Multijugador
            dif = Submenu()
            if dif == 4: continue

            niveles = {1: 20, 2: 12, 3: 5}
            n = niveles.get(dif, 20)

            resultado = juego_multiplayer(n)
            
            historial_partidas.append(resultado)
            guardar_excel(historial_partidas)

        elif opcion == 3: #Ver estadísticas
            mostrar_pantalla(historial_partidas) 

        elif  opcion == 4: # Salir
            print(Fore.CYAN + "¡Gracias por jugar! ¡Hasta luego!")

            #Para apagar la música
            if MUSICA_ACTIVA:
                pygame.mixer.music.fadeout(2000)
                
            break

if __name__ == "__main__":
    main()
            




            
            
    