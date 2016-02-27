__author__ = 'jtakwani'
#ti implment set of stacks
#ctci 3.3

import stack

class SetOfStacks:

    list_of_stack = []
    size = 10
    count = 0
    def push(self,value):
        if not self.list_of_stack:
            s = stack.Stack()
            s.push(value)
        if self.count != 10:
            s.push(value)
        else:
            self.list_of_stack.append(s)
            s = stack.Stack()
            s.push(value)