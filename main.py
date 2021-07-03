import numpy as np
import random
import time


# Función para crear los tableros
def crear_tablero():
    return np.full((10, 10), " ")


# 4 variables paralos 4 tablerose
tablero_usuario1 = crear_tablero()
tablero_usuario1_disparos = crear_tablero()
tablero_usuario2 = crear_tablero()
tablero_usuario2_disparos = crear_tablero()

# barcos añadido de forma fija

# barcos jugador1
tablero_usuario1[(0, 1)] = "O"
tablero_usuario1[(0, 3)] = "O"
tablero_usuario1[(0, 5)] = "O"
tablero_usuario1[(8, 1)] = "O"
tablero_usuario1[3][1:3] = "O"
tablero_usuario1[5][1:3] = "O"
tablero_usuario1[5][7:10] = "O"
tablero_usuario1[7][5:8] = "O"
tablero_usuario1[0][8:10] = "O"
tablero_usuario1[1][3:7] = "O"

# barcos jugador2
tablero_usuario2[(4, 1)] = "O"
tablero_usuario2[(3, 5)] = "O"
tablero_usuario2[(3, 7)] = "O"
tablero_usuario2[(9, 0)] = "O"
tablero_usuario2[5][3:5] = "O"
tablero_usuario2[7][3:5] = "O"
tablero_usuario2[7][7:9] = "O"
tablero_usuario2[0][1:4] = "O"
tablero_usuario2[2][1:4] = "O"
tablero_usuario2[1][3:7] = "O"

#contadores de disparos acertados de cada jugador. El contador_1 para el usuario y el contador_2 para el ordenador
contador_1 = 0
contador_2 = 0

#True es el usuario1 y False es el ordenador
tipo_jugador = True

while contador_1 < 20 and contador_2 < 20:

    # turno usuario 1
    if tipo_jugador == True:

        try:
            x = int(input("Elige un numero de fila entre 0 y 9: "))
            y = int(input("Elige un numero de columna entre 0 y 9: "))
        except (NameError, ValueError):
            print("----Tienes que eligir un numero entero entre 0 y 9. Por favor, intentalo de nuevo.----")

        if tablero_usuario2[x, y] == "O":
            tablero_usuario1_disparos[x, y] = "X"
            tablero_usuario2[x, y] = "X"
            contador_1 += 1
            print("Tocado!!\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

        elif tablero_usuario2[x, y] == " ":
            tablero_usuario1_disparos[x, y] = "-"
            tablero_usuario2[x, y] = "-"
            tipo_jugador = False
            print("Al agua!!\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")
        else:
            tipo_jugador = False
            print("Ya has eligido esta coordenada...\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

    # turno ordenador
    elif tipo_jugador == False:

        # disparo de forma aleatoria
        x2 = random.randint(0, 9)
        y2 = random.randint(0, 9)

        if tablero_usuario1[x2, y2] == "O":
            tablero_usuario2_disparos[x, y] = "X"
            tablero_usuario1[x, y] = "X"
            contador_2 += 1
            time.sleep(0.5)
            print("El ordenador ha tocado uno de tus barcos!!\nTablero de barcos usuario 1\n", tablero_usuario1, "\n")

        elif tablero_usuario1[x2, y2] == " ":
            tablero_usuario2_disparos[x2, y2] = "-"
            tablero_usuario1[x2, y2] = "-"
            tipo_jugador = True
            time.sleep(0.5)
            print("El ordenador ha disparado al agua!\nTablero de barcos usuario 1\n", tablero_usuario1,
                  "\n Tablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")
        else:
            tipo_jugador = True
            time.sleep(0.5)
            print("El ordenador le ha vuelto a dar a la misma coordenada...\nTablero de barcos usuario 1\n",
                  tablero_usuario1, "\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

# Mensaje final para proclamar si el usuario ha ganado o perdido
if contador_1 > contador_2:
    print("Has ganado al ordenador! Enhorabuena!!")
elif contador_2 > contador_1:
    print("Has perdido! El ordenador te ha vencido")