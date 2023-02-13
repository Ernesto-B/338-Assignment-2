"""
Creators: Ernesto Barreto, Reese Sanchez
Date: 
338 Assignment 2
"""

import sys
import json
import time
import matplotlib.pyplot as plt

sortTime = []
xLabels = ["Array 1", "Array 2", "Array 3", "Array 4", "Array 5", "Array 6", "Array 7", "Array 8", "Array 9", "Array 10", "Array 11", "Array 12", "Array 13"]

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    start_timer1 = time.perf_counter()
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    end_timer1 = time.perf_counter()
    sortTime.append(end_timer1-start_timer1)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2.5.json', 'r') as f:
    data = json.load(f)

start_timer = time.perf_counter()
func1(data, 0, len(data) - 1)
end_timer = time.perf_counter()

#print("The sorted array is: ", data)
print("Time taken: ", format((end_timer - start_timer) * 1000, '.40f'), "seconds") # Not sure if this is the correct way to calculate time

time_taken = (end_timer - start_timer) * 10 ** 12
plt.bar(xLabels, sortTime)
plt.xlabel('Iteration')
plt.ylabel('Time Taken (ps)')
plt.title('Sorting Time')
plt.show()