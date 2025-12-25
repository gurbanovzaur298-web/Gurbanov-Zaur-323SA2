nomer = input("введите номер телефона в формате '+7-XXX-XXX-XX-XX': ")
print(f"\nпроверка номера: {nomer}")
if len(nomer) != 16:
    print("неверно: неверная длина номера")
    print("ожидается 16 символов, получено:", len(nomer))
    exit()
if nomer[0] != '+' or nomer[1] != '7' or nomer[2] != '-':
    print("неверно: неверное начало (+7-)")
    exit()
if nomer[6] != '-' or nomer[10] != '-' or nomer[13] != '-':
    print("неверно: дефисы не на своих местах")
    exit()
mesta_s_tsiframi = [3, 4, 5, 7, 8, 9, 11, 12, 14, 15]
for mesto in mesta_s_tsiframi:
    if not nomer[mesto].isdigit():
        print(f"неверно: символ в позиции {mesto} не цифра")
        exit()
kod_operatora = nomer[3:6]
dopustimye_kody = ['910', '911', '912', '915', '916', '917', '918', '919',
                   '921', '922', '923', '924', '925', '926', '927', '928', '929']
if kod_operatora not in dopustimye_kody:
    print(f"неверно: код оператора {kod_operatora} не поддерживается")
    exit()
print("верно: номер корректен")
print(f"код оператора: {kod_operatora}")