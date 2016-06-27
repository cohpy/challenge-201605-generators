%%script diff_python
# The time increment we want is simple,
# and since we will be staying within a month,
# we can eliminate the datetime.timedelta() stuff.

import datetime
from itertools import islice, count

FIRST_MEETING_DATE = datetime.date(2009, 9, 28)

N_INVALID_DECEMBER_MEETING_DAYS = 2
EARLIEST_VALID_DECEMBER_DATE = N_INVALID_DECEMBER_MEETING_DAYS + 1

DECEMBER = 12
MONDAY = 0  # per date.weekday()

def get_formatted_reversed_december_meeting_dates(last_year):
    return list(
        '{0.year}/{0.month}/{0.day}'.format(date)
        for date in (
        list(islice(filter(
        lambda date: date.weekday() == MONDAY,
        (datetime.date(year, DECEMBER, EARLIEST_VALID_DECEMBER_DATE + i)
        for i in count())),
        1))[0]
        for year in reversed(range(FIRST_MEETING_DATE.year, last_year + 1))))

this_year = datetime.date.today().year
assert (
    repr(get_formatted_reversed_december_meeting_dates(this_year)) ==
    open('joe_style_good_output').read())
