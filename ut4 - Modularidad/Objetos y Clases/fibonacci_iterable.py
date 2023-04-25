# ******************
# FIBONACCI ITERABLE
# ******************


class FibonacciIterable:
    def __init__(self, n_values_to_generate: int):
        self.pointer = 0
        self.n_values_to_generate = n_values_to_generate

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= self.n_values_to_generate:
            raise StopIteration


def run(n):
    fibo = FibonacciIterable(n)
