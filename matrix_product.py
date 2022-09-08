#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     27.08.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Подключаем модуль для генерирования случайных чисел
from random import *

# Функция для создания матрицы со случайными элементами
def matrix_filling(n, m):
    matrix =  [[randint(0, 9) for j in range(m)] for i in range(n)]
    return matrix

# Функция для создания единичной матрицы
def unit_matrix(n):
    matrix = [[int(i == j) for i in range(n)] for j in range(n)]
    return matrix
# Функция для вычисления произведения квадратных матриц
def matrix_product(A, B):
    # Размер матрицы
    matrix_size = len(A)
    # Результирующая матрица с начальными нулевыми значениями
    C = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    # Первый индекс
    for i in range(matrix_size):
        # Второй индекс
        for j in range(matrix_size):
            # Внутренний индекс, по которому берется сумма
            for k in range(matrix_size):
                # Добавляем слагаемок в сумму
                C[i][j] += A[i][k] * B[k][j]
    # Вывод резултата функции
    return C
# Функция для отображения матрицы
def show_matrix(matrix):
    # Перебор строк матрицы
    for line in matrix:
        # Перебор элементов в строке матрицы
        for element in line:
            # Отображаем элемент матрицы
            print(element, end=" ")
        # Переход на новую строку
        print()
# Инициализация генератора случайных чисел
seed(2014)
# Матрица со случайными числами
A = matrix_filling(3, 5)
# Матрица в виде списка
print("Список:", A)
# Матрица как она есть
print ("Эта же матрица:")
show_matrix(A)
# Единичная матрица
E = unit_matrix(4)
print("Единичная матрица:")
show_matrix(E)
# Первая матрица
A1 = matrix_filling(3, 3)
A2 = matrix_filling(3, 3)
# Произведение матриц
A3 = matrix_product(A1, A2)

# Вывод матриц
print("Первая матрица:")
show_matrix(A1)
print("Вторая матрица:")
show_matrix(A2)
print("Произведение матриц:")
show_matrix(A3)
