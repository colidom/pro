# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    # Solución con bucle
    # for article_name, article_stock in stock.items():
    #     available = True
    #     if merch == article_name and article_stock < amount:
    #         available = False
    #         break
    # Solución sin bucle
    merch_stock = stock[merch]
    available = merch_stock >= amount
    return available


if __name__ == "__main__":
    run({"pen": 20, "cup": 11, "keyring": 40}, "cup", 9)
