import math

user_input = input("Введите выражение (число знак число): ")

try:
    parts = user_input.split()
    
    if len(parts) != 3:
        print("Ошибка: нужно ввести три элемента через пробел")
    else:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        result = None
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ошибка: деление на ноль")
        elif operator == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                print("Ошибка: деление на ноль")
        elif operator == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                print("Ошибка: деление на ноль")
        elif operator == '**':
            result = num1 ** num2
        else:
            print(f"Ошибка: неизвестный оператор '{operator}'")
        
        if result is not None:
            print(f"Результат: {result}")
            
except ValueError:
    print("Ошибка: некорректный ввод чисел")
except Exception as e:
    print(f"Ошибка: {e}")