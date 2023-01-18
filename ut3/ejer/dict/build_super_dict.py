# ***************************
# DICCIONARIO EN CONSTRUCCIÓN
# ***************************


def run(items: list) -> dict:
    unpack_items = {}
    for item in items:
        movie_name = item[0]
        movie_date = item[1:]
        unpack_items[movie_name] = movie_date
    return unpack_items


if __name__ == "__main__":
    run(
        [
            ["Episode IV - A New Hope", "May 25", 1977, "George Lucas"],
            ["Episode V - The Empire Strikes Back", "May 21", 1980],
            ["Episode VI - Return of the Jedi", "May 25", 1983],
        ]
    )
