from datetime import date, datetime


DATE_PATTERN_DATA = '%d-%m-%Y'
DATE_PATTERN_RU = 'ДД-ММ-ГГГГ'

class Task:
    """Класс будет представлять одну задачу с необходимыми полями."""
    def __init__(
            self,
            id: int | None,
            title: str,
            description: str = "",
            category: str = "",
            due_date: date | None = None,
            priority: str = "",
            status: bool = False
        ):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    @property
    def is_completed(self) -> bool:
        return self.status

    def mark_as_completed(self):
        self.status = True

    def to_dict(self) -> dict:
        date_str = None
        if self.due_date:
            date_str = self.due_date.strftime(DATE_PATTERN_DATA)

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': date_str,
            'priority': self.priority,
            'status': self.is_completed
        }

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(
            id=data['id'],
            title=data['title'],
            description=data.get('description', ""),
            category=data.get('category', ""),
            due_date=Task.convert_data_from_str(data.get('due_date', None)),
            priority=data.get('priority', ""),
            status=data.get('status', False),
        )
        return task
    
    @staticmethod
    def convert_data_from_str(date_str: str) -> date | None:
        if not date_str or len(date_str) == 0:
            return None
        return datetime.strptime(date_str, DATE_PATTERN_DATA).date()
