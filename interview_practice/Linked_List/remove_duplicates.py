__author__ = 'jtakwani'
#removing duplicates from unsorted ll
#2.1 CTCI

import linked_list
class RemoveDuplicates:
    def remove_duplicates(self,a):
        s = set()
        head = a
        #print(a.next.value)
        while a:
            if a.value not in s:
                s.add(a.value)
                a = a.next
                #print s
                continue
            else:
                print a.value
                self.remove_value(head,a.value)
                break



    def remove_value(self,l,value):
        previous = head = l
        l=l.next
        while l:
            if l.value == value:
                previous.next = l.next
                l = l.next;
                previous = previous.next
            else:
                l = l.next;
                previous = previous.next
        return (a.print_linked_list(a))

a = linked_list.LinkedList('a')
a.next = linked_list.LinkedList('b')
a.next.next = linked_list.LinkedList('c')
a.next.next.next =linked_list.LinkedList('d')
a.next.next.next.next = linked_list.LinkedList('d')
a.print_linked_list(a)

rd = RemoveDuplicates()
print(rd.remove_duplicates(a))


