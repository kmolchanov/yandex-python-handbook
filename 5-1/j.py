class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        item = self.head.item
        self.head = self.head.next
        return item

    def is_empty(self):
        return self.head is None
