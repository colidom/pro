# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    with open(input_path, "r") as file_input:
        freq_1 = {}
        file = file_input.read()
        file = file.replace("\n", " ").lower()
        file_to_list = file.split()
    for word in file_to_list:
        if word not in freq_1:
            freq_1[word] = 1
        else:
            freq_1[word] += 1
    freq = freq_1.copy()
    for key, value in freq_1.items():
        if value < lower_bound:
            del freq[key]

    return freq


if __name__ == "__main__":
    run("data/word_freq/cistercian.txt", 9)
