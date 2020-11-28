import datetime


def getPreviousDate():
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today-one_day
    return yesterday


print(getPreviousDate())
