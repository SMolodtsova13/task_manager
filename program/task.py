class Task:
    """Класс будет представлять одну задачу с необходимыми полями."""
    def __init__(
            self,
            title: str,
            description: str = "",
            category: str = "",
            due_date: str = "",
            priority: str = "",
            status: bool = False
        ):
        self.id = None
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
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.is_completed
        }

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(
            title=data['title'],
            description=data.get('description', ""),
            category=data.get('category', ""),
            due_date=data.get('due_date', ""),
            priority=data.get('priority', "")
        )
        task.id = data['id']
        task.status = data['status']
        return task
