def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
n=7
print(fib(n))