# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return None
        def mergeklists(list1,list2):
            dummy=ListNode(0,None)
            temp=dummy
            while list1 and list2:
                if list1.val<=list2.val:
                    temp.next=list1
                    temp=list1
                    list1=list1.next
                else:
                    temp.next=list2
                    temp=list2
                    list2=list2.next
            if list1:
                temp.next=list1
            else:
                temp.next=list2
            return dummy.next
        head=lists[0]
        for i in range(1,len(lists)):
            head=mergeklists(head,lists[i])
        return head
        
            
