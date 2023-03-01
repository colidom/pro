# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:

    money_back = {}
    for money in sorted(available_currencies, reverse=True):
        if to_give_back >= money:
            currency_qty = to_give_back // money
            to_give_back = to_give_back % money
            money_back[money] = currency_qty
    if to_give_back > 0:
        return None
    return money_back


if __name__ == "__main__":
    run(20, [5, 2, 1])
