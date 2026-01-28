exit = False
total_expenses: list[int] = []
day_expense: int = 0


while exit is not True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать все сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")
    option = input("Выберите опцию №: ")
    if option == "1":
        day_expense = int(input("Введите ваши расходы: "))
        total_expenses.append(day_expense)  # [100, 50, 50]

    elif option == "2":
        print("Все ваши расходы:")
        for ind, exp in enumerate(total_expenses):  # [1/100, 2/50, 50]
            print(f"{ind+1}.{exp}руб.")

    elif option == "3":
        average_expenses = sum(total_expenses) / len(total_expenses)
        print(f"Ваши расходы: {sum(total_expenses)} руб.")
        print(f"Ваши средние расходы: {int(average_expenses)} руб.")
    elif option == "4":
        num_delete = int(input("Введите номер расходов для удаления: "))
        total_expenses.pop(num_delete-1)
    elif option == "5":
        exit = True
    else:
        print("Некорректный ввод")
