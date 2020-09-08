

class lecture:
    def __init__(self, subject, day, time, due_work):
        self.subject = subject
        self.day = day
        self.time = time
        self.due_work = due_work

class assignment:
    def __init__(self, subject, name, due):
        self.subject = subject
        self.name = name
        self.due = due
        self.is_done = False
    def show(self):
        print(f'''
Assignment name: {self.name}
Subject: {self.subject}
Due Date: {self.due}
''')

