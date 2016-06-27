%%script diff_python
# DAYS_PER_WEEK is not used, so get rid of it.
# (Don't stop at the one bug.)

import datetime

FIRST_MEETING_DATE = datetime.date(2009, 9, 28)

N_INVALID_DECEMBER_MEETING_DAYS = 2
EARLIEST_VALID_DECEMBER_DATE = N_INVALID_DECEMBER_MEETING_DAYS + 1

DECEMBER = 12
MONDAY = 0  # per date.weekday()

def format_date(date):
    return '{0.year}/{0.month}/{0.day}'.format(date)

def iter_date(date, increment=datetime.timedelta(days=1)):
    while True:
        yield date;
        date += increment

def get_december_meeting_date(year):
    start_date = datetime.date(year, DECEMBER, EARLIEST_VALID_DECEMBER_DATE)
    for date in iter_date(start_date):
        if date.weekday() == MONDAY:
            return date

def get_december_meeting_dates(years):
    return (
        get_december_meeting_date(year)
        for year in years
    )

def get_formatted_december_meeting_dates(years):
    return (
        format_date(date)
        for date in get_december_meeting_dates(years)
    )

def get_formatted_reversed_december_meeting_dates(last_year):
    years = reversed(range(FIRST_MEETING_DATE.year, last_year + 1))
    return list(get_formatted_december_meeting_dates(years))

this_year = datetime.date.today().year
assert (
    repr(get_formatted_reversed_december_meeting_dates(this_year)) ==
    open('joe_style_good_output').read())
