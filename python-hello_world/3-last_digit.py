#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
     last_digit = - last_digit

if last_digit > 5:
    comparison = 'greater than 5'
    print('Last digit of {} is {} and is {}'.format(number, last_digit, comparison))

elif last_digit == 0:
      comparison = '0'
      print('Last digit of {} is {} and is {}'.format(number, last_digit, comparison))
else:
     comparison = 'less than 6 and not 0'
     print('Last digit of {} is {} and is {}'.format(number, last_digit, comparison))
