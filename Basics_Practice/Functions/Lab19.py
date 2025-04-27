# *args and **args

def f1(a=1, b=4, c=6):
    return a + b + c


f1()
f1(1)
f1(a=1, b=4)
f1(c=6, a=1, b=4)
f1(a=68)
r = f1(c=1, b=56, a=87)
print(r)
print(f1)
