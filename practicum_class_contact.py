#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     06.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Contact:
    def __init__(self, name, phone, address,birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday

        print(f"Создаём новый контакт {name}(объект {__name__} класса Contact()) ")

# здесь создайте объекты mike и vlad
mike = Contact("Михаил Булгаков", "2-03-27", "Россия, Москва, Большая Пироговская, дом 35б, кв.6", "15.05.1891")
vlad = Contact("Владимир Маяковский", "73-88", "Лубянский проезд, д.3, кв.12", "19.07.1893")
def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")

# здесь вызовите функцию print_contact(),
# и она напечатает на экране данные контактов mike и vlad
print_contact()

# Изменяем свойство объектов
mike.address = "Россия, Москва, Нащокинский переулок, дом 3, кв.44"
mike.phone = "К-058-67"
vlad.address = "Россия, Гендриков переулок, дом 15, кв. 5"
vlad.phone = "2-35-71"

# выводим контакты с изменениями
print_contact()
