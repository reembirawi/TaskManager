from user import User


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
            status: str = "open",
            user: User = None
    ):
        self.title = title
        self.description = description
        self.status = status
        self.user = user
        Task.count += 1
        Task.task_list.append(self)

    def assign(self, assigned_user: User):
        """Assign this task to a user."""
        self.user = assigned_user
        self.status = "in-progress"
        assigned_user.add_task(self)
        return f'{self.title} task assigned to {self.user.fullname()}'

    def complete(self):
        """Mark the task as completed."""
        self.status = "done"
        return f"{self.title} task is completed"

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
    def display_all_task():
        for task in Task.task_list:
            print(task.display())

    @staticmethod
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
