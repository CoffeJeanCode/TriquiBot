class BiArray:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = self.width * self.height
        self.length = 0
        self.data = [None] * self.size

    def __str__(self):
        return f"BiArray({self.data})"

    def index(self, row, col):
        return row * self.width + col

    def rawGet(self, index):
        return self.data[index]
        
    def get(self, row, col):
        return self.data[self.index(row, col)]

    def rawSet(self, index, value):
        self.data[index] = value
        return self 

    def set(self, row, col, value):
        self.data[self.index(row, col)] = value
        self.length += 1
        return self

    def copy(self):
        copied = BiArray(self.width, self.height)
        copied.data = self.data.copy()
        return copied

    def fill(self, value):
        self.data = [value] * self.size
        self.length = self.size
        return self

    def push(self, value):
        if self.length < self.size:
            self.data[self.length] = value
            self.length += 1
            return self
        else:
            raise IndexError("BiArray is full, cannot push more elements")

    def append(self, value):
        if self.length < self.size:
            self.data[self.length] = value
            self.length += 1
            self.width += 1
            self.size += self.height
        else:
            self.width += 1
            self.size += self.height
            self.data += [value] * self.height
            self.length += self.height

    def pop(self):
        if self.length > 0:
            self.length -= 1            
            return self.data.pop()
        else:
            raise IndexError("BiArray is empty, cannot pop more elements")
            
    def isFull(self):
      return self.length == self.size