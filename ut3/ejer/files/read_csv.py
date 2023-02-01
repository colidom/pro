# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile, "r") as file_input:
        csv_header = file_input.readline().strip().split(",")
        for line in file_input:
            pokemons = {}
            body_items = line.strip().split(",")
            for header_item, body_item in zip(csv_header, body_items):
                if body_item.isdigit():
                    pokemons[header_item] = int(body_item)
                elif body_item == "True":
                    pokemons[header_item] = True
                elif body_item == "False":
                    pokemons[header_item] = False
                else:
                    pokemons[header_item] = body_item
            data.append(pokemons)

    return data


if __name__ == "__main__":
    run("data/read_csv/pokemon.csv")
