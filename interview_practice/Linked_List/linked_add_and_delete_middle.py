__author__ = 'jtakwani'
#this program is to add a node in the middle of the list
#it also deletes from the given postion
#ctci 2.3

class Add_Delete_Middle():
    def __init__(self,key):
        self.value = key
        self.next = None

    def add_at_given_postion(self,position,value):
        i = 1
        previous = head = self
        while i != position and head.next != None:
            previous = head
            head = head.next
            i = i + 1
        previous.next = value
        value.next = head

    def delete_from_given_position(self,position):
        i = 1
        previous = head = self
        while i != position:
            previous = head
            head = head.next
            i = i +1
        value = head.value
        previous.next = head.next
        return value

    def print_value_at_postion(self,position):
        i = 1
        head = self
        while i != position:
            head = head.next
            i = i + 1
        return head.value

a = Add_Delete_Middle('a')
b = Add_Delete_Middle('b')
c = Add_Delete_Middle('c')
d = Add_Delete_Middle('d')

a.add_at_given_postion(1,a)
print (a.print_value_at_postion(1))
a.add_at_given_postion(2,b)
print (a.print_value_at_postion(2))
a.add_at_given_postion(3,d)
print (a.print_value_at_postion(3))
a.add_at_given_postion(4,c)
print (a.print_value_at_postion(4))

print(a.delete_from_given_position(4))
print(a.delete_from_given_position(3))
print(a.delete_from_given_position(2))
print(a.delete_from_given_position(1))


