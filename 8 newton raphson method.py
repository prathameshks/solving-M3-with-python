def f(x):
    return 3*x**3 - 9*x**2 + 8


def df(x):
    return 9*x**2 - 18*x


def xn(xn_1):
    if (xn_1 == 0):
        return 1
    return xn_1 - f(xn_1)/df(xn_1)


def equate(old_val, new_val):
    return (round(old_val, acu) == round(new_val, acu))


acu = int(input("Enter Accuracy: "))
x0 = int(input("Enter X0: "))

x1 = xn(x0)

while (not equate(x0, x1)):
    x0 = x1
    x1 = xn(x0)

print("Root is ", round(x1, acu))
