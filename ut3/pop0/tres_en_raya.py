import sys

"""
Juego Tres en Raya , recibe dos argumentos al iniciar el script
Args
--------
    - Player_1(X)
    - Player_2(O)
Examples
--------
    > python tres_en_raya.py player1 player2 
"""
print("    ===============================================")
print("           Bienvenidos al juego Tres en Raya       ")
print("    ===============================================")
# Guardamos los nombres introducidos por consola
player_1 = sys.argv[1:2]
player_2 = sys.argv[2:3]

playing = "s"
while playing == "s":
    # Inicializamos variables vacías para pintar tablero
    # a = b = c = d = e = f = g = h = i = "  "
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Pintamos el tablero
    print("\n    --Tablero--   --Guía de juego--     --Jugadores--")
    print("-------------------------------------------------------")
    print("   ", board[0], "|", board[1], "|", board[2], end="       ")
    print(1, "|", 2, "|", 3)
    print("  ", "-----------", end="       ")
    print(f"---------       Jugador(X): {player_1[0]}   ")
    print("   ", board[3], "|", board[4], "|", board[5], end="       ")
    print(4, "|", 5, "|", 6)
    print("  ", "-----------", end="       ")
    print(f"---------       Jugador(O): {player_2[0]}   ")
    print("   ", board[6], "|", board[7], "|", board[8], end="       ")
    print(7, "|", 8, "|", 9)

    # Lógica del juego
    board2 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_turn = True
    player2_turn = False
    loop = 0
    while loop < 9:

        if player1_turn:
            user_1 = input(
                f"\n {player_1[0].upper()} indica un número del 1 al 9 para colocar la ficha (X): "
            )
            # Comprobamos si el valor por consola es numérico
            if user_1.isdigit():
                x = int(user_1)
                # Comprobamos si la celda está disponible
                if (
                    x == board2[0]
                    or x == board2[1]
                    or x == board2[2]
                    or x == board2[3]
                    or x == board2[4]
                    or x == board2[5]
                    or x == board2[6]
                    or x == board2[7]
                    or x == board2[8]
                    or x > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 1 para pintarlo en el tablero
                    if x == 1:
                        board[0] = "X"
                        board2[1] = 1
                    if x == 2:
                        board[1] = "X"
                        board2[2] = 2
                    if x == 3:
                        board[2] = "X"
                        board2[3] = 3
                    if x == 4:
                        board[3] = "X"
                        board2[4] = 4
                    if x == 5:
                        board[4] = "X"
                        board2[5] = 5
                    if x == 6:
                        board[5] = "X"
                        board2[6] = 6
                    if x == 7:
                        board[6] = "X"
                        board2[7] = 7
                    if x == 8:
                        board[7] = "X"
                        board2[8] = 8
                    if x == 9:
                        board[8] = "X"
                        board2[8] = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras Jugador 1 elegir posición
            print("\n    --Tablero--   --Guía de juego--     --Jugadores--")
            print("-------------------------------------------------------")
            print("   ", board[0], "|", board[1], "|", board[2], end="       ")
            print(1, "|", 2, "|", 3)
            print("  ", "-----------", end="       ")
            print(f"---------       Jugador(X): {player_1[0]}   ")
            print("   ", board[3], "|", board[4], "|", board[5], end="       ")
            print(4, "|", 5, "|", 6)
            print("  ", "-----------", end="       ")
            print(f"---------       Jugador(O): {player_2[0]}   ")
            print("   ", board[6], "|", board[7], "|", board[8], end="       ")
            print(7, "|", 8, "|", 9)

            # Comprobamos el resultado del juego
            if (
                (board[0] + board[3] + board[6] == "XXX")
                or (board[1] + board[4] + board[7] == "XXX")
                or (board[2] + board[5] + board[8] == "XXX")
                or (board[0] + board[1] + board[2] == "XXX")
                or (board[3] + board[4] + board[5] == "XXX")
                or (board[6] + board[7] + board[8] == "XXX")
                or (board[0] + board[4] + board[8] == "XXX")
                or (board[6] + board[4] + board[2] == "XXX")
            ):
                print("-------------------------------------------------------")
                print(f"Jugador {player_1[0]} ha ganado")
                break
            player1_turn = False
            player2_turn = True
            loop = loop + 1
        else:
            user_2 = input(
                f"\n {player_2[0].upper()} indica un número del 1 al 9 para colocar la ficha (O): "
            )
            if user_2.isdigit():
                y = int(user_2)
                # Comprobamos si la celda está disponible
                if (
                    y == board2[0]
                    or y == board2[1]
                    or y == board2[2]
                    or y == board2[3]
                    or y == board2[4]
                    or y == board2[5]
                    or y == board2[6]
                    or y == board2[7]
                    or y == board2[8]
                    or y > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 2
                    if y == 1:
                        board[0] = "O"
                        board2[1] = 1
                    if y == 2:
                        board[1] = "O"
                        board2[2] = 2
                    if y == 3:
                        board[2] = "O"
                        board2[3] = 3
                    if y == 4:
                        board[3] = "O"
                        board2[4] = 4
                    if y == 5:
                        board[4] = "O"
                        board2[5] = 5
                    if y == 6:
                        board[5] = "O"
                        board2[6] = 6
                    if y == 7:
                        board[6] = "O"
                        board2[7] = 7
                    if y == 8:
                        board[7] = "O"
                        board2[8] = 8
                    if y == 9:
                        board[8] = "O"
                        board2[8] = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras
            print("\n    --Tablero--   --Guía de juego--     --Jugadores--")
            print("-------------------------------------------------------")
            print("   ", board[0], "|", board[1], "|", board[2], end="       ")
            print(1, "|", 2, "|", 3)
            print("  ", "-----------", end="       ")
            print(f"---------       Jugador(X): {player_1[0]}   ")
            print("   ", board[3], "|", board[4], "|", board[5], end="       ")
            print(4, "|", 5, "|", 6)
            print("  ", "-----------", end="       ")
            print(f"---------       Jugador(O): {player_2[0]}   ")
            print("   ", board[6], "|", board[7], "|", board[8], end="       ")
            print(7, "|", 8, "|", 9)

            # Comprobamos el resultado del juego
            if (
                (board[0] + board[3] + board[6] == "OOO")
                or (board[1] + board[4] + board[7] == "OOO")
                or (board[2] + board[5] + board[8] == "OOO")
                or (board[0] + board[1] + board[2] == "OOO")
                or (board[3] + board[4] + board[5] == "OOO")
                or (board[6] + board[7] + board[8] == "OOO")
                or (board[0] + board[4] + board[8] == "OOO")
                or (board[6] + board[4] + board[2] == "OOO")
            ):
                print("-------------------------------------------------------")
                print(f"Jugador {player_2[0]} ha ganado")
                break
            player2_turn = False
            player1_turn = True
            loop = loop + 1
    else:
        print("-------------------------------------------------------")
        print("Empate")
    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
    if playing == "n":
        print("==============================================")
        print("                ¡Hasta pronto!                ")
        print("==============================================")
