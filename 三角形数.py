def t(n):
    if n == 1:
        return 1
    return n * n - t(n - 1)


def t2(n):
    return n * (n + 1) / 2
