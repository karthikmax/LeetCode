#find duplicate entry
#get n and a series of n numbers (separated by comma). n and numbers should be separated by semi-colon


import sys

entry = input()
n = int(entry.split(';')[0])
val = list(map(int,entry.split(';')[1].split(',')))

res = list()

for i in val:
    cnt = val.count(i)
    if cnt > 1:
        if res.count(i) == 0:
            res.append(i)

print(res)