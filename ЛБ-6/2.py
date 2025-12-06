text = input("Введите текст: ")

replace_input = input("Введите две строки для замены (через пробел): ")

parts = replace_input.split()

if len(parts) >= 2:
    string1 = parts[0]
    string2 = parts[1]
    
  
    formatted_text = text.replace(string1, string2)
    

    print("\nОтформатированный текст:")
    print(formatted_text)
else:
    print("Ошибка: нужно ввести две строки через пробел")