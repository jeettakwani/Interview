__author__ = 'jtakwani'
#adding tow numbers stored as linked list
# the numbers are stored in forward order
#ctci 2.5

import linked_list

class Add_Two_Numbers:
    def adding(self,ll1,ll2):
        #if len(ll1) == 0 and len(ll2) == 0: return 0
        #if len(ll1) == 0: return ll2
        #if len (ll2) == 0: return ll1
        list1 = []
        list2 = []
        while ll1:
            list1.append(ll1.value)
            ll1 = ll1.next
        while ll2:
            list2.append(ll2.value)
            ll2 = ll2.next
        print list1
        print list2
        answer = self.add_numbers(list1,list2)
        final = ''
        while answer:
            final = final + str(answer.pop())
        return final

    def add_numbers(self,l1,l2):
        carry = 0
        final_list = []
        while l1 or l2:
            if len(l1) != 0 and len(l2) != 0:
                num1 = l1.pop()
                num2 = l2.pop()
                sum = num1 + num2 + carry
                final_list.append(sum%10)
                carry = sum/10
            elif len(l1) != 0:
                final_list.append(l1.pop()+ carry)
                carry = 0
            elif len(l2) != 0:
                final_list.append(l2.pop() + carry)
                carry = 0
        final_list.append(carry)
        return final_list


a = linked_list.LinkedList(4)
a.next = linked_list.LinkedList(2)
a.next.next = linked_list.LinkedList(7)

b =linked_list.LinkedList(1)
b.next = linked_list.LinkedList(1)
b.next.next = linked_list.LinkedList(7)

add = Add_Two_Numbers()
print(add.adding(a,b))