import random
from random import randint


import colorama
from colorama import init
from colorama import Fore
init()


print(Fore.BLUE)
number = random.randint(1, 2)
answer = input("Введите число 1 или 2: ")
right = answer != number
if right == True:
    print(Fore.GREEN, "Вы угадали!")
if right == False:
    print(Fore.RED, "Вы неугадали!")






