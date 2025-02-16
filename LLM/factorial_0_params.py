def factorial_0(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_0(n - 1)