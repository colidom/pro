# ********************
# AQUÍ TIENE SU VUELTA
# ********************
"""
Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. Por lo tanto hay que devolver el cambio. 
La tienda dispone de una serie concreta de monedas/billetes. El objetivo del ejercicio es devolver el cambio al cliente empezando por la moneda/billete 
más grande y llegando hasta la más pequeña                           
    • Si el dinero es justo hay que devolver un diccionario vacío.
    • Si el cambio no es posible hay que devolver None.
"""


def run(to_give_back: float, available_currencies: list) -> dict:

    money_back = {}
    for money in sorted(available_currencies):
        pass
    if to_give_back > 0:
        return None
    else:
        return money_back


if __name__ == "__main__":
    run(20, [5, 2, 1])
