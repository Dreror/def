def num1(x, y):
    return x - y


def num2(x, y):
    return x + y


x1 = int(input("x= "))
y1 = int(input("y= "))


print(num1(x1, y1))
print(num2(x1, y1))

x2 = num1(x1, y1)
y2 = num2(x1, y1)
b = []
for a in range(x2, y2 * 2):
    a = a / 2
    b.append(a)
print(b)
