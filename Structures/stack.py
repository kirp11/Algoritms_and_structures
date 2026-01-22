

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    def pop(self):
        if self.top is not None:
            self.top = self.top.next
            self.size -= 1
        else:
            raise IndexError("Стэк пуст")


    def peek(self):
        return self.top.value


    def is_empty(self):
        return True if self.top is None else False

    def get_size(self):
        return self.size

    def view_stack(self):
        current_node = self.top
        while current_node is not None :
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
        return


l = Stack()
print(l.get_size())
l.push(10)
print(l.get_size())
l.push(20)
l.push(40)
print(l.peek())
l.push(60)
l.push(900)
l.view_stack()
print(l.get_size())
print()


print("__________")
l.pop()
l.view_stack()
print(l.get_size())
