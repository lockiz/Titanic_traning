import calendar
from datetime import date


def get_free_museum_dates(year):
    """

    Вычисляет даты бесплатного посещения музея по заданному году

    Аргументы:
        year - год (int)

    """

    for month in range(1, 13):
        dates_month = calendar.monthcalendar(year, month)
        if dates_month[0][calendar.THURSDAY]:
            print(date(year, month, dates_month[2][calendar.THURSDAY]).strftime('%d.%m.%Y'))
        else:
            print(date(year, month, dates_month[3][calendar.THURSDAY]).strftime('%d.%m.%Y'))


get_free_museum_dates(int(input()))
