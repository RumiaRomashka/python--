# Калькулятор скидки. Спросить у пользователч цену товара Спроисть процент скидки. Просчитать и вывести цену со скидкой.
price = input("Введите цену товара: ")
discount = input("Введите процент скидки: ")
discount_price = int(price.strip()) * (int(discount.strip()) / 100)
new_price = int(price) - discount_price
print("Цена с учетом скидки:", int(new_price), "руб.")
