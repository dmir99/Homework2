# Daniyal Mir PSID:1614263
from datetime import datetime


def conv_date(user_date):
    date_object = datetime.strptime(user_date, '%B %d, %Y')
    new_date = date_object.strftime('%-m/%-d/%Y')
    return new_date


the_dates = []
user_date = str(input("Please enter a date: "))

while user_date != "-1":
    try:
        new_date = conv_date(user_date)
        the_dates.append(new_date)
    except:
        pass
    user_date = str(input("Please enter a date: "))

i = 0
for i in the_dates:
    print(i)
