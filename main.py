import calendar
from datetime import date


def get_free_museum_dates(year):
    """

    Вычисляет даты бесплатного посещения музея по заданному году

    Аргументы:
        year - год (int)

    """
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        if cal[0].index(1) <= 3:
            print(date(year, month, cal[0][3] + 14).strftime('%d.%m.%Y'))
        elif cal[0].index(1) >= 4:
            print(date(year, month, cal[1][3] + 14).strftime('%d.%m.%Y'))
        else:
            print(date(year, month, cal[1][3] + 8).strftime('%d.%m.%Y'))


get_free_museum_dates(int(input()))


#  Хотел оставить тут комментарий


def get_my_input(inp):
    """ Возвращаем новое * 2 значение из ввода """
    return inp * 2


print(get_my_input(int(input())))

