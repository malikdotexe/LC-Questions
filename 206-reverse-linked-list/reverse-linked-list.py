
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive soln

        #base case - "if not head" handles edge case when given linked list is empty and if not head.next is our base case which gets hit when we are at last node
        if not head or not head.next:
            return head
        
        newhead = self.reverseList(head.next)
        #Eg - 5 which is 4's next gets assigned 4 as its next ,in turn reversing the list
        head.next.next = head
        #Eg- Setting our 4's next to None 
        head.next = None
        #Returning head of reverse list
        return newhead


        #iterative
        # curr = head
        # prev = None
        # while curr:
        #     nextnode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextnode
        # return prev

        