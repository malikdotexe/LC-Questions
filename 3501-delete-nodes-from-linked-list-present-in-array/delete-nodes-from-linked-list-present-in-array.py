# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)
        #deleting starting nodes if they are in nums by shifting head 
        while head and head.val in nums:
            head = head.next
        
        curr= head
        #deleting nodes in place
        while curr and curr.next: #as we are accessing curr.next.val
            if curr.next.val in nums:
                #Deleting the node by skipping and indirectly traversing too as now curr.next.val in the if condition would retrieve the new nodes value
                curr.next= curr.next.next
            else:
                curr= curr.next
        return head