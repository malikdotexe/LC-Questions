# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy head to simplify the addition logic
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        # Loop until both lists are processed and no carry is left
        while l1 or l2 or carry:
            # Get values from the two lists, defaulting to 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next