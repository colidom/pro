""" 
Juego Tres en raya 
   __|_|__
   __|_|__  O X
     | |
"""
# Nombre de los jugadores
player_1 = input("Nombre del jugador 1: ")
player_2 = input("Nombre del jugador 2: ")

# Inicializando variables
playing = True
moves = 0

# Inicio del juego
while playing:
    print("Elija donde desea colocar su ficha!")
    row = input("Fila: ")
    column = input("Columna: ")
    moves += 1
    if moves == 9:
        playing = False

print(f"Fichas en el tablero: {moves}")
