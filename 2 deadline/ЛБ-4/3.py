tasks = []

while True:
    print("\n" + "="*30)
    print("To-Do List")
    print("="*30)
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    
    choice = input("\nВыберите действие: ")
    
    if choice == '1':
        if tasks:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("\nСписок задач пуст!")
    
    elif choice == '2':
        task = input("\nВведите новую задачу: ")
        tasks.append(task)
        print(f"Задача '{task}' добавлена!")
    
    elif choice == '3':
        if not tasks:
            print("\nСписок задач пуст!")
            continue
            
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        try:
            task_num = int(input("\nКакую задачу выполнили? (номер): "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Задача '{removed_task}' удалена!")
            else:
                print("Неверный номер задачи!")
        except ValueError:
            print("Пожалуйста, введите число!")
    
    elif choice == '4':
        print("Выход из программы. До свидания!")
        break
    
    else:
        print("Неверный выбор! Введите число от 1 до 4.")