from __future__ import annotations

MIN_YEAR = 1900
MAX_YEAR = 2050

DAYS_IN_MONTH = {
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
WEEKDAYS = [
    "DOMINGO",
    "LUNES",
    "MARTES",
    "MIÉRCOLES",
    "JUEVES",
    "VIERNES",
    "SÁBADO",
]
MONTHS = [
    "ENERO",
    "FEBRERO",
    "MARZO",
    "ABRIL",
    "MAYO",
    "JUNIO",
    "JULIO",
    "AGOSTO",
    "SEPTIEMBRE",
    "OCTUBRE",
    "NOVIEMBRE",
    "DICIEMBRE",
]


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos."""

        self.year = year if MIN_YEAR <= year <= MAX_YEAR else MIN_YEAR
        self.month = month if 0 < month <= 12 else 1
        self.day = day if day <= DAYS_IN_MONTH[self.month] else 1
        self.leap_year = Date.is_leap_year(self)

    @staticmethod
    def is_leap_year(item) -> bool:
        year = item if isinstance(item, int) else item.year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        days_since_start = 0
        for year in range(MIN_YEAR, self.year):
            days_since_start += 366 if Date.is_leap_year(year) else 365
        for month in range(1, self.month):
            days_since_start += DAYS_IN_MONTH[month]
        if self.month > 2 and Date.is_leap_year(self.year):
            days_since_start += 1
        days_since_start += self.day - 1
        return days_since_start

    @property
    def days_in_month(self) -> int:
        """Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        if Date.is_leap_year(self) and self.month == 2:
            return DAYS_IN_MONTH[self.month] + 1
        return DAYS_IN_MONTH[self.month]

    @property
    def weekday(self) -> int:
        delta_days = self.get_delta_days()
        weekday = (delta_days + 1) % 7
        return weekday

    @property
    def is_weekend(self) -> bool:
        return self.weekday == 0 or self.weekday == 6

    @property
    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self) -> str:
        return f"{WEEKDAYS[self.weekday]} {self.day} DE {MONTHS[self.month - 1]} DE {self.year}"

    def __add__(self, days: int) -> "Date":
        """Sumar un número de días a la fecha"""

        year = self.year
        month = self.month
        day = self.day

        # Calcular el nuevo día sumando los días indicados
        while days > 0:
            days_in_month = DAYS_IN_MONTH[month]
            if Date.is_leap_year(year) and month == 2:
                days_in_month += 1

            if day + days > days_in_month:
                days_to_end_of_month = days_in_month - day + 1
                days -= days_to_end_of_month
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            else:
                day += days
                days = 0

        return Date(day, month, year)

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
