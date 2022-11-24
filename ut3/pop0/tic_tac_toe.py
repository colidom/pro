""" 
Juego Tres en raya 
   __|_|__
   __|_|__  O X
     | |
"""
# Nombre de los jugadores
playing = "s"
while playing == "s":
    print("Bienvenido al juego Piedra - Papel - Tijera\n")
    player_1 = input("Jugador (1) por favor introduce tu nombre: ").upper()
    print(f"Bienvenid@ {player_1} juegas como 'O'")
    player_2 = input("Jugador (2) por favor introduce tu nombre: ").upper()
    print(f"Bienvenid@ {player_2} juegas como 'X'")
    # Inicializamos variables vacías para pintar tablero
    a = b = c = d = e = f = g = h = i = " "
    # Pintamos el tablero
    print("\n--Tablero de juego--    --Guía de juego--\n")
    print("      ", a, "|", b, "|", c, end="            ")
    print(1, "|", 2, "|", 3)
    print("      ", "---------", end="            ")
    print("---------")
    print("      ", d, "|", e, "|", f, end="            ")
    print(4, "|", 5, "|", 6)
    print("      ", "---------", end="            ")
    print("---------")
    print("      ", g, "|", h, "|", i, end="            ")
    print(7, "|", 8, "|", 9)
    
    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
