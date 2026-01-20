# ВВести три траты: еда, транспорт, развлечения.
# Вывести общую сумму и среднеее.

food = input("Затраты на еду: ")
transport = input("Затраты на транспорт: ")
entertainment = input("Затраты на развлечения: ")
budget = int(food.strip()) + int(transport.strip()) + \
    int(entertainment.strip())
srednee = int(budget / 3)

print("Общие затраты: ", budget, "руб.")
print("Средние затраты: ", srednee, "руб.")
