# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        tmp=head
        prev=None
        while tmp:
            count+=1
            tmp=tmp.next
        if count==1:
            return None
        p=count-n
        if p==0:
            return head.next
        i=0
        tmp=head
        while i<p-1:
            tmp=tmp.next
            i+=1
        tmp.next=tmp.next.next
        return head

        