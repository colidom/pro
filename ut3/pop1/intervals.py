# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    irange = []

    corchetes_index_start = interval.find("[")
    corchetes_index_end = interval.find("]")
    parentesis_index_start = interval.find("(")
    parentesis_index_end = interval.find(")")
    extracted = interval[1:-1]
    val1 = extracted.split(",")[0]
    val2 = extracted.split(",")[1]
    if corchetes_index_start != -1 or parentesis_index_end != -1:
        for i in range(int(val1), int(val2) + 1):
            irange.append(i)
    else:
        for i in range(int(val1), int(val2) + 1):
            irange.append(i)

    return irange


if __name__ == "__main__":
    run("(3,10]")
