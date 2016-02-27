__author__ = 'jtakwani'
#basic linked list

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

    def insert_node(self,head,value):
        while head.next is not None:
            head = head.next
        head.next = value

    def delete_node(self,head):
        while head.next:
            head = head.next
        head.next = None

    def print_linked_list(self,head):
        while head :
            print head.value
            head = head.next

#a = LinkedList('a')
#b = LinkedList('b')
#c = LinkedList('c')
#a.insert_node(a,b)
#b.insert_node(a,c)
#a.print_linked_list()
#a.delete_node(a)