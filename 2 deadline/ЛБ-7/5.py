def format_report(report_title, *data, **properties):
    """Форматирует отчет с данными и свойствами"""
    
    print(f"--- Отчет: {report_title} ---")
    
    print("Данные:")
    for item in data:
        print(f" - {item}")
    
    print("\nСвойства:")
    for key, value in properties.items():
        print(f" - {key}: {value}")
    
    print("-" * 30)


format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)