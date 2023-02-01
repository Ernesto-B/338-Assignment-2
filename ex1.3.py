"""
Creators: Ernesto Barreto, Reese Sanchez
Date: 
338 Assignment 2
"""

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

print([fib_memo(i) for i in range(10)])
