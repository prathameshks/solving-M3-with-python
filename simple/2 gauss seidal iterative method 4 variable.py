# Written by: Github Copilot & Prathamesh Sable
val = []
n = int(input("Number of Variables:"))
for i in range(n):
    eq = []
    for j in range(n+1):
        eq.append(float(input(f"Enter coeff eq:{i}, var: {j} :")))
    val.append(eq)

acu = int(input("Enter the accuracy: "))


def gauss_seidal(vars, itr):
    ans = [0 for i in range(n)]
    for i in range(n):
        temp = val[i][n] - sum([val[i][j] * vars[j]
                               for j in range(n) if j != i])
        ans[i] = temp / val[i][i]
        print(f"x{i}^{itr} = ",
              f"({val[i][n]} - ({sum([val[i][j] * vars[j] for j in range(n) if j != i])})) / {val[i][i]}")
        print(f"x{i}^{itr} = ", round(ans[i], acu))

    return ans


vars = [0 for i in range(n)]
i = 1
while (input("Do you want to continue? (y/n) ") != "n"):
    print("Iteration ", i)
    vars = gauss_seidal(vars, i)
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
6
15
2
72
1
1
54
110

"""
