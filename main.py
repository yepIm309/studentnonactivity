from math import factorial, acos
from random import randrange


class Calculator:

    def plus(self, digit, digit2):
        print(int(digit + digit2))

    def minus(self, digit, digit2):
        print(int(digit - digit2))

    def proizv(self, digit, digit2):
        print(int(digit * digit2))

    def delenie(self, digit, digit2):
        print(float(digit / digit2))

    def exp(self, digit, digit2):
        print(int(digit ** digit2))

    def process(self, enter):
        while (enter != "stop"):
            if (enter == "+"):
                self.plus(int(input("Первое число: ")), int(input("Второе число: ")))
            elif (enter == "-"):
                self.minus(int(input("Первое число: ")), int(input("Второе число: ")))
            elif (enter == "*"):
                self.proizv(int(input("Первое число: ")), int(input("Второе число: ")))
            elif (enter == "/"):
                self.delenie(float(input("Первое число: ")), float(input("Второе число: ")))
            elif (enter == "**"):
                self.exp(int(input("Первое число: ")), int(input("Второе число: ")))
            elif (enter == "abs"):
                print(abs(int(input("Введите число: "))))
            elif (enter == "random"):
                print(randrange(int(input("Введите число: "))))
            elif (enter == "factorial"):
                print(factorial(int(input("Введите число: "))))
            elif (enter == "acos"):
                print(acos(int(input("Введите число от '-1' до '1': "))))
            enter = input("Введите действие: ")


calc = Calculator()

print('''
    Программа Калькулятор.
    Выберите действие:
    '+' - сложение
    '-' - вычитание
    '*' - умножение
    '/' - деление
    '**' - возведение в степень
    'abs' - модуль числа
    'random' - случайное число
    'factorial' - факториал числа
    'acos' - арккосинус
    'stop' - закончить работу программы
    ''')

enter = input("Введите действие: ")
calc.process(enter)