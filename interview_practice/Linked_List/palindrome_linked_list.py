__author__ = 'jtakwani'
# ctci 2.7
#if a linked list is palindrom

import linked_list
class Palindrom_LinkedList:

    def is_palindrome(self,ll):
        l = []
        while ll:
            l.append(ll.value)
            ll = ll.next
        return self.check_palindrome(l)

    def check_palindrome(self,l):
        j = len(l)-1
        for i in range (len(l)/2):
            if l[i] == l[j]:
                j = j - 1
            else:
                return False
        return True

a = linked_list.LinkedList('e')
a.next = linked_list.LinkedList('v')
a.next.next = linked_list.LinkedList('e')
#a.next.next.next =linked_list.LinkedList('b')
#a.next.next.next.next = linked_list.LinkedList('a')
#a.next.next.next.next.next = linked_list.LinkedList('c')

palindrome = Palindrom_LinkedList()
print(palindrome.is_palindrome(a))
