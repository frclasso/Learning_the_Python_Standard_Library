#!/usr/bin/env python3

from datetime import datetime

now = datetime.now()

print(f'Now: {now}')
print(f'Date: {now.date()}')
print(f'Year: {now.year}')
print(f'Month: {now.month}')
print(f'Day:{now.day}')
print(f'Hour: {now.hour}')
print(f'Minute: {now.minute}')
print(f'Seconds:{now.second}')

print(f'Time: {now.time()}')
