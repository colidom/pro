# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    for key, value in stock.items():
        available = True
        if merch == key and value <= amount:
            available = False
            break
    return available


if __name__ == "__main__":
    run({"pen": 20, "cup": 11, "keyring": 40}, "cup", 9)
