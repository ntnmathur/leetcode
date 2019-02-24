### [1,2,3,4,...n]  --> enter here/ exit here

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Empty List"

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(1)
s.push('two')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
print(s.pop())

