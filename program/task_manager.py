import json

from task import Task

DATA_FILE_NAME = 'tasks.json'


class TaskManager:
    """Класс управляет всеми операциями над задачами.
       Добавление, редактирование, выполнение, удаление и поиск."""
    def __init__(self, tasks=None):
        if tasks is None:
            tasks = []
        self.tasks = tasks
        self.next_id = len(tasks) + 1

    def add_task(self, task: Task) -> Task:
        """Добавляет новую задачу."""
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Возвращает все текущие задачи."""
        return self.tasks

    def find_by_id(self, id: int) -> Task | None:
        """Ищет задачу по уникальному идентификатору."""
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def update_task(self, updated_task: Task) -> Task:
        """Обновляет существующую задачу."""
        index = next((i for i, t in enumerate(self.tasks) if t.id == updated_task.id), None)
        if index is not None:
            self.tasks[index] = updated_task
        return updated_task

    def delete_task(self, id: int) -> bool:
        """Удаляет задачу по идентификатору."""
        task_to_delete = self.find_by_id(id)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            return True
        return False

    def search_tasks(self, query: str) -> list[Task]:
        """Производит поиск задач по ключевому слову."""
        results = []
        query = query.lower()
        for task in self.tasks:
            if query in task.title.lower() or query in task.category.lower():
                results.append(task)
        return results

    def complete_task(self, id: int) -> Task | None:
        """Отмечает задачу как выполненную."""
        task = self.find_by_id(id)
        if task:
            task.mark_as_completed()
            return task
        return None
    def save_tasks(self, filename: str = DATA_FILE_NAME):
        """Сохраняет список задач в файл."""
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    @classmethod
    def load_tasks_from_file(cls, filename: str = DATA_FILE_NAME):
        """Загружает задачи из файла."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                tasks = [Task.from_dict(d) for d in data]
                return cls(tasks)
        except FileNotFoundError:
            print(f'Файл {filename} не найден.')
            return cls()
