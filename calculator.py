while True:
    a = float(input("Первое число: "))
    operator=input("Оператор: ")
    b = float(input("Второе число: "))
    operators = {
        "+":f"Ответ: {a + b}",
        "-":f"Ответ: {a - b}",
        "*":f"Ответ: {a * b}",
        "/":f"Ответ: {a / b}",
        "**":f"Ответ: {a ** b}",
        "^":f"Ответ: {a ** b}",
        "//":f"Ответ: {a // b}",
        "%":f"Ответ: {a % b}"
    }
    
    if operators.get(operator, None) != None:
        print(operators.get(operator, "Вы ввели несуществующий оператор"))
    else: 
        print()
    