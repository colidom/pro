# *****************
# SUMA DE COCIENTES
# *****************
"""
| Escriba una función recursiva que calcule la suma de cocientes de un número.                                                    │
│                                                                                                                                 │
│ La suma de cocientes un número entero n se define como:                                                                         │
│                                                                                                                                 │
│   n                                                                                                                             │
│ ____                                                                                                                            │
│ ╲                                                                                                                               │
│  ╲    1       1   1         1                                                                                                   │
│  ╱    ─ = 1 + ─ + ─ + ... + ─                                                                                                   │
│ ╱     k       2   3         n                                                                                                   │
│ ‾‾‾‾                                                                                                                            │
│ k = 1                                                                                                                           │
│                                                                                                                                 │
│ Por ejempo, si n=4 entonces la suma de cocientes quedaría como: 1 + 1/2 + 1/3 + 1/4  
"""


def sum_quot(n: int) -> float:
    if n == 1:
        return 1
    return 1 / +sum_quot(n - 1)


sum_quot(5)
