from __future__ import annotations

MIN_YEAR = 1900
MAX_YEAR = 2050


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos."""

        self.DAYS_IN_MONTH = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        self.year = year if MIN_YEAR <= year <= MAX_YEAR else MIN_YEAR
        self.month = month if 0 < month <= 12 else 1
        self.day = day if day <= self.DAYS_IN_MONTH[self.month] else 1
        self.leap_year = Date.is_leap_year(self)

    @staticmethod
    def is_leap_year(item: Date) -> bool:
        year = item if isinstance(item, int) else item.year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        if Date.is_leap_year(self):
            return 366
        return 365

    @property
    def days_in_month(self) -> int:
        """Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        if Date.is_leap_year(self) and self.month == 2:
            return self.DAYS_IN_MONTH[self.month] + 1
        return self.DAYS_IN_MONTH[self.month]

    @property
    def weekday(self) -> int:
        ...

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day}/{self.month}/{self.year}"

    def __str__(self):
        """MARTES 2 DE SEPTIEMBRE DE 2003"""
        return f"{self.weekday()} {self.day} de {self.year}"

    def __add__(self, days: int) -> Date:
        """Sumar un número de días a la fecha"""
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""
        ...

    def __eq__(self, other: Date) -> bool:
        ...

    def __gt__(self, other: Date) -> bool:
        ...

    def __lt__(self, other: Date) -> bool:
        ...


date = Date(6, 10, 2012)
print(date.leap_year)
print(date.get_delta_days())
