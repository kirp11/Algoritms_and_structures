

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.top = None
        self.size = 0

    def enqueue(self, item):
        if self.top is None:
            self.top = Node(item, None)
            self.size += 1
            return
        current_node = self.top
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(item, None)
        self.size += 1

    def dequeue(self):
        if self.top is not None:
            self.top = self.top.next
            self.size -= 1
        else:
            print("Очередь пуста")


    def peek(self):
        return self.top.value


    def is_empty(self):
        return True if self.top is None else False

    def get_size(self):
        return self.size

    def view_queue(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
        return


l = Queue()
print(l.get_size())
l.dequeue()
l.enqueue(10)
print(l.get_size())
l.dequeue()
l.view_queue()
l.enqueue(20)
l.enqueue(40)
print(l.peek())
l.enqueue(60)
l.enqueue(900)
l.view_queue()
l.dequeue()
print(l.peek())
l.view_queue()
l.dequeue()
print(l.get_size())
print()


print("__________")
l.view_queue()
print(l.get_size())