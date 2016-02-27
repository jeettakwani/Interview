__author__ = 'jtakwani'
#this is to implement the basic functionality
#of stack with one additional operation
#to find min in o(1) time
#ctci 3.2

class Stack:
    stack_list = []
    min = 0
    def push(self,value):
        if not self.stack_list:
            self.min = value
            self.stack_list.append(value)
        else:
            if value < self.min:
                self.min = value
            self.stack_list.append(value)
    def pop(self):
        return self.stack_list.pop()

    def minimum(self):
        return self.min

    def top(self):
        return self.stack_list[len(self.stack_list)-1]


s = Stack()
s.push(1)
s.push(23)
s.push(20)
s.push(-1)
s.push(100)

print s.minimum()
print s.top()