



class HashTable():
    def __init__(self):
        self.__count = 0
        self.__size = 100
        self.__memory = [None] * self.__size


    def add(self, key, item):
        hash = self.__hash(key)
        if self.__memory[hash] is not None:
            pass

        self.__memory[hash] = item

    def get(self, key):
        hash = self.__hash(key)
        if self.__memory[hash] is None:
            raise ValueError("не найден")
        return self.__memory[hash]

    def clear(self):
        self.__memory.clear()
        self.__memory = [None] * self.__size

    def __hash(self, key):
        index = hash(key) % self.__size
        return index

    def get_size(self):
        return self.__count

table = HashTable()
table.add("z", 2)
table.add("n", 5)
print(table.get("n"))
print(table)