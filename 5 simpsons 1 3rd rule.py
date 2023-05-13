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

print("X = ", x)
print("Y = ", y)

if (((len(x)-1) % 2) == 0):
    ans = (h/3) * ((y[0]+y[-1]) + (2 * sum(y[2:-1:2])) + (4 * sum(y[1:-1:2])))
    print("Ans = ", ans)
else:
    print("simpsons 1/3rd rule can not be applied")
