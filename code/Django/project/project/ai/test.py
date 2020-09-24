import pandas as pd
import csv
import os

# data = pd.read_csv('./func/datasets/filename.csv')

f = open('./func/datasets/filename.csv', 'r')
rdr = csv.reader(f)
text = '화재'
count = 0
for list in rdr:
    # if list[6] == text and list[1] == '1' and list[3] == '정면':
    #     print(list[5][:-3] + "avi")
    if list[1] == '1' and list[3] == '정면':
        count += 1

print(count)

# print(data)