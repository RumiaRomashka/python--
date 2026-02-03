exit = False
total_expenses: list[int] = []
value: int = 0


def add_expense(total_expenses, value: int) -> list:  # Добавляет расход список и их значения
    total_expenses.append(value)  # [100, 50, 50]
    return total_expenses


def delete_expense(total_expenses, index):  # Удаляет расход
    total_expenses.pop(index-1)
    return total_expenses


def get_total(total_expenses):  # Вовзращает сумму
    for ind, exp in enumerate(total_expenses):  # [1/100, 2/50, 50]
        print(f"{ind+1}.{exp}руб.")
    return total_expenses


def get_average(total_expenses):  # Возвращает средний расход
    average_expenses = sum(total_expenses) / len(total_expenses)
    return average_expenses


while exit is not True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать все сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")
    option = input("Выберите опцию №: ")

    if option == "1":
        value = int(input("Введите сумму вашего расхода: "))
        total_expenses = add_expense(total_expenses, value)

    elif option == "2":
        print("Все ваши расходы:")
        print(get_total(total_expenses))

    elif option == "3":
        average_expenses = get_average(total_expenses)
        print(f"Ваши расходы: {sum(total_expenses)} руб.")
        print(f"Ваши средние расходы: {int(average_expenses)} руб.")

    elif option == "4":
        index = int(input("Введите номер расходов для удаления: "))
        total_expenses = delete_expense(total_expenses, index)

    elif option == "5":
        exit = True
    else:
        print("Некорректный ввод")
