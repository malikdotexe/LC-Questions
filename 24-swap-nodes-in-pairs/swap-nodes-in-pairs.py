# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #dummy node pointing to the head
        dummy= ListNode(0,head)
        prev,curr = dummy,head
        while curr and curr.next:
            #saving temps
            third = curr.next.next
            second = curr.next
            #new pointers
            second.next = curr
            prev.next = second
            curr.next = third
            #updating pointers
            prev = curr
            curr = third
        return dummy.next
    