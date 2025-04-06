"""
Консольный менеджер задач
=========================

Описание:
    Программа предоставляет простой интерфейс для управления списком задач через консоль.
    Пользователь может добавлять, просматривать, отмечать и удалять задачи.

Использование:
    Запустите скрипт:
        python task_manager.py
"""

def display_menu():
    print("\n--- Менеджер задач ---")
    print("1. Добавить задачу")
    print("2. Просмотреть задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выход")

def add_task(tasks):
    task = input("Введите описание новой задачи: ").strip()
    if task:
        tasks.append({'task': task, 'done': False})
        print("Задача добавлена!")
    else:
        print("Описание задачи не может быть пустым.")

def view_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nСписок задач:")
    for idx, item in enumerate(tasks, start=1):
        status = "✔" if item['done'] else "✖"
        print(f"{idx}. [{status}] {item['task']}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = True
            print("Задача отмечена как выполненная!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Введите номер задачи, которую хотите удалить: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Задача '{removed['task']}' удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Выход из программы. До новых встреч!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == '__main__':
    main()
