from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYNINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, dna_seq) -> None:
        self.dna_seq = dna_seq
        self.sequence = 0

    @property
    def calc_adenine(self):
        pass

    @property
    def calc_thynine(self):
        pass

    @property
    def calc_cytoshine(self):
        pass

    @property
    def calc_guanine(self):
        pass

    def __add__(self, other: DNA):
        pass

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
