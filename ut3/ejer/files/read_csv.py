# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open(datafile, "r") as file_input:
        pokemons = {}
        data = []

        csv_header = file_input.readline().strip().split(",")

        for header_item, body_item in zip(csv_header, file_input):
            stripped_line = body_item.strip()
            for line in stripped_line.split(","):
                pokemons[header_item] = line

        data.append(pokemons)
        print(data)

    return data


if __name__ == "__main__":
    run("data/read_csv/pokemon.csv")
