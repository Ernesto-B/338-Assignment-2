"""
Creators: Ernesto Barreto, Reese Sanchez
Date: 
338 Assignment 2
"""

import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    median_index = (start + end) // 2
    array[start], array[median_index] = array[median_index], array[start]
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def sort(array):
    func1(array, 0, len(array) - 1)

with open('ex2.json', 'r') as f:
    data = json.load(f)

start_timer = time.time()
sort(data)
end_timer = time.time()

#print("The sorted array is: ", data)

#Bruh idk how to plot this
time_taken = (end_timer - start_timer) * 10 ** 12
plt.plot([0, 1], [0, time_taken], 'ro')
plt.xlabel('Iteration')
plt.ylabel('Time Taken (ps)')
plt.title('Sorting Time')
plt.show()