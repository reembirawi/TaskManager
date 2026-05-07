from time import time


class Timer:
    """
        Context manager for measuring execution
        time of a function or code block.
    """
    def __init__(self, func):
        self.func = func
        self.startTime = 0.0
        self.endTime = 0.0

    def __enter__(self):
        self.startTime = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.endTime = time()
        elapsed = self.endTime - self.startTime
        print(f"{self.func.__name__} took {elapsed * 1000:.5f} ms")
        return False
