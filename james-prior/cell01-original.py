import itertools
import datetime
import calendar

def find_december_monday(currentYear):
    month = 12
    dates = []

    for year in range(currentYear, 2008, -1):
        day = 1
    
        if calendar.weekday(year, month, day) == calendar.MONDAY:
            day += 7
            dates.append(str(year) + '/' + str(month) + '/' + str(day)) 
        elif calendar.weekday(year, month, day + 1) == calendar.MONDAY:
            day += 8
            dates.append(str(year) + '/' + str(month) + '/' + str(day))
        else:
            for day in range(3, 8):
                if calendar.weekday(year, month, day) == calendar.MONDAY:
                    dates.append(str(year) + '/' + str(month) + '/' + str(day))

    return dates
