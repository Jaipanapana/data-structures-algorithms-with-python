# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1

        if list1.val>list2.val:
            list1,list2=list2,list1
        head=list1
        prev1=None
        prev2=None
        c1=None
        c2=None
        while list1 and list2:
            c1=list1
            c2=list2
            if list1.val<=list2.val:
                prev1=list1
                list1=list1.next
            else:
                prev1.next=list2
                prev1=list2
                prev2=list2.next
                list2.next=list1
                list2=prev2
        if c1.next==None:
            c1.next=list2
        else:
            c2.next=list1
        return head
        

        