# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open(datafile, "r") as file_input:
        pokemons = {}
        data = []

        csv_header = file_input.readline().strip()
        print(csv_header)

        for line in file_input:
            stripped_line = line.strip()
            pokemons = {}
            #
            print(stripped_line)

    return data


if __name__ == "__main__":
    run("data/read_csv/pokemon.csv")
