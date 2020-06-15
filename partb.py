# Daniyal Mir 1614263
from datetime import datetime

f = open("inputDates.txt")


def conv_date(user_date):
    date_object = datetime.strptime(user_date, '%B %d, %Y')
    new_date = date_object.strftime('%-m/%-d/%Y')
    return new_date


the_dates = []

for line in f:
    line = line.strip( )
    try:
        new_date = conv_date(line)
        the_dates.append(new_date)
    except:
        pass


i = 0
for i in the_dates:
    print(i)

f.close()
