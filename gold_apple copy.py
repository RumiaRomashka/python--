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
    while not exit:
        print("1.Пополнить")
        print("2.Списать")
        print("3.Остаток")
        print("4.Выход")
        option = int(input("Выберите опцию: "))
        schet, exit = do_option(option, schet, exit)


def get_sum():
    return int(input("Введите сумму: "))


def do_option(option: int, schet: int, exit: bool):
    if option == 1:
        popolnenie = get_sum()
        schet += popolnenie

    elif option == 2:
        spisanie = get_sum()
        if spisanie > schet:
            print("Недостаточно средств")
        else:
            schet -= spisanie

    elif option == 3:
        print(schet)

    elif option == 4:
        exit = True

    return schet, exit


main()
