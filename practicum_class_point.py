#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Пользователь
#
# Created:     06.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км

    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(
        other.latitude) * cos(self.longitude - other.longitude)
        return 6371 * acos(cos_d)

class City(Point):

    def __init__(self, latitude, longitude, name, population):

        # допишите код: сохраните свойства родителя
        super().__init__(latitude, longitude)
        # и добавьте свойства name и population
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")

class Mountain(Point):

    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        # и добавьте свойства name и height
        self.name = name
        self.height = height
    # Переопределите метод show(self):
    def show(self):
        # информацию о горе нужно вывести в формате:
        # "Высота горы <название> - <высота> м."
        print("Высота горы {name} - {height} м.")

moscow = City(55.753960, 37.620393, "Москва", 11920000)
everest = Mountain(27.988056, 86.925278, "Эверест", 8849)
labinsk = City(44.6333, 40.7333, "Лабинск", 57273)
print(f"Расстояние от Москвы до Эвереста - {moscow.distance(everest)} км")
print(f"Расстояние от города {moscow.name} до города {labinsk.name} - {moscow.distance(labinsk)} км")