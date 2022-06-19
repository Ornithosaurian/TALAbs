from numpy import abs

x = int(input("Input x= "))
y = int(input("Input y= "))
f = 0


def solver(x, y, f):
    if x <= 0 or y <= 0:
        print("x or y should be > 0")
    else:
        if x <= y:
            f = abs(x - y)
        elif x > y:
            f = (1 + x) * y
        print(f)
    return f

solver(x, y, f)


def toBinary(f):
    binary = '{0:b}'.format(f)
    print(binary)


toBinary(solver(x,y,f))

