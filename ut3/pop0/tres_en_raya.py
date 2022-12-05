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
print(sys.argv)
while playing == "s":
    # Inicializamos variables vacías para pintar tablero
    # a = b = c = d = e = f = g = h = i = "  "
    board = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]

    # Pintamos el tablero
    print("\n        Tablero          Guía de juego          Jugadores")
    print("   -------------------------------------------------------------")
    print("    ", board[0], "|", board[1], "|", board[2], end="          ")
    print(1, "|", 2, "|", 3)
    print("  ", " ----+----+----", end="       ")
    print(f" ---+---+---     Jugador(❌): {player_1[0]}   ")
    print("    ", board[3], "|", board[4], "|", board[5], end="          ")
    print(4, "|", 5, "|", 6)
    print("  ", " ----+----+----", end="       ")
    print(f" ---+---+---     Jugador(🟢): {player_2[0]}   ")
    print("    ", board[6], "|", board[7], "|", board[8], end="          ")
    print(7, "|", 8, "|", 9)

    # Lógica del juego
    check_board = [" ", " ", " ", " ", " ", " ", " ", "  ", " "]
    player1_turn = True
    player2_turn = False
    loop = 0
    while loop < 9:

        if player1_turn:
            user_1 = input(
                f"\n {player_1[0].upper()} indica un número del 1 al 9 para colocar la ficha (❌): "
            )
            # Comprobamos si el valor por consola es numérico
            if user_1.isdigit():
                x = int(user_1)
                # Comprobamos si la celda está disponible
                if (
                    x == check_board[0]
                    or x == check_board[1]
                    or x == check_board[2]
                    or x == check_board[3]
                    or x == check_board[4]
                    or x == check_board[5]
                    or x == check_board[6]
                    or x == check_board[7]
                    or x == check_board[8]
                    or x > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 1 para pintarlo en el tablero
                    if x == 1:
                        board[0] = "❌"
                        check_board[1] = 1
                    if x == 2:
                        board[1] = "❌"
                        check_board[2] = 2
                    if x == 3:
                        board[2] = "❌"
                        check_board[3] = 3
                    if x == 4:
                        board[3] = "❌"
                        check_board[4] = 4
                    if x == 5:
                        board[4] = "❌"
                        check_board[5] = 5
                    if x == 6:
                        board[5] = "❌"
                        check_board[6] = 6
                    if x == 7:
                        board[6] = "❌"
                        check_board[7] = 7
                    if x == 8:
                        board[7] = "❌"
                        check_board[8] = 8
                    if x == 9:
                        board[8] = "❌"
                        check_board[8] = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras Jugador 1 elegir posición
            print("\n        Tablero          Guía de juego          Jugadores")
            print("   -------------------------------------------------------------")
            print("    ", board[0], "|", board[1], "|", board[2], end="          ")
            print(1, "|", 2, "|", 3)
            print("  ", " ----+----+----", end="       ")
            print(f" ---+---+---     Jugador(❌): {player_1[0]}   ")
            print("    ", board[3], "|", board[4], "|", board[5], end="          ")
            print(4, "|", 5, "|", 6)
            print("  ", " ----+----+----", end="       ")
            print(f" ---+---+---     Jugador(🟢): {player_2[0]}   ")
            print("    ", board[6], "|", board[7], "|", board[8], end="          ")
            print(7, "|", 8, "|", 9)

            # Comprobamos el resultado del juego
            if (
                (board[0] + board[3] + board[6] == "❌❌❌")
                or (board[1] + board[4] + board[7] == "❌❌❌")
                or (board[2] + board[5] + board[8] == "❌❌❌")
                or (board[0] + board[1] + board[2] == "❌❌❌")
                or (board[3] + board[4] + board[5] == "❌❌❌")
                or (board[6] + board[7] + board[8] == "❌❌❌")
                or (board[0] + board[4] + board[8] == "❌❌❌")
                or (board[6] + board[4] + board[2] == "❌❌❌")
            ):
                print("--------------------------------------------------------------")
                print(f"Jugador {player_1[0]} ha ganado 🎉🎉")
                break
            player1_turn = False
            player2_turn = True
            loop = loop + 1
        else:
            user_2 = input(
                f"\n {player_2[0].upper()} indica un número del 1 al 9 para colocar la ficha (🟢): "
            )
            if user_2.isdigit():
                y = int(user_2)
                # Comprobamos si la celda está disponible
                if (
                    y == check_board[0]
                    or y == check_board[1]
                    or y == check_board[2]
                    or y == check_board[3]
                    or y == check_board[4]
                    or y == check_board[5]
                    or y == check_board[6]
                    or y == check_board[7]
                    or y == check_board[8]
                    or y > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 2
                    if y == 1:
                        board[0] = "🟢"
                        check_board[1] = 1
                    if y == 2:
                        board[1] = "🟢"
                        check_board[2] = 2
                    if y == 3:
                        board[2] = "🟢"
                        check_board[3] = 3
                    if y == 4:
                        board[3] = "🟢"
                        check_board[4] = 4
                    if y == 5:
                        board[4] = "🟢"
                        check_board[5] = 5
                    if y == 6:
                        board[5] = "🟢"
                        check_board[6] = 6
                    if y == 7:
                        board[6] = "🟢"
                        check_board[7] = 7
                    if y == 8:
                        board[7] = "🟢"
                        check_board[8] = 8
                    if y == 9:
                        board[8] = "🟢"
                        check_board[8] = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras
            print("\n        Tablero          Guía de juego          Jugadores")
            print("   -------------------------------------------------------------")
            print("    ", board[0], "|", board[1], "|", board[2], end="          ")
            print(1, "|", 2, "|", 3)
            print("  ", " ----+----+----", end="       ")
            print(f" ---+---+---     Jugador(❌): {player_1[0]}   ")
            print("    ", board[3], "|", board[4], "|", board[5], end="          ")
            print(4, "|", 5, "|", 6)
            print("  ", " ----+----+----", end="       ")
            print(f" ---+---+---     Jugador(🟢): {player_2[0]}   ")
            print("    ", board[6], "|", board[7], "|", board[8], end="          ")
            print(7, "|", 8, "|", 9)

            # Comprobamos el resultado del juego
            if (
                (board[0] + board[3] + board[6] == "🟢🟢🟢")
                or (board[1] + board[4] + board[7] == "🟢🟢🟢")
                or (board[2] + board[5] + board[8] == "🟢🟢🟢")
                or (board[0] + board[1] + board[2] == "🟢🟢🟢")
                or (board[3] + board[4] + board[5] == "🟢🟢🟢")
                or (board[6] + board[7] + board[8] == "🟢🟢🟢")
                or (board[0] + board[4] + board[8] == "🟢🟢🟢")
                or (board[6] + board[4] + board[2] == "🟢🟢🟢")
            ):
                print("--------------------------------------------------------------")
                print(f"Jugador {player_2[0]} ha ganado 🎉🎉")
                break
            player2_turn = False
            player1_turn = True
            loop = loop + 1
    else:
        print("--------------------------------------------------------------")
        print("Empate❌🟢")
    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
    if playing == "n":
        print("==============================================")
        print("                ¡Hasta pronto!                ")
        print("==============================================")
