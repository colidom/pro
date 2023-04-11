# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    century = year // 100
    if year % 100 == 0:
        return century
    return century + 1


if __name__ == "__main__":
    run(1705)
