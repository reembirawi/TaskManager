from enum import Enum


class TaskStatus(Enum):
    OPEN = "not-started"
    IN_PROGRESS = "in-progress"
    DONE = "done"
