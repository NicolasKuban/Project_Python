#-------------------------------------------------------------------------------
# Name:        Листинг 2.7. Вычисление суммы чисел (арифмитическая прогрессия)
# Purpose:
#
# Author:      nicrad
#
# Created:     21.08.2022
# Copyright:   (c) nicrad 2022
# Licence:     <private>
#-------------------------------------------------------------------------------
#
#
# Быстрый способ
# sum(range(1, n+1))
#
# Выводим сообщение о назначение программы
print("Сумма натуральных чисел")
# Запрашиваем у пользователя верхний предел прогрессии
limit = int(input("Введите верхний предел прогрессии: "))
# Формируем текст итогового сообщения
result_text = f"1 + 2 + ... {limit} ="
total = 0
# Оператор цикла для вычисления суммы прогрессии
for i in range(1, limit + 1):
    # Увеличиваем сумму прогрессии на величину текучего числа
    total += i
# Выводим на экран результат вычислений
print(result_text, total)
