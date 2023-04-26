# ******************
# FIBONACCI ITERABLE
# ******************


class FibonacciIterable:
    def __init__(self, n_values_to_generate: int):
        self.n_values_to_generate = n_values_to_generate
        self.pointer = 0
        self.fst_num = 0
        self.snd_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= self.n_values_to_generate:
            raise StopIteration
        next_value = self.fst_num
        self.fst_num, self.snd_num = self.snd_num, self.fst_num + self.snd_num
        self.pointer += 1
        return next_value


def run(n: int) -> list:
    return list(FibonacciIterable(n))
