import math
import csv 
import pandas as pd
import plotly.express as px
with open('data.csv',newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# FINDING MEAN
def MEAN(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    return mean


#SQUARING AND GETTING THE VALUES

square_list = []
for number in data:
    a = int(number)-MEAN(data)
    a = a**2
    square_list.append(a)

# GETTING THE SUM

sum = 0
for i in square_list:
    sum = sum+i

# DIVIDING THE SUM BY THE TOTAL VALUES
result = sum/(len(data)-1)

# GETTING THE DEVIATION BY TAKING SQUARE ROOT OF THE RESULT
standard_deviation = math.sqrt(result)
print(standard_deviation)
    