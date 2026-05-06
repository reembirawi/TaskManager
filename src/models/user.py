class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.tasks = []

    def fullname(self):
        return f'{self.first} {self.last}'

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def __eq__(self, other):
        return (
                self.first == other.first and
                self.last == other.last
        )
