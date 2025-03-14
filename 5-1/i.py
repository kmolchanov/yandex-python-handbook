class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        item = None
        if not self.is_empty():
            item, *self.queue = self.queue
        return item

    def is_empty(self):
        return self.queue == []
