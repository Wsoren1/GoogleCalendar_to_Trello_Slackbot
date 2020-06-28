from datetime import datetime as dt


class Task:
    def __init__(self, category, due_date, start_date, title):
        self.category = category
        self.due_date = due_date
        self.start_date = start_date
        self.title = title
        self.comments = None
        self.end_date = None
        self.completed = None

    def task_update(self):
        pass

    def task_completed(self):
        pass

    def push_task_to_board(self, board):
        pass
