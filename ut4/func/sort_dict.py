# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = sorted(unsorted_items.items(), key lambda) 
    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
