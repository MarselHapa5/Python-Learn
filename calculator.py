
from colorama import init
from colorama import Fore, Back, Style
init()
repeat = 1
while repeat == 1:
    print (Back.BLUE)
    exit = input("Вы хотите выйти из программы(если вы хотите выйти напечатайте Yes если не хотите напечатайте No)")
    if (exit == "Yes"):
        quit()
    if (exit == "No"):
        print("Хорошо")
    a = float(input("Первое число: "))
    print (Back.GREEN)
    operator=input("Оператор: ")
    print (Back.BLUE)
    b = float(input("Второе число: "))
    print (Back.RED)
    if (operator == "+"):
        answer = a + b
        print("Ответ:")
        print(answer)
    if (operator == "+"):
        answer = a - b
        print("Ответ:")
        print(answer)
    if (operator == "*"):
        answer = a * b
        print("Ответ:")
        print(answer)
    if (operator == "/"):
        answer = a / b
        print("Ответ:")
        print(answer)
    if (operator == "**"):
        answer = a ** b
        print("Ответ:")
        print(answer)