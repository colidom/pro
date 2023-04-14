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


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.year = year if 1900 <= 2050 else 1900
        self.month = month if 0 < month <= 12 else 1
        self.day = day if day <= Date.is_leap_year(year) or month == DAYS_IN_MONTH[month] else 1
        self.leap_year = True if Date.is_leap_year(year) and self.month == 2 else False

    @staticmethod
    def is_leap_year(year) -> bool:
        division4 = (year % 4 == 0) or (year % 100 != 0)
        division400 = year % 400 == 0
        return True if division4 or division400 else False

    def days_in_month(self) -> int:
        if Date.is_leap_year(self.year) or self.month == 2:
            return DAYS_IN_MONTH[self.month]
        return DAYS_IN_MONTH[self.month] + 1

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        if Date.is_leap_year(self.year):
            return 366
        return 365

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        pass

    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day}/{self.month}/{self.year}"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        return f"{self.weekday()} {self.day} de {self.year}"

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


date = Date(6, 10, 2012)
print(date.leap_year)
print(date.delta_days())
