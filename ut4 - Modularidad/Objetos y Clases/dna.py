from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, sequence) -> None:
        self.sequence = sequence

    @property
    def calc_adenine(self):
        return self.sequence.count(DNA.ADENINE)

    @property
    def calc_thymine(self):
        return self.sequence.count(DNA.THYMINE)

    @property
    def calc_cytosine(self):
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def calc_guanine(self):
        return self.sequence.count(DNA.GUANINE)

    def __add__(self, other: DNA):
         new_seq = ''.join([max(val_seq_1, val_seq_2) for val_seq_1, val_seq_2 in zip(self.sequence, other.sequence)])
         return new_seq

    def __mul__(self, other: DNA):
        pass

    def get_occurrence_of_each_base(self):
        pass

    @classmethod
    def build_from_file(self, path):
        pass

    def dump_to_file(self, path):
        pass

    def __str__(self) -> str:
        return f"{self.sequence}"
