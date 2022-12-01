# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return distance


if __name__ == "__main__":
    run(3, 5, -7, -4)
