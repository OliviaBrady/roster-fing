from ics import Calendar, Event
from datetime import datetime
from dateutil import tz

c = Calendar()



def to_utc(date_string):

    """ ics format wants utc strings, this will convert to UTC timezone """

    date_format = '%Y-%m-%d %H:%M:%S'

    time_dt = datetime.strptime(date_string, date_format).replace(tzinfo=tz.gettz('Australia/Sydney'))
    time_dt = time_dt.astimezone(tz.tzutc())



with open('Example Roster.html', 'r') as my_file:
    lines = my_file.readlines()

    for line in lines:
        if 'li data-role="list-divider"' in line:
            day, mth, year = line.split('>')[1].split('-')[0].split(' ')[1].split('/')

            e = Event()
            e.name = "Shift"
            time = f"{year}-{mth}-{day} 07:00:00"
            e.begin = to_utc(time)
            e.duration = {'hours':12}
            c.events.add(e)

with open('night-shift.ics', 'w') as my_file:
    my_file.writelines(c)