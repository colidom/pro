# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    imoves_splitted = imoves.split(",")
    for imove in imoves_splitted:
        article_name = imove[0]
        amount = int(imove[1:])
        # Opción más compacta
        inventory[article_name] = inventory.get(article_name, 0) + amount
        # Opción con condicional
        # if article_name in inventory:
        #     inventory[article_name] += amount
        # else:
        #     inventory[article_name] = amount

    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
