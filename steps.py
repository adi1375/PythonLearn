def steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return steps(n - 3) + steps(n - 2) + steps(n - 1)
