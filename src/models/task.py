from models.user import User
from utils.decorators import log_call
from models.task_status import TaskStatus

class Task:
    """
        Represents a task in a task management system.
        Responsibilities:
        - Store task information (title, description, status)
        - Assign task to a user
        - Mark task as complete
    """
    count = 0
    task_list = []

    def __init__(
            self,
            title: str,
            description: str,
            status: TaskStatus = TaskStatus.OPEN,
            user: User = None
    ):
        self.title = title
        self.description = description
        self.status = status
        self.user = user
        Task.count += 1
        Task.task_list.append(self)

    @log_call
    def assign(self, assigned_user: User):
        """Assign this task to a user."""
        self.user = assigned_user
        self.status = TaskStatus.IN_PROGRESS
        assigned_user.add_task(self)
        return f'{self.title} task assigned to {self.user.fullname()}'

    @log_call
    def complete(self):
        """Mark the task as completed."""
        self.status = TaskStatus.DONE
        return f"{self.title} task is completed"

    @log_call
    def display(self):
        """Display task information."""
        if self.user is None:
            assigned = "Not assigned"
        else:
            assigned = self.user.fullname()

        return (
            f"Task title: {self.title}\n"
            f"Task description: {self.description}\n"
            f"Assigned user: {assigned}\n"
            f"Task status: {self.status}\n"
        )

    @staticmethod
    @log_call
    def filter_tasks(tasks: list, **kwargs):
        filtered_tasks = []
        for task in tasks:
            take_task = True
            for key, value in kwargs.items():
                if isinstance(value, User):
                    if not value.__eq__(task.user):
                        take_task = False
                elif getattr(task, key) != value:
                    take_task = False
                    break

            if take_task:
                filtered_tasks.append(task)
        return filtered_tasks

    @staticmethod
    @log_call
    def display_all_task():
        tasks = Task.task_list
        tasks_information = [f'{task.display()}' for task in tasks]
        print('\n'.join(tasks_information))

    @staticmethod
    @log_call
    def get_number_of_tasks():
        return Task.count

    def __str__(self):
        return self.display()

    def __eq__(self, other):
        return (
                self.title == other.title and
                self.description == other.description and
                self.user == other.user
        )
