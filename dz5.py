# 100 руб 50 коп -> 100.50₽ ["100", "руб", "50", "коп"] if len(money) = 4
# 100 руб -> 100.00₽ ["100", "руб"] if len(money) = 2
# руб ["руб"] if len(money) != 2 or len(money) !=4
# 100 руб 25 ["100", "руб", "25"]
# 100 25 ["100", "25"]
# 100 рар 25 аар ["100", "рар", "25", "аар"] если [1] != "руб" или [3] != "коп" и проверить что [0] и[2] цифры

money = input("Введите сумму: ").lower().replace(".", "").replace(",", "")
money = money.split(" ")
if not (len(money) == 2 or len(money) == 4):
    print("Некорректный формат суммы")
    exit()
if len(money) == 4:
    if money[1] != "руб" or money[3] != "коп":
        print("Некорректный формат суммы")
        exit()
    elif not money[0].isnumeric() and not money[2].isnumeric():
        print("Некорректный формат суммы")
        exit()
    else:
        print(f"{money[0]}.{money[2]}₽")

else:
    if money[1] != "руб":
        print("Некорректный формат суммы")
        exit()
    elif not money[0].isnumeric():
        print("Некорректный формат суммы")
        exit()
    else:
        print(f"{money[0]}.00₽")
