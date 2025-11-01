class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0,head)
        tail = head
        nums = set(nums)
        while True:
            #selecting range
            while tail and tail.val in nums:
                tail = tail.next
            #deleting node (tail is on the node next to the node to be deleted)
            prev.next= tail
            #updating pointer
            if not tail:
                break
            
            tail = tail.next
            prev = prev.next
            
        return dummy.next