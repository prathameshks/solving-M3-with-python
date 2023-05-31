# YOU NEED TO SET FUNCTION f(x) MANUALLY

import math
a = float(input("Enter a:"))
b = float(input("Enter b:"))
h = float(input("Enter Value of h:"))
acu = int(input("Enter accuracy:"))


def f(x):
    y = (x**3 - 4*x - 9)
    return y


if (f(a) < 0):
    reverse = 0
else:
    reverse = 1


def bisect(x, var, itr):
    mid = (x+var)/2
    f_mid = f(mid)
    print(f"x{itr} = ", round(mid, acu))
    print(f"f(x{itr}) = ", round(f_mid, acu))
    if (f_mid == 0):
        return (mid, 0)
    elif (f_mid < 0):
        if (reverse):
            return (mid, 1)
        else:
            return (mid, -1)
    else:
        if (reverse):
            return (mid, -1)
        else:
            return (mid, 1)


i = 1
while (input("Do you want to continue? (y/n) ") != "n"):
    print("Iteration ", i)
    mid, res = bisect(a, b, i)
    if (res == 0):
        print("x is ", round(mid, acu))
        break
    elif (res == -1):
        a = mid
    else:
        b = mid
    i += 1

"""
10
1
-1
11.19
1
10
1
28.08
-1
1
10
35.61
"""
