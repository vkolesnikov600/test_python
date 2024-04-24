def is_year_leap(year):
    leap_year = year % 4 == 0
    print(f"Год {year}: {leap_year}")
    return leap_year


result = is_year_leap(2024)