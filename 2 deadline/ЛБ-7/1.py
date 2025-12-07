def sum_numbers(*args: float) -> float:
    """
    Возвращает сумму произвольного количества чисел.
    
    Parameters:
    *args: произвольное количество числовых аргументов
    
    Returns:
    float: сумма всех переданных чисел
    """
    return sum(args)


# Пример вызова
print(sum_numbers(1, 2, 3, 4, 5))  # 15