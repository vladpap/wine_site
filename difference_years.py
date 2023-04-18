from datetime import date


def get_difference_years_rus(years):

    year_difference = date.today().year - years

    years_rus = ""
    if year_difference == 1:
        years_rus = "год"
    elif year_difference >= 2 and year_difference < 5:
        years_rus = "года"
    elif year_difference >= 5 and year_difference < 100:
        years_rus = "лет"
    elif year_difference == 101:
        years_rus = "год"
    elif year_difference >= 2 and year_difference < 105:
        years_rus = "года"
    else:
        years_rus = "лет"

    return "{0} {1}".format(str(year_difference), years_rus)


if __name__ == "__main__":
    print(get_difference_years_rus(1920))
