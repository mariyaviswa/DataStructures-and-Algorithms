import time


def factorial(n):
    # Base case
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = int(input())
st = time.time()
res = factorial(num)
ed = time.time()
print(f"{num} factorial is: ", res)
print("Execution Time: ", ed - st)
