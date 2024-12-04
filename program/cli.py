from program.storage import Storage
from program.task import Task
from program.task_manager import TaskManager


def display_menu():
    """Взаимодействие с пользователем через командную строку."""
    print("Меню:")
    print("1. Просмотреть все задачи")
    print("2. Добавить задачу")
    print("3. Изменить задачу")
    print("4. Выполнить задачу")
    print("5. Удалить задачу")
    print("6. Найти задачу")
    print("7. Сохранить изменения")
    print("0. Выход")

def show_tasks(tasks):
    for task in tasks:
        print(f"{task.id}: {task.title}")
        print(f"\tОписание: {task.description}")
        print(f"\tКатегория: {task.category}")
        print(f"\tСрок выполнения: {task.due_date}")
        print(f"\tПриоритет: {task.priority}")
        print(f"\tВыполнено: {'Да' if task.is_completed else 'Нет'}\n")

def run_cli():
    manager = TaskManager(Storage.load_tasks())
    
    while True:
        display_menu()
        choice = input("\nВведите номер пункта меню: ")
        
        if choice == '1':
            tasks = manager.get_all_tasks()
            if tasks:
                show_tasks(tasks)
            else:
                print("Задачи отсутствуют.")
            
        elif choice == '2':
            title = input("Название задачи: ")
            description = input("Описание задачи: ")
            category = input("Категория задачи: ")
            due_date = input("Срок выполнения (ДД-ММ-ГГГГ): ")
            priority = input("Приоритет (Низкий/Средний/Высокий): ")
            new_task = Task(title, description, category, due_date, priority)
            manager.add_task(new_task)
            print("Задача успешно добавлена!")
            
        elif choice == '3':
            id_ = input("ID задачи для изменения: ")
            task = manager.find_by_id(id_)
            if task:
                print(f"Текущие параметры задачи:\n{task.to_dict()}")
                new_title = input("Новое название (оставьте пустым для сохранения текущего): ") or task.title
                new_description = input("Новое описание (оставьте пустым для сохранения текущего): ") or task.description
                new_category = input("Новая категория (оставьте пустым для сохранения текущей): ") or task.category
                new_due_date = input("Новый срок выполнения (оставьте пустым для сохранения текущего): ") or task.due_date
                new_priority = input("Новый приоритет (оставьте пустым для сохранения текущего): ") or task.priority
                
                updated_task = Task(new_title, new_description, new_category, new_due_date, new_priority)
                updated_task.id = task.id
                updated_task.status = task.status
                manager.update_task(updated_task)
                print("Задача успешно изменена!")
            else:
                print("Задача с таким ID не найдена.")
                
        elif choice == '4':
            id_ = input("ID задачи для отметки как выполненной: ")
            completed_task = manager.complete_task(id_)
            if completed_task:
                print(f"Задача '{completed_task.title}' отмечена как выполненная.")
            else:
                print("Задача с таким ID не найдена.")
                
        elif choice == '5':
            id_ = input("ID задачи для удаления: ")
            if manager.delete_task(id_):
                print("Задача удалена.")
            else:
                print("Задача с таким ID не найдена.")
                
        elif choice == '6':
            query = input("Введите ключевое слово для поиска: ")
            found_tasks = manager.search_tasks(query)
            if found_tasks:
                show_tasks(found_tasks)
            else:
                print("По вашему запросу ничего не найдено.")
                
        elif choice == '7':
            Storage.save_tasks(manager.tasks)
            print("Все изменения были сохранены.")
            
        elif choice == '0':
            break
        
        else:
            print("Неправильный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    run_cli()
