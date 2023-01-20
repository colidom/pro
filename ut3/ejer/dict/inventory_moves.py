# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    imoves_splitted = imoves.split(",")
    for imove in imoves_splitted:
        article_name = imove[0]
        inventory_mod = int(imove[1:])
        inventory[article_name] = inventory_mod

    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
