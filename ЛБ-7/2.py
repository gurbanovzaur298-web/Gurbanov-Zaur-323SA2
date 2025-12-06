password = input("Введите пароль для регистрации: ")
confirm_password = input("Подтвердите пароль: ")

if password == confirm_password:
    print("Пароль успешно установлен!")
else:
    print("Пароли не совпадают!")
    exit() 

print("\n" + "="*30)

login_password = input("Введите пароль для входа: ")

if login_password == password:
    print("Access")
else:
    print("Denied")