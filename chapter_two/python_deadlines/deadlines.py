id_tool = 0

class Deadline:
    def __init__(self, task, expiry, priority):
        self.task = task
        self.expiry = expiry
        self.priority = priority
        global id_tool
        id_tool += 1
        self.id = id_tool

    def upcoming_list(self):
        pass
    def priority_list(self):
        pass
    def alert_list(self):
        pass
    def archive_list(self):
        pass

class Agenda:
    def __init__(self):
        self.deadlines = []
    def new_deadline(self, task, expiry, priority):
        pass
    def edit_deadline(self, id, task, expiry, priority):
        pass
    def mark_deadline(self):
        pass
    def purge_deadline(self):
        pass
    def _find_deadline(self):
        pass