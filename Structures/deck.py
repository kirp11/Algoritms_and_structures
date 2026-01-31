


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        if self.head is None:
            self.head = self.tail = Node(item, None)
            self.size += 1
            return
        current_node = self.head
        node = Node(item, current_node)
        self.head = node
        self.size += 1


    def appendright(self, item):
        if self.head is None:
            self.head = self.tail = Node(item, None)
            self.size += 1
            return
        node = Node(item, None)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def insert(self, item, index):
        index_node = 0
        current_node = self.head
        while index_node != index - 1:
            current_node = current_node.next
            index_node += 1
        node = Node(item, current_node.next)
        current_node.next = node
        self.size += 1

    def popleft(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1
        else:
            print("Очередь пуста")

    def popright(self):
        if self.tail is not None:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
            self.size -= 1
        else:
            print("Очередь пуста")

    def peekleft(self):
        return self.head.value

    def peekright(self):
        return self.tail.value


    def is_empty(self):
        return True if self.head is None else False

    def get_size(self):
        return self.size

    def view_queue(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
        return


l = Deque()
print(l.get_size())
l.append(10)
l.appendright(20)
l.view_queue()
l.append(50)
l.view_queue()
print(l.get_size())
l.insert(100, 2)
l.view_queue()
l.popleft()
l.view_queue()
l.popright()
l.view_queue()
