a = float(input("Первое число: "))
operator=input("Оператор: ")
b = float(input("Второе число: "))
if operator == "+":
    answer = a + b
    print("Ответ:" + str(answer))
if operator == "-":
    answer = a - b 
    print("Ответ:" + str(answer))
if operator == "*":
    answer = a * b 
    print("Ответ:" + str(answer))
if operator == "/":
    answer = a / b 
    print("Ответ:" + str(answer))
    