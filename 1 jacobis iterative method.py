a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
d1 = float(input("Enter d1: "))
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))
d2 = float(input("Enter d2: "))
a3 = float(input("Enter a3: "))
b3 = float(input("Enter b3: "))
c3 = float(input("Enter c3: "))
d3 = float(input("Enter d3: "))
acu = int(input("Enter the accuracy: "))

def jacobis(x0, y0, z0, itr):
    for i in range(100):
        x1 = (d1 - (b1 * y0) - (c1 * z0)) / a1
        y1 = (d2 - (a2 * x0) - (c2 * z0)) / b2
        z1 = (d3 - (a3 * x0) - (b3 * y0)) / c3
    print(f"x{itr} = ", round(x1, acu))
    print(f"y{itr} = ", round(y1, acu))
    print(f"z{itr} = ", round(z1, acu))
    return (x1, y1, z1)

x1 = y1 = z1 = 0
i = 1
while (input("Do you want to continue? (y/n) ") != "n"):
    print("Iteration ", i)
    x1, y1, z1 = jacobis(x1, y1, z1, i)
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
