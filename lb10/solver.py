from numpy import abs


def solver(x, y, f):
    if x <= 0 or y <= 0:
        print("x or y should be > 0")
    else:
        if x <= y:
            f = abs(x - y)
        elif x > y:
            f = (1 + x) * y
        binary = '{0:b}'.format(f)
    return binary
