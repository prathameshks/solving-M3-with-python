n = int(input("Enter Number of Variables:"))
a = []
b = []
print("Equation Format is - ax + by + cz + ... = d")

for i in range(n):
    temp = []
    for j in range(n):
        x = float(input(f"Enter Eq{i+1}'s {j+1} coefficient: "))
        temp.append(x)
    d = float(input(f"Enter d{i+1}: "))
    a.append(temp)
    b.append(d)

acu = int(input("Enter the accuracy: "))


def equate(old_val, new_val):
    for i in range(n-1):
        if (round(old_val[i], acu) != round(new_val[i], acu)):
            return False
    return True
    


def gauss_seidal(old_vals):
    new_val = old_vals.copy()
    for i in range(n):
        val = b[i]
        for j in range(n):
            val -= a[i][j]*new_val[j]
        val += a[i][i]*new_val[i]
        val /= a[i][i]
        new_val[i] = val
    return new_val


itr = 1
cont = True
vals = [0 for i in range(n)]
while (cont):
    old_vals = vals.copy()
    vals = gauss_seidal(old_vals)
    print("Iteration ", itr)
    print(vals)
    if (itr % 10 == 0):
        print(f"Completed {itr} iterations.")
        ch = input("Do you want to continue(n/N to cancel):")
        if (ch == 'n' or ch == "N"):
            break
    cont = not equate(old_vals, vals)
    itr += 1

print('-'*20)
print("solution is ")
for i in range(n):
    print(f"var {i+1} = ", round(vals[i], acu))
print('-'*20)

"""
3
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
5
"""

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
6
15
2
72
1
1
54
110

"""

"""
3
27
6
-1
85
6
15
2
72
1
1
54
110
"""