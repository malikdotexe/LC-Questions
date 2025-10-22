# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #creating dummy node for ease
        dummy = ListNode()
        #curr for iterating
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            #defaulting to 0 if any number is any digits less than other
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            
            total = val1+val2+carry
            #We update carry value later as the carry from previous sum is added to the next place
            carry = total//10
            
            curr.next = ListNode(total%10)
            
            #updating pointers  
            if l1:
                l1 = l1.next
            if l2:
                l2 =l2.next 
            curr = curr.next

        return dummy.next



