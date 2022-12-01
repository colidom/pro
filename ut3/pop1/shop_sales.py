# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs = 0
    displays = 0
    for sale in sales:
        pcs += sale[0]
        displays += sale[1]
    return pcs, displays


if __name__ == "__main__":
    run([[4, 5], [1, 3], [3, 2]])
