# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
purchase_amounts = [0]  # Суммы покупок

with open('test_file/task_3.txt', encoding='utf-8') as file:
    text = file.readlines()
    current_purchase_idx = 0
    for line in text:
        if line[:-1].isdigit():
            purchase_amounts[current_purchase_idx] += int(line[:-1])
        else:
            current_purchase_idx += 1
            purchase_amounts.append(0)

three_most_expensive_purchases = sum(sorted(purchase_amounts, reverse=True)[:3])

assert three_most_expensive_purchases == 202346
