etazh = int(input("Введите номер этажа: "))
match etazh:
    case -1:
        print("Подвал, здесь находится склад")
    case 1:
        print("Холл и респешен")
    case 10:
        print("Технический этаж вход запрещен")
    case _ if 2 <= etazh <= 9:
        if etazh % 2 == 0:
            print("Офис")
        else:
            print("Жилые помещения")
    case _:
        print("Такого этажа не существует")
