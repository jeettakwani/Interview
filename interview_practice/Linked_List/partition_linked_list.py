__author__ = 'jtakwani'
#partitioning a linked list
#ctci 2.4

import linked_list

class Partition:
    def partition(self,ll,value):
        head = ll
        tail = ll
        while ll:
            next = ll.next
            if ll.value < value:
                ll.next = head
                head = ll
            else:
                tail.next = ll
                tail = ll
            ll = next
        tail.next = None
        while head:
            print head.value
            print "|"
            head = head.next


a = linked_list.LinkedList(4)
a.next = linked_list.LinkedList(21)
a.next.next = linked_list.LinkedList(7)
a.next.next.next =linked_list.LinkedList(9)
a.next.next.next.next = linked_list.LinkedList(1)
a.next.next.next.next.next = linked_list.LinkedList(12)

partition = Partition()
print(partition.partition(a,9))