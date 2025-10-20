# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find mid using fast,slow
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        prev= None
        #reversing the second half
        while mid:
            temp = mid.next
            mid.next = prev
            prev= mid
            mid = temp

        #joining
        first,second = head,prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2









