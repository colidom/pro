""" 
Juego Tres en raya 
   __|_|__
   __|_|__  O X
     | |
"""
import sys
# Nombre de los jugadores
playing = "s"
while playing == "s":
    print("===============================================")
    print("  Bienvenido al juego Piedra - Papel - Tijera  ")
    print("===============================================")
    player_1 = sys.argv[1:2]
    player_2 = sys.argv[2:]
    # Inicializamos variables vacías para pintar tablero
    a = b = c = d = e = f = g = h = i = " "
    # Pintamos el tablero

    print("\n   --Tablero--   --Guía de juego--   --Jugadores--\n")
    print("   ", a, "|", b, "|", c, end="       ")
    print(1, "|", 2, "|", 3)
    print("   ", "---------", end="       ")
    print(f"---------       Player(X): {player_1[0]}   ")
    print("   ", d, "|", e, "|", f, end="       ")
    print(4, "|", 5, "|", 6)
    print("   ", "---------", end="       ")
    print(f"---------       Player(O): {player_2[0]}   ")
    print("   ", g, "|", h, "|", i, end="       ")
    print(7, "|", 8, "|", 9)
    
    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
