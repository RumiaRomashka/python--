def hello():
    print("Привет")


hello()


def hello1(name: str):
    print("Привет,", name)


hello1("Rumi")


def multiply(a: float, b: float) -> float:
    res = a * b
    return res


res = multiply(2, 4)
print(res)

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

type holodniy_ovosch = int


def holodilnik() -> int:
    ovosch = input("Напиши число ")
    ohlad_ovosch = int(ovosch)
    return ohlad_ovosch


ovosch_from_holodilnik = holodilnik()  # "1" -> 1
# ovosch_from_holodilnik = 1
print(ovosch_from_holodilnik)
