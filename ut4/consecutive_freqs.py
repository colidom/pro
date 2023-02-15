# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items, as_string=False):
    prev_item = 0
    unique_items = []
    repeated = 0

    for item in items:

        if not as_string:
            # Salida Lista de tuplas
            if item != prev_item:
                prev_item = item
                unique_items.append(item)
                repeated += 0
            else:
                repeated += 1


items = [1, 2, 2, 4, 4, 5]
cfreq(items, as_string=False)
