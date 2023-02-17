# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items, /, as_string=False):
    freqs = []

    # Salida Lista de tuplas
    if not as_string:
        prev_item = items[0]
        rep_item = 1
        for item in items[1:]:
            if item != prev_item:
                freqs.append((prev_item, rep_item))
                rep_item = 1
                prev_item = item
            else:
                rep_item += 1
        freqs.append((prev_item, rep_item))
    print(freqs)


items = [1, 2, 2, 4, 4, 5, 1]
cfreq(items, as_string=False)
