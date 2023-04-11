# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = []
    packed_items = [f"{v}:{k}" for k, v in unsorted_items.items()]
    packed_items.sort()
    for item in packed_items:
        value, key = item.split(":")
        fixed_item = (key, value)
        sorted_items.append(fixed_item)
    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
