def are(a, b, c):
    x = a + b + c
    return x / 3


q = 1
while q == 1:
    print("0 - Вийти",
          "1 - Порахувати арефметичне", sep="\n")
    q = int(input("Що хочете зробити? = "))
    if q == 0:
        print("Допобачення!")
        break
    else:
        print("Введіть числа для обчислення")
        a1 = int(input("Num1= "))
        b1 = int(input("Num2= "))
        c1 = int(input("Num3= "))
        print(f"Середне арефметичне = {are(a1, b1, c1)}")
