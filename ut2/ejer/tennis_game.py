# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    player_A = player_B = 0
    for point in points:
        if point == "A":
            player_A += 1
        else:
            player_B += 1
    if player_A >= 4 or player_B >= 4 and abs(player_A - player_B) > 2:
        if player_A > player_B:
            winner = "A"
        else:
            winner = "B"

    return winner


if __name__ == "__main__":
    run("ABAABA")
