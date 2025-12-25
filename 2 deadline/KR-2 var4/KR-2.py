import math
route = [(0, 0), (2, 4), (5, 8), (10, 8), (12, 5)]
print("анализ gps-трека:")
print("координаты точек:", route)
print()
obshaya_dlina = 0
print("расчет длин участков:")
for i in range(len(route) - 1):
    tochka1 = route[i]
    tochka2 = route[i + 1]
    x1, y1 = tochka1
    x2, y2 = tochka2
    rasstoyanie = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    obshaya_dlina += rasstoyanie
    print(f"участок {i+1}: {tochka1} -> {tochka2} = {rasstoyanie:.2f}")
print(f"\n1. общая длина маршрута: {obshaya_dlina:.2f}")
print()
max_dlina = 0
max_nachalo = None
max_konec = None
for i in range(len(route) - 1):
    tochka1 = route[i]
    tochka2 = route[i + 1]
    x1, y1 = tochka1
    x2, y2 = tochka2   
    rasstoyanie = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if rasstoyanie > max_dlina:
        max_dlina = rasstoyanie
        max_nachalo = tochka1
        max_konec = tochka2
print(f"2. самый длинный перегон:")
print(f"   начало: {max_nachalo}")
print(f"   конец: {max_konec}")
print(f"   длина: {max_dlina:.2f}")
print()
pervaya_tochka = route[0]
poslednyaya_tochka = route[-1]
print(f"3. проверка замкнутости:")
print(f"   первая точка: {pervaya_tochka}")
print(f"   последняя точка: {poslednyaya_tochka}")
if pervaya_tochka == poslednyaya_tochka:
    print("   маршрут замкнут (первая и последняя точки совпадают)")
else:
    print("   маршрут не замкнут")