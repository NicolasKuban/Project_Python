# -------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Пользователь
#
# Created:     06.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
# -------------------------------------------------------------------------------

class Human:
    def __init__(self, name):
        self.name = name
    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу

    def answer_question(self, question):
        print("Очень интересный вопрос! Не знаю.")


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f"{someone.name}, {question}")
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question in right_answer:
            # если да - ответить на него
            print(right_answer[question])
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            super().answer_question(question)

# объявите и реализуйте классы CodeReviewer и Mentor


class CodeReviewer(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question in right_answer:
            # если да - ответить на него
            print(right_answer[question])
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question in right_answer:
            # если да - ответить на него
            print(right_answer[question])
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            super().answer_question(question)

# Функция для обработки правильных ответов


right_answer = {
    "мне грустненько, что делать?": "Держись, всё получится. Хочешь видео с котиками?",
    "мне грустненько, что делать?": "Отдохни и возвращайся с вопросами по теории.",
    "что не так с моим проектом?": "О, вопрос про проект, это я люблю.",
    "как устроиться работать питонистом?": "Сейчас расскажу."
}

# следующий код менять не нужно, он работает, мы проверяли


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
student1.ask_question(curator, 'как вы сегодня спали?')
student1.ask_question(mentor, 'как вы сегодня спали?')
student1.ask_question(reviewer, 'как вы сегодня спали?')
