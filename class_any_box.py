#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     29.08.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Первый базовый класс
class box_size:
    # конструктор
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    # Метод для вычисления объема
    def volume_box(self):
        # Результат - произведение полей экземпляра
        return self.width * self.height * self.depth
    # Метод для отображения значений полей экземпляра
    # и результат вызова метода volume()
    def show(self):
        # Поля экземпляра класса
        print("Размеры и объем ящика:")
        print("{0:<12}".format("Ширина:"), self.width)
        print("{0:<12}".format("Высота:"), self.height)
        print("{0:<12}".format("Глубина:"), self.depth)
        # Результат вызова метода volume()
        print("{0:<12}".format("Объем:"), self.volume_box())
# Второй базовый класс
class box_parametrs:
    # конструктор
    def __init__(self, weight, color):
        # Присваивание значений полям экземпляра
        self.weight = weight
        self.color = color
    # Метод для отображения значений полей экземпляра
    def show(self):
        # Отображение значений полей
        print("\nДополнительные параметры ящика:")
        print("{0:<12}".format("Вес (масса):"), self.weight)
        print("{0:<12}".format("Цвет:"), self.color)

# Производный класс
class box(box_size, box_parametrs):
    # Конструктор
    def __init__(self, width, height, depth, weight, color):
        # Вызов конструктора первого базового класса
        box_size.__init__(self, width, height, depth)
        # Вызов конструктора второго базового класса
        box_parametrs.__init__(self, weight, color)
        # Вызов метода show() экземпляра класса
        self.show()
    # Переопределение метода show()
    def show(self):
        # Вызов метода show() из первого базового класса
        box_size.show(self)
        # Вызов метода show() из второго базового клааса
        box_parametrs.show(self)
# Создаем экземпляр производного класса
any_box = box(10, 20, 30 ,5, "зеленый")
# any_box.show()