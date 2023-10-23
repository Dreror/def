def add(x, y):
    return x + y


def dis(x, y):
    return x - y


def mul(x, y):
    return x * y


def dell(x, y):
    return x / y


def sqr(x, y):
    return x ** y


def qua(x):
    return x ** 2


def qb(x):
    return x ** 3


print("Вас вітає калькулятор!")
a = 1
while a in range(0, 8):
    print("Доступні функції:",
          "1 - додавання",
          "2 - віднімання",
          "3 - множення",
          "4 - ділення",
          "5 - взведення в ступінь",
          "6 - зведення до квадрата",
          "7 - зведення до куба",
          "0 - Вийти", sep="\n")
    a = int(input("Що бажаете зробити? = "))
    while a not in range(0, 8):
        print("Невірне значення! Спробуйте ще раз")
        a = int(input("Що бажаете зробити? = "))
    if a == 0:
        print("Допобачення!")
        break
    if a <= 5:
        print("Чудово! Введіть числo/а")
        x1 = int(input("Num1= "))
        y1 = int(input("Num2= "))
        if a == 1:
            print(add(x1, y1))
        elif a == 2:
            print(dis(x1, y1))
        elif a == 3:
            print(mul(x1, y1))
        elif a == 4:
            if y1 == 0:
                print("Не можна ділити на ноль!")
            else:
                print(dell(x1, y1))
        elif a == 5:
            print(sqr(x1, y1))
    elif 5 < a < 8:
        print("Чудово! Введіть числo/а")
        x1 = int(input("Num1= "))
        if a == 6:
            print(qua(x1))
        elif a == 7:
            print(qb(x1))

