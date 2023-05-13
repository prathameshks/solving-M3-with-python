a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
u = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

b = [0, 0, 0]
v = [0, 0, 0]
ans = [0, 0, 0]

for i in range(3):
    for j in range(3):
        a[i][j] = float(input(f"Enter a{i+1}{j+1}: "))
        if i == j:
            l[i][j] = 1
        if i < j:
            u[i][j] = 0
        if i > j:
            l[i][j] = 0

for i in range(3):
    b[i] = float(input(f"Enter b{i+1}:"))

for i in range(3):
    for j in range(3):
        if (i <= j):
            sum = 0
            for k in range(i):  # for u
                sum += l[i][k]*u[k][j]
            u[i][j] = round(a[i][j] - sum, 3)
        else:
            sum = 0
            for k in range(j):  # for l
                sum += l[i][k]*u[k][j]
            l[i][j] = round((a[i][j] - sum)/u[j][j], 3)

# for U*X = V and LV = A
for i in range(3):
    sum = 0
    for j in range(3):
        sum += l[i][j]*v[j]
    v[i] = b[i]-sum

# for UX = V
for i in range(2, -1, -1):
    sum = 0
    for j in range(3):
        sum += u[i][j]*ans[j]
    ans[i] = (v[i]-sum)/u[i][i]


def print_matrix(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j], " "*(6-len(str(a[i][j]))), end=" ")


print("A = ")
print_matrix(a)
print("L = ")
print_matrix(l)
print("U = ")
print_matrix(u)

print("V = ", v)

print("X = ", ans)


"""
3
2
7
2
3 
1
3
4
1
"""
