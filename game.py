from colorama import init
from colorama import Fore,Back,Style
init()






Floor1 = input("Вы видите две двери в какую вы зайдете?(1 или 2): ")
if (Floor1 == "1"):
    print(Fore.RED ,"Неправильно. Вы умерли.")
    quit()
if (Floor1 == "2"):
    print(Fore.GREEN, "Правильно. Вы выжили")
    Floor2 = input("Это огненный дракон что вы используете против него?(Огненную бомбу(1), или Ледяную бомбу(2)?")
    if(Floor2 == "1"):
        print(Fore.RED, "Дракон даже ничего не почувствовал и съел вас. Вы умерли.")
        quit()
    if(Floor2 == "2"):
        print(Fore.GREEN, "Правильно. Вы выжили")



    
    