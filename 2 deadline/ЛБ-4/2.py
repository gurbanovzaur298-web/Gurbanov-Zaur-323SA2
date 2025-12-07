import random

numbers = [random.randint(1, 100) for _ in range(10)]

even_numbers = [x for x in numbers if x % 2 == 0]
numbers_gt_50 = [x for x in numbers if x > 50]

print("=" * 50)
print(f"Исходный список ({len(numbers)} чисел): {numbers}")
print(f"Четные числа ({len(even_numbers)} чисел): {even_numbers}")
print(f"Числа больше 50 ({len(numbers_gt_50)} чисел): {numbers_gt_50}")
print("=" * 50)