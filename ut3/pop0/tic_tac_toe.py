import sys

"""
Juego tic tac toe, recibe dos argumentos al iniciar el script
Args
--------
    - Player_1(X)
    - Player_2(O)
Examples
--------
    > python tic_tac_toe.py name1 name2 
"""
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
    print("\n--Tablero--   --Guía de juego--   --Jugadores--\n")
    print("", a, "|", b, "|", c, end="       ")
    print(1, "|", 2, "|", 3)
    print("", "---------", end="       ")
    print(f"---------       Jugador(X): {player_1[0]}   ")
    print("", d, "|", e, "|", f, end="       ")
    print(4, "|", 5, "|", 6)
    print("", "---------", end="       ")
    print(f"---------       Jugador(O): {player_2[0]}   ")
    print("", g, "|", h, "|", i, end="       ")
    print(7, "|", 8, "|", 9)

    # Lógica del juego
    loop = 1
    while loop < 5:
        user = input("\nIntroduzca un número de 1-9: ")
        # Comprobamos si el valor por consola es numérico
        if user.isdigit():
            # La lógica de nuestro juego
            pass
        else:
            # Si no es numérico, error y continue al if
            print("\nError: Solo se admiten valores numéricos")
            continue
        # Pintamos el tablero
        print("\n--Tablero--   --Guía de juego--   --Jugadores--\n")
        print("", a, "|", b, "|", c, end="       ")
        print(1, "|", 2, "|", 3)
        print("", "---------", end="       ")
        print(f"---------       Player(X): {player_1[0]}   ")
        print("", d, "|", e, "|", f, end="       ")
        print(4, "|", 5, "|", 6)
        print("", "---------", end="       ")
        print(f"---------       Player(O): {player_2[0]}   ")
        print("", g, "|", h, "|", i, end="       ")
        print(7, "|", 8, "|", 9)
    else:
        print("Empate")

    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
