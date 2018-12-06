from datetime import datetime, timedelta, date


yesterday = date.today() - timedelta(days=1)
today = date.today()
# Месяц назад довольно абстрактное понятие. Взяла примерно 30 дней в неделях.
month_ago = date.today() - timedelta(weeks=4.3)
datetime_object = datetime.strptime('01/01/17 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')
print("Yesterday:", yesterday)
print("Today:", today)
print("Month ago:", month_ago)
print(type(datetime_object))
