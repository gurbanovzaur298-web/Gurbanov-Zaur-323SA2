tekst = input("введите произвольный текст: ")

zamena = input("введите что заменить и на что заменить (через пробел): ")

chasti_zameny = zamena.split()

if len(chasti_zameny) >= 2:
    chto_zamenit = chasti_zameny[0]
    na_chto_zamenit = chasti_zameny[1]
    
    noviy_tekst = tekst.replace(chto_zamenit, na_chto_zamenit)
    
    print("результат замены:")
    print(noviy_tekst)
else:
    print("ошибка: нужно ввести две строки через пробел")