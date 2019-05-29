"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Get user input of month/month and year
l = len(sys.argv)
d = sys.argv
print(d)

c = calendar.TextCalendar()
current = datetime.now()

# If no input, print cal of current month
if l <= 1:
    current_cal = c.formatmonth(current.year, current.month)
    print(current_cal)

# If only month, render that month's calendar
if l == 2:
    month = d.pop(1)
    print(list(calendar.month_abbr))
    #month_cal = c.formatmonth(current.year, month)
    #print(month_cal)

# If month and year, render the calendar for that month in that year

# Else, print directions for giving proper input