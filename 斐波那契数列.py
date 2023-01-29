def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def f2(n):
    num = [1, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    for i in range(2, n + 1):
        num.append(num[i - 1] + num[i - 2])
    return num[n - 1]
