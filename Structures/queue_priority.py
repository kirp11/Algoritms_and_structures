


class NodeWithPriority:
    def __init__(self, value, priority, next=None):
        self.value = value
        self.priority = priority
        self.next = next

class QueuePriority:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, item, priority):
        new_node = NodeWithPriority(item, priority, None)
        if self.head is None or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.priority >= priority:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.size += 1

    def extract_max(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1
        else:
            print("Очередь пуста")

    def extract_min(self):
        if self.head is not None:
            current_node = self.head
            min_priority = current_node.priority
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.priority < min_priority:
                    min_priority = current_node.priority
            current_node = self.head
            while current_node.next.priority > min_priority:
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.size -= 1
        else:
            print("Очередь пуста")


    def peek_max_priority(self):
        return self.head.value

    def peek_min_priority(self):
        current_node = self.head
        min_priority = current_node.priority
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.priority < min_priority:
                min_priority = current_node.priority
        current_node = self.head
        while current_node.priority != min_priority:
            current_node = current_node.next
        return current_node.value


    def is_empty(self):
        return True if self.head is None else False

    def get_size(self):
        return self.size

    def view_queue_priority(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, "p:", current_node.priority, end="    ")
            current_node = current_node.next
        print()
        return


l = QueuePriority()
print(l.get_size())
l.insert(10,2)
l.insert(12,1)
print(l.get_size())
l.insert(8,3)
l.insert(6,1)
l.insert(2,2)
l.insert(15,1)
l.insert(20,3)
l.insert(25,3)

l.view_queue_priority()
print(l.peek_max_priority())
print(l.peek_min_priority())
l.extract_max()
l.view_queue_priority()
l.extract_min()
l.view_queue_priority()



print("__________")
print(l.get_size())