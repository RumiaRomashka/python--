# Спросить у пользователя категорию блюда (напиток, суп, десерт)
# Если напиток - чай, кофе, сок
# Если суп - борщ, щи, суп-пюре
# Если десерт - торт, мороженое, фрукты
# Пользователь вводит конкретное блюдо
# Программа с помощью match case выводит цену выбранного блюда

price_tea = 20
price_cofee = 19
price_sok = 18
price_borch = 150
price_shi = 100
price_pyure = 80
price_tort = 200
price_ice = 230
price_frut = 340


order = input(
    "Введите выбранную категорию блюда (напиток, суп, десерт): ").lower().strip()

match order:
    case "напиток":
        drink = input("Выберите напиток (чай, кофе, сок) ").lower().strip()
        if drink == "чай":
            print(price_tea)
        elif drink == "кофе":
            print(price_cofee)
        elif drink == "сок":
            print(price_sok)
        else:
            print("Некорректный ввод")
    case "суп":
        sup = input("Выберите суп (борщ, щи, суп-пюре) ").lower().strip()
        if sup == "борщ":
            print(price_borch)
        elif sup == "щи":
            print(price_shi)
        elif sup == "суп-пюре":
            print(price_pyure)
        else:
            print("Некорректный ввод")
    case "десерт":
        desert = input(
            "Выберите десерт (торт, мороженое, фрукты) ").lower().strip()
        if desert == "торт":
            print(price_tort)
        elif desert == "мороженое":
            print(price_ice)
        elif desert == "фрукты":
            print(price_frut)
        else:
            print("Некорректный ввод")
    case _:
        print("Некорректный ввод")
