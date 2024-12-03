# import json
# import pytest
# from manager import Task, TaskManager

# @pytest.fixture(scope="module")
# def setup():
#     manager = TaskManager("tasks_test.json")
#     yield manager

# def test_add_task(setup):
#     manager = setup
#     task = Task("Новая задача", "Описание задачи", "Работа", "2023-01-05", "Высокий")
#     manager.add_task(task)
#     assert len(manager.tasks) == 1
#     assert manager.tasks[0].title == "Новая задача"

# def test_edit_task(setup):
#     manager = setup
#     task = Task("Редактируемая задача", "Описание задачи", "Личное", "2023-02-06", "Средний")
#     manager.add_task(task)
#     manager.edit_task(task.task_id, {"title": "Отредактированная задача"})
#     assert manager.tasks[0].title == "Отредактированная задача"

# def test_mark_as_done(setup):
#     manager = setup
#     task = Task("Завершенная задача", "Описание задачи", "Обучение", "2023-03-07", "Низкий")
#     manager.add_task(task)
#     manager.mark_as_done(task.task_id)
#     assert manager.tasks[0].status == True

# def test_delete_task(setup):
#     manager = setup
#     task = Task("Удаляемая задача", "Описание задачи", "Работа", "2023-04-08", "Средний")
#     manager.add_task(task)
#     manager.delete_task(task.task_id)
#     assert len(manager.tasks) == 0

# def test_find_task_by_id(setup):
#     manager = setup
#     task = Task("Найденная задача", "Описание задачи", "Личное", "2023-05-09", "Высокий")
#     manager.add_task(task)
#     found_task = manager.find_task_by_id(task.task_id)
#     assert found_task == task

# def test_list_all_tasks(setup):
#     manager = setup
#     task1 = Task("Первая задача", "Описание первой задачи", "Работа", "2023-06-10", "Средний")
#     task2 = Task("Вторая задача", "Описание второй задачи", "Личное", "2023-07-11", "Низкий")
#     manager.add_task(task1)
#     manager.add_task(task2)
#     all_tasks = manager.list_all_tasks()
#     assert len(all_tasks) == 2
#     assert all_tasks[0].title == "Вторая задача"

# def test_list_tasks_by_category(setup):
#     manager = setup
#     task1 = Task("Первая задача", "Описание первой задачи", "Работа", "2023-08-12", "Высокий")
#     task2 = Task("Вторая задача", "Описание второй задачи", "Личное", "2023-09-13", "Средний")
#     manager.add_task(task1)
#     manager.add_task(task2)
#     work_tasks = manager.list_tasks_by_category("Работа")
#     personal_tasks = manager.list_tasks_by_category("Личное")
#     assert len(work_tasks) == 1
#     assert len(personal_tasks) == 1

# def test_search_tasks(setup):
#     manager = setup
#     task1 = Task("Первая задача", "Описание первой задачи", "Работа", "2023-10-14", "Высокий")
#     task2 = Task("Вторая задача", "Описание второй задачи", "Личное", "2023-11-15", "Средний")
#     manager.add_task(task1)
#     manager.add_task(task2)
#     searched_tasks = manager.search_tasks("задача")
#     assert len(searched_tasks) == 2
#     assert searched_tasks[0].title == "Первая задача"

# if __name__ == "__main__":
#     pytest.main(["-v"])