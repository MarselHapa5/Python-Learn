from colorama import init
from colorama import Fore, Back, Style
init()
print (Back.BLUE)

a = float(input("Первое число: "))
print (Back.GREEN)
operator=input("Оператор: ")
print (Back.BLUE)
b = float(input("Второе число: "))
print (Back.RED)
answer = a operator b
print(float(answer))