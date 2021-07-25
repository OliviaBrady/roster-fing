from ics import Calendar, Event
from datetime import datetime, timedelta
from dateutil import tz

c = Calendar()



def to_utc(date_string):

    """ ics format wants utc strings, this will convert to UTC timezone """

    date_format = '%Y-%m-%d %H:%M:%S'

    time_dt = datetime.strptime(date_string, date_format).replace(tzinfo=tz.gettz('Australia/Sydney'))
    time_dt = time_dt.astimezone(tz.tzutc())

    return time_dt


with open('Example Roster.html', 'r') as my_file:
    lines = my_file.readlines()

    dates = []
    start_times = []

    for line in lines:

        if 'li data-role="list-divider"' in line:
            day, mth, year = line.split('>')[1].split('-')[0].split(' ')[1].split('/')

            date = (day, mth, year)
            dates.append(date)

        elif '19:00 - 07:30' in line:
            start_times.append('19:00:00')

        elif '07:00 - 19:30' in line:
            start_times.append('07:00:00')

    for date, start_time in zip(dates, start_times):

        day, mth, year = date

        e = Event()
        e.name = "Night Shift" if start_time == "19:00:00" else "Day Shift"
        time = f"{year}-{mth}-{day} {start_time}"
        e.begin = to_utc(time)
        e.duration = {"hours" : 12, "minutes" : 30}
        c.events.add(e)

with open('Rosters/roster_julyaug.ics', 'w') as my_file:
    my_file.writelines(c)

print('completed successfully')