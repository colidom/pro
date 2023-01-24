# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    output = ()
    first_set = []
    second_set = []
    for internal_tuple in input:
        first_set.append(internal_tuple[0])
        second_set.append(internal_tuple[1])

    output = (set(first_set), set(second_set))
    return output


if __name__ == "__main__":
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
