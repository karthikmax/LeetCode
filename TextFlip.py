#Text flip - print space separated text in separate line with letter reversed and maintaining the cases= of each letter

import sys
import numpy as np
import pandas as pd

txt = input()
txt_split = txt[::-1].split(' ')
txt_split_ordered = txt_split[::-1]
for ts in txt_split_ordered:
    print(ts)
