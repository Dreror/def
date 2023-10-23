def indx(a, b):
    return a / b ** 2


q = ["on"]
while q.count("on"):
    a1 = float(input("Введіть свою вагу= "))
    b1 = float(input("Введіть свій зріст в МЕТРАХ= "))
    x = indx(a1, b1)
    if 18.5 < x < 24.9:
        print(f"{round(x, 2)} - маса тіла в нормі")
    elif x < 18.5:
        print(f"{round(x, 2)} - недостатня вага")
    elif x > 25:
        print(f"{round(x, 2)} - слідкуйте за фігурою")
    print("Якщо хочете завершити програму - off",
          "Якщо бажаете продовжити - Enter", sep="\n")
    q.append(input("Що бажаете зробити?= "))
    while not q.count("off") and not q.count("") and len(q) == 2:
        q.clear()
        q.append("on")
        print("Невірне значення!")
        print("Якщо хочете завершити програму - off",
              "Якщо бажаете продовжити - Enter", sep="\n")
        q.append(input("Що бажаете зробити?= "))
    if q.count("off"):
        print("Допобачення!")
        break
    else:
        q.pop()
        continue
