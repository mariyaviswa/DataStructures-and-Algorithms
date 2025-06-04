"""
Find the nth fibonacci number using recursion
---------------------------------------------
Multiple Recursion calls
"""


def fibo(n):
    if n <= 1:
        return n
    last = fibo(n - 1)
    secondLast = fibo(n - 2)
    return last + secondLast


ans = fibo(6)
print("6th fibonacci number: ", ans)