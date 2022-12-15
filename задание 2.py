def f1(x, y, f2):
    f = f2(x, y)
    print("f = ", f)
def f2(x, y): return x + y
x = int(input())
y = int(input())
f1(x, y, f2)