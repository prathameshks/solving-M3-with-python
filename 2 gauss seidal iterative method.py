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

def gauss_seidal(x, y, z, itr):
    x = (d1 - (b1 * y) - (c1 * z)) / a1
    y = (d2 - (a2 * x) - (c2 * z)) / b2
    z = (d3 - (a3 * x) - (b3 * y)) / c3
    print(f"x{itr} = ", round(x, acu))
    print(f"y{itr} = ", round(y, acu))
    print(f"z{itr} = ", round(z, acu))
    return (x, y, z)

x = y = z = 0
i = 1
while (input("Do you want to continue? (y/n) ") != "n"):
    print("Iteration ", i)
    x, y, z = gauss_seidal(x, y, z, i)
    i += 1

"""
20
1
-2
17
3
20
-1
-18
2
-3
20
25

27
6
-1
85
1
1
54
110
6
15
2
72
"""
