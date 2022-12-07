#!/usr/bin/python3

def sum_all(*args):
  sum = 0
  for num in args:
    if type(num) is list:
      sum += sum_all(*num)
    else:
      sum += int(num)
  return sum
