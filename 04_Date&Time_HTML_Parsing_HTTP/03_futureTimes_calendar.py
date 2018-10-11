#!/usr/bin/env python3

# Calculating future times
from datetime import datetime, timedelta

now = datetime.now()

testDate = now + timedelta(days=2) # 2 days from now
treeWeeksAgo = now - timedelta(weeks=3)

print(testDate.date()) # it's a datetime instance
print(treeWeeksAgo.date())

if testDate > treeWeeksAgo:
    print('Comparison works')

# Using calendar library
import calendar

cal = calendar.month(2001,10)  # October 2001
print(cal)

cal2 = calendar.weekday(2001, 10, 11)  # What's 11 weekday
print(cal2)

# leap year/bissextile year
print(calendar.isleap(1999))
print(calendar.isleap(2000))