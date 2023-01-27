# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = "data/avg_temps/avg_temps.dat"
    month_temps = []
    avg_temps = []
    # Lectura del fichero y cálculo de media de temperaturas
    with open(input_path, "r") as file_input:
        for temperatures in file_input:
            temperatures_list = temperatures.split(",")
            for temperature in temperatures_list:
                month_temps.append(int(temperature))
                month_temperature = sum(month_temps)
                avg_temps.append(month_temperature / len(month_temps))
                month_temps = []

    # Escritura al fichero data/avg_temps/.expected
    with open(output_path, "w") as file_output:
        for avg_temp in avg_temps:
            file_output.write(f"{avg_temp:.2f}\n")

    return filecmp.cmp(output_path, "data/avg_temps/.expected", shallow=False)


if __name__ == "__main__":
    run("data/avg_temps/temperatures.dat")
