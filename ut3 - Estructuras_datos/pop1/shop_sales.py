# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs = 0
    displays = 0
    for daily_sales in sales:
        pcs += daily_sales[0]
        displays += daily_sales[1]
    return pcs, displays


if __name__ == "__main__":
    run([[4, 5], [1, 3], [3, 2]])
