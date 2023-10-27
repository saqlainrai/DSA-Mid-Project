
from algorithms import *

with open("array.csv", 'r') as file:
    data = file.read()
    array = data.split(',')
    for i in range(len(array)):
        array[i] = int(array[i])

array = counting_sort(array)

for i in array:
    print(i)