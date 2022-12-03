import sys

"""
Juego tic tac toe, recibe dos argumentos al iniciar el script
Args
--------
    - Player_1(X)
    - Player_2(O)
Examples
--------
    > python tic_tac_toe.py player1 player2 
"""
print("===============================================")
print("       Bienvenidos al juego Tres en raya       ")
print("===============================================")
# Guardamos los nombres introducidos por consola
player_1 = sys.argv[1:2]
player_2 = sys.argv[2:3]

playing = "s"
while playing == "s":
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
    m = n = o = p = q = r = s = t = u = " "
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
                    x == m
                    or x == n
                    or x == o
                    or x == p
                    or x == q
                    or x == r
                    or x == s
                    or x == t
                    or x == u
                    or x > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 1 para pintarlo en el tablero
                    if x == 1:
                        a = "X"
                        n = 1
                    if x == 2:
                        b = "X"
                        o = 2
                    if x == 3:
                        c = "X"
                        p = 3
                    if x == 4:
                        d = "X"
                        q = 4
                    if x == 5:
                        e = "X"
                        r = 5
                    if x == 6:
                        f = "X"
                        s = 6
                    if x == 7:
                        g = "X"
                        t = 7
                    if x == 8:
                        h = "X"
                        u = 8
                    if x == 9:
                        i = "X"
                        u = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras Jugador 1 elegir posición
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

            # Comprobamos el resultado del juego
            if (
                (a + d + g == "OOO")
                or (b + e + h == "OOO")
                or (c + f + i == "OOO")
                or (a + b + c == "OOO")
                or (d + e + f == "OOO")
                or (g + h + i == "OOO")
                or (a + e + i == "OOO")
                or (g + e + c == "OOO")
            ):
                print("=============================")
                print(f"Jugador {player_2[0]} ha ganado")
                break
            elif (
                (a + d + g == "XXX")
                or (b + e + h == "XXX")
                or (c + f + i == "XXX")
                or (a + b + c == "XXX")
                or (d + e + f == "XXX")
                or (g + h + i == "XXX")
                or (a + e + i == "XXX")
                or (g + e + c == "XXX")
            ):
                print("=============================")
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
                    y == m
                    or y == n
                    or y == o
                    or y == p
                    or y == q
                    or y == r
                    or y == s
                    or y == t
                    or y == u
                    or y > 9
                ):
                    print("\nYa hay una ficha en esta posición, por favor elija otra")
                    continue
                else:
                    # Comprobamos el valor introducido por el jugador 2
                    if y == 1:
                        a = "O"
                        n = 1
                    if y == 2:
                        b = "O"
                        o = 2
                    if y == 3:
                        c = "O"
                        p = 3
                    if y == 4:
                        d = "O"
                        q = 4
                    if y == 5:
                        e = "O"
                        r = 5
                    if y == 6:
                        f = "O"
                        s = 6
                    if y == 7:
                        g = "O"
                        t = 7
                    if y == 8:
                        h = "O"
                        u = 8
                    if y == 9:
                        i = "O"
                        u = 9
            else:
                # Si no es numérico, error y continue al if
                print("\nError: Solo se admiten valores numéricos del 1 al 9")
                continue
            # Pintamos el tablero tras
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

            # Comprobamos el resultado del juego
            if (
                (a + d + g == "OOO")
                or (b + e + h == "OOO")
                or (c + f + i == "OOO")
                or (a + b + c == "OOO")
                or (d + e + f == "OOO")
                or (g + h + i == "OOO")
                or (a + e + i == "OOO")
                or (g + e + c == "OOO")
            ):
                print("=============================")
                print(f"Jugador {player_2} ha ganado")
                break
            elif (
                (a + d + g == "XXX")
                or (b + e + h == "XXX")
                or (c + f + i == "XXX")
                or (a + b + c == "XXX")
                or (d + e + f == "XXX")
                or (g + h + i == "XXX")
                or (a + e + i == "XXX")
                or (g + e + c == "XXX")
            ):
                print("=============================")
                print(f"Jugador {player_1} ha ganado")
                break
            player2_turn = False
            player1_turn = True
            loop = loop + 1
    else:
        print("===========================")
        print("Empate")
    playing = input("\nJuego finalizado, ¿quiere seguir jugando? s/n: ").lower()
    if playing == "n":
        print("===============================================")
        print("=                Hasta pronto                 =")
        print("===============================================")
