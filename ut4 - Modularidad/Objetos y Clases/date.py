MIN_YEAR = 1900
MAX_YEAR = 2050

WEEK_DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        if year < MIN_YEAR or year > MAX_YEAR:
            year = MIN_YEAR
        if month < 1 or month > 12:
            month = 1
        days_in_month = self.days_in_month(month, year)
        if day < 1 or day > days_in_month:
            day = 1

        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def days_in_month(self, month, year) -> int:
        if month == 2 and self.is_leap_year():
            return 29
        elif month == 2:
            return 28
        elif month in (4, 6, 9, 11):
            return 30
        else:
            return 31

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        return True

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        delta = self.delta_days()
        return (delta + 1) % 7

    def is_weekend(self) -> bool:
        return True

    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day}/{self.month}/{self.year}"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        weekday = WEEK_DAYS[self.weekday()]
        month = MONTH_NAMES[self.month - 1]
        return f"{weekday} {self.day} de {month} de {self.year}"

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


date = Date(1, 1, 1900)
print("Año biciesto: ", date.is_leap_year())
print("Día de la semana: ", date.weekday())
print("Método str: ", date.__str__())
