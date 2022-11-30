# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs_in_day = []
    displays_in_day = []
    for sale in sales:
        pcs_in_day.append(sale[0])
        displays_in_day.append(sale[1])
    pcs = sum(pcs_in_day)
    displays = sum(displays_in_day)
    return pcs, displays


if __name__ == "__main__":
    run([[4, 5], [1, 3], [3, 2]])
