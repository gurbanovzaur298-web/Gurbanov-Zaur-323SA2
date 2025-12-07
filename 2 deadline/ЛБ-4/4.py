import random

temperatures = [random.randint(10, 25) for _ in range(14)]

max_temp = max(temperatures)
min_temp = min(temperatures)

avg_temp = sum(temperatures) / len(temperatures)

days_above_avg = sum(1 for t in temperatures if t > avg_temp)

sorted_temps = sorted(temperatures)

fahrenheit_temps = [t * 9/5 + 32 for t in temperatures]

print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp:.1f}°C")
print(f"Дней выше средней: {days_above_avg}")
print(f"Отсортированные температуры: {sorted_temps}")
print(f"Температуры в Фаренгейтах: {[round(f, 1) for f in fahrenheit_temps]}")