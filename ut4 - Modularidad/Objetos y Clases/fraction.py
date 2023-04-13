class Fraction:
    def __init__(self, num, den):
        gcd = self.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __add__(self, other):
        fr_num = self.num * other.den
        fr_den = self.den * other.num
        return Fraction(fr_num + fr_den, self.den * other.den)

    def __sub__(self, other):
        fr_num = self.num * other.den
        fr_den = self.den * other.num
        return Fraction(fr_num - fr_den, self.den * other.den)

    def __mul__(self, other):
        fr_num = self.num * other.num
        fr_den = self.num * other.den
        return Fraction(fr_num, fr_den)

    def __truediv__(self, other):
        fr_num = self.num / other.den
        fr_den = self.num / other.num
        return Fraction(fr_num, fr_den)

    def __str__(self) -> str:
        return f"{self.num} / {self.den}"

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Algoritmo de Euclides para el cálculo del Máximo Común Divisor."""
        while b > 0:
            a, b = b, a % b
        return a


op1 = Fraction(25, 30)
op2 = Fraction(40, 45)

sum_op = op1 + op2
print(sum_op)
