def fib(n):
    if n <= 2:
        return (n,1)
    else:
        (a, b) = fib(n - 1)
        return [a + b,  a]

a = fib(995)
print(a)