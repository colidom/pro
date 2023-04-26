# ******************
# FIBONACCI ITERABLE
# ******************


class FibonacciIterable:
    def __init__(self, n_values_to_generate: int):
        self.n_values_to_generate = n_values_to_generate
        self.pointer = 0
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= self.n_values_to_generate:
            raise StopIteration
        next_value = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        self.pointer += 1
        return next_value


def run(n: int) -> list:
    return list(FibonacciIterable(n))
