import random

def intList():
    
    return(list(str(random.randint(1,100000000))))

def symbList():
    letGlas = "aeiouy"
    letSoglas = "bcdfghjklmnpqrstvwxyz"
    lettersCount = random.randrange(8, 14)
    counter = 0
    list1 = []
    while counter < lettersCount:
        list1.append(letSoglas[random.randrange(0, 19)])
        list1.append(letGlas[random.randrange(0,5)])
        counter += 2

    return list1