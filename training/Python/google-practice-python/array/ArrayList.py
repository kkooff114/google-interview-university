class ArrayList(object):
    array = []
    arrayLength = 12

    def push(self, object):
        self.array.append(self, object)

    def size(self):
        return len(self.array)

    def isEmpty(self):
        if len(self.array) == 0:
            return True

        else:
            return False


    def at(self, index):
        if index <= len(self.array) - 1:
            return self.array[index]

        else:
            raise ValueError

    def insert(self, index, item):
        self.array.insert(self, index, item)

    def delete(self, index):
        self.array.pop(index)


    def pop(self):
        self.array.pop(self)
