# Создать список из трат на неделю (7 чисел)
# Посчитать сумму, среднее, минимум и максимум
# Сохранить в кортеже (минимум, максимум, сумма) и вывести его

cost = [340, 560, 2890, 569, 3100, 5100, 677]
sum_cost = sum(cost)
min_cost = min(cost)
max_cost = max(cost)
sr_cost = sum_cost / len(cost)
tuple_cost = (min_cost, max_cost, sum_cost)
print(tuple_cost)
