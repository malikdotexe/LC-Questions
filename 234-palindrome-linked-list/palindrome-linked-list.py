# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #reversing the second half
        curr = slow
        prev = None
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr =temp
        
        #Checking if both half are now equal
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

