from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __str__(self) -> str:
        return f"{self.sequence}"
    
    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def calc_adenine(self) -> str:
        return self.sequence.count(DNA.ADENINE)

    @property
    def calc_thymine(self) -> str:
        return self.sequence.count(DNA.THYMINE)

    @property
    def calc_cytosine(self) -> str:
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def calc_guanine(self) -> str:
        return self.sequence.count(DNA.GUANINE)

    def __add__(self, other: DNA) -> DNA:
        new_seq = ''.join([max(val_seq_1, val_seq_2) for val_seq_1, val_seq_2 in zip(self.sequence, other.sequence)])
        return DNA(new_seq)

    def __mul__(self, other: DNA) -> DNA:
        new_seq = ''.join(val_seq_1 for val_seq_1, val_seq_2 in zip(self.sequence, other.sequence) if val_seq_1 == val_seq_2)
        return DNA(new_seq)

    def get_occurrence_of_each_base(self):
        pass

    @classmethod
    def build_from_file(cls, path):
        buffer = []
        with open(path) as f:
            for bases in f:
                buffer.append(bases.strip())
        return DNA("".join(buffer))

    def dump_to_file(self, path):
        with open(path) as f:
            pass
