#!/usr/bin/python

import sys

cron_input = sys.argv[1].split()

all_time_units = {
        'minute': [i for i in range(60)],
        'hour': [i for i in range(24)],
        'day_of_week': [i for i in range(1, 8)],
        'day_of_month': [i for i in range(1, 32)],
        'month': [i for i in range(1, 13)]
    }

def format_string(time_string, time_unit):
    if time_string == "*":
        return map(str, all_time_units[time_unit])
    if "," in time_string:
        result = get_days_list(time_string, time_unit)
        return result
    if "/" in time_string:
        result = get_minutes(time_string, time_unit)
        return result
    
    if "-" in time_string:
        result = get_days_week_months(time_string, time_unit)
        return result

    return time_string


def get_minutes(time_string, time_unit):
    time_string = time_string.split("/")
    numerator = time_string[0]
    denominator = int(time_string[1])
    if numerator == "*":
        return map(str, [i for i in all_time_units[time_unit]
                if i % denominator == 0])
    else:
        return map(str, [i for i in range(0, int(numerator), denominator)])
            
def get_days_list(time_string, time_unit):
    time_list = time_string.split(",")
    return time_list

def get_days_week_months(time_string, time_unit):
    time_string = time_string.split("-")
    try:
        start = int(time_string[0])
        end = int(time_string[1])
        start, end = all_time_units[time_unit].index(start), all_time_units[time_unit].index(end)
        return map(str, all_time_units[time_unit][start:end + 1])
    except ValueError:
        raise Exception('Incorrect or invalid range for {}'.format(time_unit))


minute = format_string(cron_input[0], "minute")
hour = format_string(cron_input[1], "hour")
day_of_month = format_string(cron_input[2], "day_of_month")
month = format_string(cron_input[3], "month")
day_of_week = format_string(cron_input[4], "day_of_week")
command = cron_input[5]


table_data = [["minute", ' '.join(minute)], ["hour", ' '.join(hour)], ["day of month", ' '.join(day_of_month)],
                ["month", ' '.join(month)], ["day of week", ' '.join(day_of_week)], ["command", command]]

for row in table_data:
    print("{: <14} {: <}".format(*row))