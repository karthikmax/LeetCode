
#Adjacency Matrix

import sys
import numpy as np
import pandas as pd

master_list = list()
try:
  while True:
      values = input()
      if values != '':
        values = list(map(int,values.split(' ')))
        master_list.append(values)
      else:
        break

except EOFError:
    pass

master_list_combined = list()
for lst in master_list:
    master_list_combined = master_list_combined + lst

#lets get max of all lists to identify our matrix size
array_max = max(master_list_combined)

#create an array of size arraymax x array_max with 0s
array = [[0 for j in range(array_max + 1)] for i in range(array_max + 1)]

for lst in master_list:
  row_element = lst[0]
  for col_element in lst[1:]:
    array[row_element][col_element] = 1

for arrlst in array:
  #print(*) is used to print all items of the list
  print(*arrlst,sep=' ')
