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
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self) -> bool:
        division4 = (self.year % 4 == 0) or (self.year % 100 != 0)
        division400 = self.year % 400 == 0
        return True if division4 or division400 else False

    def days_in_month(self) -> int:
        if self.is_leap_year() or self.month == 2:
            return DAYS_IN_MONTH[self.month]
        return DAYS_IN_MONTH[self.month] + 1

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        pass

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
        return f"{self.weekday} {self.day} de {self.year}"

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


date = Date(6, 10, 1990)
print(date.days_in_month())
