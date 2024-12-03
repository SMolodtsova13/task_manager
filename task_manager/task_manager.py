from .task import Task
import uuid


class TaskManager:
    """Класс управляет всеми операциями над задачами.
       Добавление, редактирование, выполнение, удаление и поиск."""
    def __init__(self, tasks=None):
        if tasks is None:
            tasks = []
        self.tasks = tasks

    def add_task(self, task: Task) -> Task:
        """Добавляет новую задачу."""
        task.id = str(uuid.uuid4())
        self.tasks.append(task)
        return task

    def get_all_tasks(self) -> list[Task]:
        """Возвращает все текущие задачи."""
        return self.tasks

    def find_by_id(self, id_: str) -> Task | None:
        """Ищет задачу по уникальному идентификатору."""
        for task in self.tasks:
            if task.id == id_:
                return task
        return None

    def update_task(self, updated_task: Task) -> Task:
        """Обновляет существующую задачу."""
        index = next((i for i, t in enumerate(self.tasks) if t.id == updated_task.id), None)
        if index is not None:
            self.tasks[index] = updated_task
        return updated_task

    def delete_task(self, id_: str) -> bool:
        """Удаляет задачу по идентификатору."""
        task_to_delete = self.find_by_id(id_)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            return True
        return False

    def search_tasks(self, query: str) -> list[Task]:
        """Производит поиск задач по ключевому слову."""
        results = []
        for task in self.tasks:
            if query.lower() in task.title.lower():
                results.append(task)
        return results

    def complete_task(self, id_: str) -> Task | None:
        """Отмечает задачу как выполненную."""
        task = self.find_by_id(id_)
        if task:
            task.mark_as_completed()
            return task
        return None

    def save_tasks(self, filename: str = 'tasks.json'):
        """Сохраняет список задач в файл."""
        import json
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    @classmethod
    def load_tasks_from_file(cls, filename: str = 'tasks.json'):
        """Загружает задачи из файла."""
        import json
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                tasks = [Task.from_dict(d) for d in data]
                return cls(tasks)
        except FileNotFoundError:
            print(f'Файл {filename} не найден.')
            return cls()
