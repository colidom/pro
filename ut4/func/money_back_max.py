# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************
"""
Un cliente compra un artículo en una tienda con dinero suficiente (mayor o igual) que el importe del artículo. 
Por lo tanto hay que devolver el cambio. La tienda dispone de una serie concreta de monedas/billetes con un máximo 
de unidades de cada moneda/billete. El objetivo del ejercicio es devolver el cambio al cliente empezando por la 
moneda/billete más grande y llegando hasta la más pequeña.                                                                                      
                                                                                                                                                                
Notas:                                                                                                                                                           
                                                                                                                                                                
 • Si el dinero es justo hay que devolver un diccionario vacío.                                                                                                  
 • Si el cambio no es posible hay que devolver None   
"""


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    for currency, max_currency_qty in sorted(available_currencies.items(), reverse=True):
        currency_qty_free = to_give_back // currency
        currency_qty = min(currency_qty_free, max_currency_qty)
        if currency_qty > 0:
            money_back[currency] = currency_qty
        to_give_back -= currency * currency_qty
        if to_give_back == 0:
            return money_back
    return None


if __name__ == "__main__":
    run(20, {5: 3, 2: 7, 1: 3})
