from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"
    BASES = ADENINE + THYMINE + CYTOSINE + GUANINE

    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __str__(self) -> str:
        return f"{self.sequence}"
    
    def __len__(self) -> int:
        return len(self.sequence)

    def __getitem__(self, index: int):
        return self.sequence[index]
    
    def __setitem__(self, index: int, new_base: str):
        bases = list(self.sequence)
        bases[index] = new_base if new_base in DNA.BASES else DNA.ADENINE
        self.sequence = "".join(bases)

    @property
    def adenines(self) -> int:
        return self.sequence.count(DNA.ADENINE)

    @property
    def thymines(self) -> int:
        return self.sequence.count(DNA.THYMINE)

    @property
    def cytosines(self) -> int:
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self) -> int:
        return self.sequence.count(DNA.GUANINE)

    def __add__(self, other):
        new_sequence = ""
        for base1, base2 in zip(self.sequence, other.sequence):
            new_sequence += max(base1, base2)
        if len(new_sequence) != max(len(self), len(other)):
            new_sequence += max(self.sequence, other.sequence)[len(new_sequence) :]
        return DNA(new_sequence)

    def __mul__(self, other: DNA) -> DNA:
        new_seq = ''.join(val_seq_1 for val_seq_1, val_seq_2 in zip(self.sequence, other.sequence) if val_seq_1 == val_seq_2)
        return DNA(new_seq)

    def stats(self) -> dict[str, float]:
        total_bases = len(self.sequence)
        adenines_rate = (self.adenines / total_bases) * 100
        thymines_rate = (self.thymines / total_bases) * 100
        cytosines_rate = (self.cytosines / total_bases) * 100
        guanines_rate = (self.guanines / total_bases) * 100
        return {
            "A": adenines_rate,
            "G": guanines_rate,
            "C": cytosines_rate,
            "T": thymines_rate,
        }

    @classmethod
    def build_from_file(cls, path):
        buffer = []
        with open(path) as f:
            for bases in f:
                buffer.append(bases.strip())
        return DNA("".join(buffer))

    def dump_to_file(self, path) -> None:
        with open(path, 'w') as f:
            f.write(self.sequence)


dna_1 = DNA("ACTGAAA")
dna_2 = DNA("ATGCA")
print(dna_1)
print(dna_1.adenines)
dna_3 = dna_1 + dna_2
print(dna_3)

print(len(dna_1))