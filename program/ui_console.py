from storage import Storage
from task import Task, DATE_PATTERN_DATA, DATE_PATTERN_RU
from task_manager import TaskManager


def display_menu():
    """Взаимодействие с пользователем через командную строку."""
    print('Меню:')
    print('1. Просмотреть все задачи')
    print('2. Добавить задачу')
    print('3. Изменить задачу')
    print('4. Выполнить задачу')
    print('5. Удалить задачу')
    print('6. Найти задачу')
    print('7. Сохранить изменения')
    print('0. Выход')


def show_task(task):
    print(f'{task.id}: {task.title}')
    print(f'Описание: {task.description}')
    print(f'Категория: {task.category}')
    print(f'Срок выполнения: {task.due_date.strftime(DATE_PATTERN_DATA)}')
    print(f'Приоритет: {task.priority}')
    print(f'Выполнено: {'Да' if task.is_completed else 'Нет'}\n')


def show_tasks(tasks):
    for task in tasks:
        show_task(task)


def run_program_ui():
    manager = TaskManager(Storage.load_tasks())

    while True:
        display_menu()
        choice = input('\nВведите номер пункта меню: ')

        if choice == '1':
            tasks = manager.get_all_tasks()
            if tasks:
                show_tasks(tasks)
            else:
                print('Задачи отсутствуют.')

        elif choice == '2':
            title = input('Название задачи: ')
            description = input('Описание задачи: ')
            category = input('Категория задачи: ')
            due_date = Task.convert_data_from_str(
                input(f'Срок выполнения {DATE_PATTERN_RU}: ')
            )
            priority = input('Приоритет (Низкий/Средний/Высокий): ')
            status_code = int(
                input('Статус задачи (1=Выполнено/0=Не выполнено): ')
            )
            new_task = Task(
                id=None,
                title=title,
                description=description,
                category=category,
                due_date=due_date,
                priority=priority,
                status=status_code == 1
            )
            manager.add_task(new_task)
            print('Задача успешно добавлена!')

        elif choice == '3':
            id = int(input('ID задачи для изменения: '))
            task = manager.find_by_id(id)
            if not task:
                print('Задача с таким ID не найдена.')
                return

            print('Текущие параметры задачи:')
            show_task(task)

            new_title = input(
                'Новое название (оставьте пустым для сохранения текущего): '
            ) or task.title
            new_description = input(
                'Новое описание (оставьте пустым для сохранения текущего): '
            ) or task.description
            new_category = input(
                'Новая категория (оставьте пустым для сохранения текущей): '
            ) or task.category
            new_due_date = input(
                f'Новый срок выполнения ({DATE_PATTERN_RU}) (оставьте пустым для сохранения текущего): '
            ) or None
            new_priority = input(
                'Новый приоритет (оставьте пустым для сохранения текущего): '
            ) or task.priority

            task.title = new_title
            task.description = new_description
            task.category = new_category

            if new_due_date:
                task.due_date = Task.convert_data_from_str(new_due_date)

            task.priority = new_priority
            manager.update_task(task)
            print('Задача успешно изменена!')

        elif choice == '4':
            id = int(input('ID задачи для отметки как выполненной: '))
            completed_task = manager.complete_task(id)
            if completed_task:
                print(
                    f'Задача "{completed_task.title}" отмечена как выполненная.'
                )
            else:
                print('Задача с таким ID не найдена.')

        elif choice == '5':
            id = int(input('ID задачи для удаления: '))
            if manager.delete_task(id):
                print('Задача удалена.')
            else:
                print('Задача с таким ID не найдена.')

        elif choice == '6':
            query = input('Введите ключевое слово для поиска: ')
            found_tasks = manager.search_tasks(query)
            if found_tasks:
                show_tasks(found_tasks)
            else:
                print('По вашему запросу ничего не найдено.')

        elif choice == '7':
            Storage.save_tasks(manager.tasks)
            print('Все изменения были сохранены.')

        elif choice == '0':
            Storage.save_tasks(manager.tasks)
            break

        else:
            print('Неправильный выбор. Попробуйте еще раз.')


if __name__ == '__main__':
    run_program_ui()
