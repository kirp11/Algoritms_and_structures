

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def append_back(self, item):
        if self.head is None:
            node = Node(item, None)
            self.head = self.last = node
            self.size +=1
            return
        new_last = Node(item, None)
        self.last.next = new_last
        self.last = new_last
        self.size += 1


    def pop(self):
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        self.size -= 1
        return

    def insert(self, item, index):
        index_node = 0
        current_node = self.head
        while index_node != index - 1:
            current_node = current_node.next
            index_node += 1
        node = Node(item, current_node.next)
        current_node.next = node
        self.size += 1


    def search(self, item):
        index = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value == item:
                return index
            current_node = current_node.next
            index += 1
        return f"такого значения нет"

    def remove(self, index):
        index_node = 0
        current_node = self.head
        while index_node != index - 1:
            current_node = current_node.next
            index_node += 1
        remove_element = current_node.next
        current_node.next = current_node.next.next
        self.size -= 1
        return remove_element.value if remove_element.value is not None else f"такого значения нет"

    def get(self, index):
        index_node = 0
        current_node = self.head
        while index_node != index:
            current_node = current_node.next
            index_node += 1

        return f"под индексом {index} лежит значение {current_node.value}"

    def set(self, index, item):
        index_node = 0
        current_node = self.head
        while index_node != index:
            current_node = current_node.next
            index_node += 1
        current_node.value = item
        return

    def is_empty(self):
        return True if self.head is None else False

    def get_size(self):
        return self.size

    def view_list(self):
        index_node = 0
        current_node = self.head
        while current_node is not None :
            print(current_node.value, end=" ")
            current_node = current_node.next
            index_node += 1
        print()
        return


l = Linked_list()
print(l.get_size())
l.append_back(10)
print(l.get_size())
l.append_back(20)
l.append_back(40)
l.append_back(60)
l.append_back(900)
l.view_list()
l.insert(500,2)
l.view_list()
print()
print(l.search(910))
l.remove(4)
l.view_list()
print(l.get_size())
print(l.get(2))
print(l.set(2, 810))
l.view_list()

print("__________")
l.pop()
l.view_list()
print(l.get_size())
