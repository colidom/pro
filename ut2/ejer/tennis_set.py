# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    games_player1 = games_player2 = 0
    points_player1 = points_player2 = 0

    for point in points:
        if point == "A":
            points_player1 += 1
        else:
            points_player2 += 1
        
        if points_player1 >= 4 and points_player1 - points_player2 >= 2:
            games_player1 += 1
            points_player1 = 0
            points_player2 = 0
        if points_player2 >= 4 and points_player2 - points_player1 >= 2:
            games_player2 += 1
            points_player1 = 0
            points_player2 = 0

    if games_player1 == 6 and games_player1 - games_player2 >= 2:
        print("Player1: ",games_player1)
    if games_player2 == 6 and games_player2 - games_player1 >= 1:
        print("Player2: ",games_player2)
    if games_player1 == 6 and games_player2 == 6:
        print("Tie-Break")
    return games_player1, games_player2


if __name__ == "__main__":
    run("AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB")
