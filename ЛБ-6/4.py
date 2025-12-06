text = input("Введите текст: ")

range_input = input("Введите диапазон (два числа через пробел, например: '3 7'): ")

try:
    start_user, end_user = map(int, range_input.split())
    
    start_index = start_user - 1  
    end_index = end_user          
    
    if start_user < 1 or end_user < start_user:
        print("Ошибка: некорректный диапазон")
    elif start_index >= len(text) or end_user > len(text):
        print(f"Ошибка: диапазон выходит за пределы текста (длина: {len(text)})")
    else:
       
        substring = text[start_index:end_index]
        print(f"\nПодстрока: '{substring}'")
        
except ValueError:
    print("Ошибка: нужно ввести два числа")
except Exception:
    print("Произошла ошибка")