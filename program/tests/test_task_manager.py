import pytest

from task import Task
from task_manager import TaskManager


@pytest.fixture
def task_manager():
    return TaskManager()


@pytest.fixture
def sample_task():
    return Task(
        id=None,
        title='Тестовая задача',
        description='Задача для проверки',
        category='Тестирование',
        due_date=Task.convert_data_from_str('31-01-2023'),
        priority='Высокий',
        status=False
    )


def test_add_task(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    assert len(task_manager.tasks) == 1
    assert added_task in task_manager.tasks


def test_find_by_id(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    found_task = task_manager.find_by_id(added_task.id)
    assert found_task == added_task


def test_update_task(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    updated_task = Task(
        id=added_task.id,
        title='Новый заголовок',
        description='Новое Описание',
        category='Личное',
        due_date=Task.convert_data_from_str('05-05-2023'),
        priority='Низкий')
    task_manager.update_task(updated_task)
    assert task_manager.find_by_id(added_task.id).title == 'Новый заголовок'


def test_complete_task(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    task_manager.complete_task(added_task.id)
    assert task_manager.find_by_id(added_task.id).is_completed


def test_search_tasks(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    result = task_manager.search_tasks('задача')
    assert len(result) == 1
    assert result[0].title == 'Тестовая задача'


def test_delete_task(task_manager, sample_task):
    added_task = task_manager.add_task(sample_task)
    task_manager.delete_task(added_task.id)
    assert len(task_manager.tasks) == 0
