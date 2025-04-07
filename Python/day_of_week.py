# Exercise: Given a single line of input containing space-separated month, day, and year,
# determine and print the day of the week for the given date in uppercase using the calendar module.

import calendar

# Read month, day, and year from input (space-separated)
month, day, year = map(int, input().split())

# Get the weekday as an integer (Monday=0, Sunday=6) for the given date.
day_int = calendar.weekday(year, month, day)

# Create a list of day names from the calendar module.
day_names = list(calendar.day_name)

# Print the day name corresponding to day_int in uppercase.
print(day_names[day_int].upper())
