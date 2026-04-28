from task import Task
from user import User

if __name__ == "__main__":
    user = User("Reem", "Birawi")
    task1 = Task("Writing an Essay", "Write an essay about clean code")
    print(task1.display())
    print(task1.assign(user))
    print(task1.display())
    print(task1.complete())
    print(task1.display())
