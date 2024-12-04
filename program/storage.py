from task_manager import TaskManager

class Storage:
    """Загрузка и сохранение задач в файл."""
    @staticmethod
    def save_tasks(tasks):
        manager = TaskManager(tasks)
        manager.save_tasks()

    @staticmethod
    def load_tasks():
        manager = TaskManager.load_tasks_from_file()
        return manager.tasks
