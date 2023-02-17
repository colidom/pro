# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items, /, as_string=False):
    freqs = []
    # Salida como Lista de tuplas
    if len(items) > 0:
        prev_item = items[0]
        rep_item = 1
        for item in items[1:]:
            if item == prev_item:
                rep_item += 1
            else:
                freqs.append((prev_item, rep_item))
                rep_item = 1
                prev_item = item
        freqs.append((prev_item, rep_item))
    # Salida como String
    if as_string:
        freqs = ",".join([f"{i}:{f}" for i, f in freqs])

    return freqs


items = [1, 2, 2, 4, 4, 5, 1]
print(cfreq(items, as_string=True))
