#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Last_digit = abs(number) % 10
if Last_digit > 5:
    comparison = 'greater than 5'
elif Last_digit == 0:
      comparison = '0'
else:
     comparison = 'less than 6 and not 0'
     print('last_digit of {} is {} and is {}'.format(number, Last_digit, comparison))
