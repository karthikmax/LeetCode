#Sum of whole numbers from 1 through N (both inclusive). Do not include numbers divisible by 3 or 7

import sys
import numpy as np
import pandas as pd
import logging

numbers = list()

def sumIntegers(num):
    sum = 0
    for i in range(1,num+1):
      if (i%3 == 0 or i%7 == 0):
        pass
      else:
        sum += i
    return sum

try:
  while True:
    usr_input = input()
    if usr_input != "":
        numbers.append(int(usr_input))
    else:
        break

except EOFError:
  pass    

for num in numbers:
    val_sum = sumIntegers(num)
    print(val_sum)
