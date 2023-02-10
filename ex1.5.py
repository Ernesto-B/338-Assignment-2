"""
Creators: Ernesto Barreto, Reese Sanchez
Date: 
338 Assignment 2
"""
import timeit

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

fibMemoLoop35 = timeit.timeit(lambda: fib_memo(35), number=35)

fibLoop35 = timeit.timeit(lambda: func(35), number=35)

print(f"It took {fibMemoLoop35} seconds for the program to calculate the first 35 numbers in the Fibonacci Sequence with memoization")

print(f"It took {fibLoop35} seconds for the program to calculate the first 35 numbers in the Fibonacci Sequence without memoization")