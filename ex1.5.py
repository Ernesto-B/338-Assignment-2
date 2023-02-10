"""
Creators: Ernesto Barreto, Reese Sanchez
Date: 
338 Assignment 2
"""
import time

def fib_memo(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)   

# starting timer
start_time1 = time.perf_counter()
# running program with memoization
print([fib_memo(i) for i in range(35)])
# stopping timer
end_time1 = time.perf_counter()

# starting timer
start_time2 = time.perf_counter()
# running program with memoization
print([func(i) for i in range(35)])
# stopping timer
end_time2 = time.perf_counter()


print(f"It took", end_time1 - start_time1 ," seconds for the program to calculate the first 35 numbers in the Fibonacci Sequence with memoization")

print(f"It took", end_time2 - start_time2," seconds for the program to calculate the first 35 numbers in the Fibonacci Sequence without memoization")