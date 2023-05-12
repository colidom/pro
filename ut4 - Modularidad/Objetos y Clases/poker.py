from __future__ import annotations


def load_card_glyphs(path: str = "cards.dat") -> dict[str, str]:
    """Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador"""
    new_neck = {}
    with open(path) as f:
        for line in f:
            suit, cards = line.strip().split(":")
            new_neck[suit] = cards.replace(",", "")
    return new_neck


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        """Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)"""
        if suit not in Card.GLYPHS:
            raise InvalidCardError(err_msg=f"{repr(suit)} is not a supported suit")
        if isinstance(value, int) and (value < Card.A_VALUE or value > Card.K_VALUE):
            raise InvalidCardError(err_msg=f"{repr(value)} is not a supported value")
        if isinstance(value, str) and (value not in Card.SYMBOLS):
            raise InvalidCardError(err_msg=f"{repr(value)} is not a supported symbol")

        self.value = value
        self.suit = suit

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        if isinstance(self.value, str):
            return Card.SYMBOLS.index(self.value) + 1
        return self.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return Card.GLYPHS[self.suit][self.cmp_value - 1]

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        if (self.cmp_value == other.cmp_value) and (other.suit == self.suit):
            return True
        return False

    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        if not isinstance(other, Card):
            return False
        if other.cmp_value == Card.A_VALUE or self.cmp_value < other.cmp_value:
            return True
        return False

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        if not isinstance(other, Card):
            return False
        if self.cmp_value == Card.A_VALUE or self.cmp_value > other.cmp_value:
            return True
        return False

    def __add__(self, other: Card) -> Card:
        """Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS."""
        suit = self.suit if self > other else other.suit
        is_ace = (
            True
            if self.cmp_value == Card.A_VALUE or other.cmp_value == Card.A_VALUE
            else False
        )
        if (result := self.cmp_value + other.cmp_value) > Card.K_VALUE or is_ace:
            value = Card.A_VALUE
        else:
            value = result
        return Card(value, suit)

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        return self.cmp_value == Card.A_VALUE

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve todos los palos como una cadena de texto"""
        return "".join(suit for suit in cls.GLYPHS)

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Función generadora que devuelve los glifos de las cartas por su palo"""
        for gliph in cls.GLYPHS[suit]:
            yield gliph


class InvalidCardError(Exception):
    """Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea"""

    def __init__(self, *, err_msg: str = ""):
        default_err_msg = "🃏 Invalid card"
        if not err_msg:
            self.err_msg = default_err_msg
        else:
            self.err_msg = f"{default_err_msg}: {err_msg}"
        super().__init__(self.err_msg)
