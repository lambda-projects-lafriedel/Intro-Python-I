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
date = sys.argv

cal = calendar.TextCalendar()

month = datetime.today().month
year = datetime.today().year

# If no input, print cal of current month
if len(date) == 1:
    pass

# If only month, render that month's calendar
elif len(date) == 2:
    month = int(date[1])

# If month and year, render the calendar for that month in that year
elif len(date) == 3:
    month = int(date[1])
    year = int(date[2])

# Else, print directions for giving proper input
else:
    print("Please enter [month] [year] as numerical values.")
    exit()

cal.prmonth(year, month)