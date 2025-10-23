# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Edge Case
        if not lists or len(lists)==0:
            return None
        #Run till length of lists reduces to 1
        while len(lists)>1:

            mergedlists = []
            #jumping by 2 as we are pairing 2 linked lists each iteration
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1<len(lists) else None
                mergedlists.append(self.merge2list(list1,list2))
            # Replace lists with merged results, reducing the number of lists each iteration, eventually breaking the loop
            lists = mergedlists
        return lists[0]



    
    def merge2list(self,list1,list2):
        res = dummy = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                dummy.next = list1
                list1 =list1.next
            else:
                dummy.next =list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next= list2
        return res.next

