# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: str) -> bool:
    n_common = []
    with open(input_path, 'r') as f:
        sentences = [line.lower().strip().split() for line in f]
    for sentence1 in sentences:
        set1 = set(sentence1)
        for sentence2 in sentences:
            set2 = set(sentence2)
            n_common.append(len(set1 & set2))

    # BLOQUE DE ESCRITURA
    output_path = 'data/common_words/output.txt'
    with open(output_path, 'w') as f:
        for n in n_common:
            f.write(f'{n}\n')

    return filecmp.cmp(output_path, 'data/common_words/.expected', shallow=False)


if __name__ == '__main__':
    run('data/common_words/minizen.txt')
