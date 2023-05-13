# YOU NEED TO SET FUNCTION f(x) MANUALLY

import math
l_lim = float(input("Enter Lower Limit:"))
u_lim = float(input("Enter Upper Limit:"))
h = float(input("Enter Value of h:"))


def f(x):
    y = (math.e ** x)/(1+x)
    return y


x = []
y = []

cal_x = l_lim
cal_y = f(l_lim)
x.append(cal_x)
y.append(cal_y)
while (cal_x < u_lim):
    cal_x += h
    cal_y = f(cal_x)
    x.append(round(cal_x, 3))
    y.append(round(cal_y, 3))

print(x)
print(y)

ans = (h/2) * ((y[0]+y[-1]) + (2 * sum(y[1:-1])))
print(ans)
