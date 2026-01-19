# Функциональность:
# Задать бюджет;
# Внести траты;
# Вывести остаток.
# Ошибка при недостатки средств.
# Пополноть бюджет.

# Логика:
# input от пользователя бюджет в руб.
# input от пользователя траты итого в руб., они недолжны быть отрицательные, будет ошибка.
# Просчитать формалой остаток и принт его
# Вывывести ошибку при траты >   бюджет -> Просьба пополнить бюджет предупреждение
# Если ок, то остаток = бюджет - траты
# Добавить - пополнить бюджет и все пересчитывается

def main():
    exit = False
    schet = 0
    while exit is not True:
        print("Пополнить")
        print("Списать")
        print("Остаток")
        print("Выход")
        option = input("Выберите опцию: ")
        schet, exit = do_option(option, schet, exit)


def get_sum():
    summ = int(input("Введите сумму: "))
    return summ


def do_option(option: str, schet: int, exit: bool):
    if option == "Пополнить":
        popolnenie = get_sum()
        schet = schet + popolnenie
        print(schet)
    elif option == "Списать":
        spisanie = get_sum()
        if spisanie > schet:
            print("Недостаточно средств")
        else:
            schet = schet - spisanie
            print(schet)
    elif option == "Выход":
        exit = True
    else:
        print(schet)

    return schet, exit


main()
