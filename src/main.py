from models.task import Task
from models.user import User
from utils.logger import setup_logger
from models.task_status import TaskStatus

setup_logger()

if __name__ == "__main__":
    user1 = User("Reem", "Birawi")
    user2 = User("Ahmad", "Birawi")

    task1 = Task("Writing an Essay", "Write an essay about clean code")
    task2 = Task("Writing an Essay", "Write an essay about clean code")
    task3 = Task("Push code to github", "Add __eq__ to Task class")

    print(task1.display())
    print(task1.assign(user1))
    print(task1.display())
    print(task1.complete())
    print(task1.display())

    task2.assign(user1)
    task3.assign(user2)

    print(f'task1 == task2 ? {task1.__eq__(task2)}')
    print(f'task1 == task3  ? {task1.__eq__(task3)}')

    print(f'Number of tasks: {task1.get_number_of_tasks()}')

    task1.display_all_task()
    filtered_task_list = task2.filter_tasks(Task.task_list, user=user1, status=TaskStatus.DONE)

    print("number of tasks in filtered task list:", len(filtered_task_list))
    for task in filtered_task_list:
        print(task.display())
