#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    comparison = 'greater than 5'
elif last_digit == 0:
      comparison = '0'
else:
     comparison = 'less than 6 and not 0'
     print('Last digit of {} is {} and is {}'.format(number, last_digit, comparison))
