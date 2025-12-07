def calc_avg(numbers: list[float]) -> float:
    """
    Вычисляет среднее арифметическое значение списка чисел.
    
    Args:
        numbers (list[float]): Список чисел для вычисления среднего
        
    Returns:
        float: Среднее арифметическое значение. Возвращает 0.0 для пустого списка
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    """
    Форматирует ФИО из списка частей имени.
    
    Args:
        parts (list[str]): Список частей имени (фамилия, имя, отчество)
        capitalize (bool, optional): Приводить ли первую букву каждого слова к верхнему регистру. 
                                   По умолчанию True.
        
    Returns:
        str: Отформатированная строка с ФИО
    """
    fio = " ".join(parts)

    if capitalize:
        return fio.title()

    return fio


def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    """
    Фильтрует словарь с оценками, оставляя только те, которые не ниже минимального значения.
    
    Args:
        data_dict (dict[str, int]): Словарь с предметами и оценками
        min_value (int): Минимальное значение оценки для включения в результат
        
    Returns:
        dict[str, int]: Отфильтрованный словарь с оценками, не ниже min_value
    """
    result = {}

    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value

    return result


if __name__ == "__main__":
    print("=" * 50)
    print("Функция 1: calc_avg (вычисление среднего значения)")
    print("=" * 50)
    
    test_cases_1 = [
        [10, 20, 30, 40],
        [1, 2, 3, 4, 5],
        [100, 200],
        []
    ]
    
    for numbers in test_cases_1:
        average = calc_avg(numbers)
        print(f"calc_avg({numbers}) = {average}")
    
    print("\n" + "=" * 50)
    print("Функция 2: fmt_fio (форматирование ФИО)")
    print("=" * 50)
    
    test_cases_2 = [
        (['петров', "иван", "сергеевич"], True),
        (['сидорова', "анна", "валерьевна"], False),
        (['ИВАНОВ', "петр", "семенович"], True),
        (['смирнов', "алексей"], True)
    ]
    
    for parts, cap in test_cases_2:
        result = fmt_fio(parts, cap)
        print(f"fmt_fio({parts}, capitalize={cap}) = '{result}'")
    
    print("\n" + "=" * 50)
    print("Функция 3: filter_scores (фильтрация оценок)")
    print("=" * 50)
    
    scores = {"math": 95, "history": 78, "english": 88, "art": 92, "physics": 85}
    thresholds = [90, 85, 80, 95, 100]
    
    print(f"Исходные оценки: {scores}")
    
    for threshold in thresholds:
        filtered = filter_scores(scores, threshold)
        print(f"Оценки >= {threshold}: {filtered}")