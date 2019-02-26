# 0, 1, 1, 2, 3, 5, 8


def fib_iter(n):
    a, b = 0,1
    for i in range(n):
        a,b = b, a + b

    return a


print(fib_iter(10))


def fib_rec(n):
    # Base Case
    if n==0 or n==1:
        return n

    # Recursive Case
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(10))


cache = {}

def fib_dyn(n):
    if n==0 or n==1:
        return n

    if n not in cache:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

print(fib_dyn(10))
