month = ["Январь", "Февраль", "Март", "Апрель", 
         "Май", "Июнь", "Июль", "Август", 
         "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
         ]


def month_to_season(month):
    if month in [12, 1, 2]:
        return print("Зима")
    elif month in [3, 4, 5]:
        return print("Весна")
    elif month in [6, 7, 8]:
        return print("Лето")
    elif month in [9, 10, 11]:
        return print("Осень")
    else:
        return "Неверный номер месяца"


month_to_season(5)
