# YOU NEED TO SET FUNCTION f(x) MANUALLY

a = float(input("Enter a:"))
b = float(input("Enter b:"))
acu = int(input("Enter accuracy:"))

def f(x):
    y = (2*x**3 + x**2 - 20*x + 12)
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

def equate(old_val, new_val):
    return (round(old_val, acu) == round(new_val, acu))

itr,mid = 1, 0

while (True):
    old_mid = mid
    print("Iteration ", itr)
    mid, res = bisect(a, b, itr)
    if (equate(old_mid,mid)):
        break
    elif (res == -1):
        a = mid
    else:
        b = mid
    if (itr % 10 == 0):
        print(f"Completed {itr} iterations.")
        ch = input("Do you want to continue(n/N to cancel):")
        if (ch == 'n' or ch == "N"):
            break
    itr += 1

print('-'*20)
print("X is ", round(mid, acu))
print('-'*20)