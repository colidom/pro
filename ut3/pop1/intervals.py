# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    irange = []
    left_symbol = interval[0]
    right_symbol = interval[-1]
    nrange = interval[1:-1]
    nrange_split = nrange.split(",")
    first_value = int(nrange_split[0])
    last_value = int(nrange_split[1])
    if left_symbol == "(":
        first_value += 1
    if right_symbol == "]":
        last_value += 1
    irange = list(range(first_value, last_value))
    return irange


if __name__ == "__main__":
    run("(3,10]")
