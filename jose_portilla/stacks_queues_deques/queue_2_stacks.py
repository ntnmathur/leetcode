# first [1,2,3,4,5] last
# first [5,4,3,2,1] last

class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:  # if out stack is empty
            while self.in_stack: # append all in stock popped elements to out_stack
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop() # return from out stack
