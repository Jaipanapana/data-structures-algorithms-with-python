# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        temp=tmp=head
        count=0
        while temp.next:
            temp=temp.next
            count+=1
        count+=1
        k=k%count
        val=count-k
        i=0
        while i<val-1:
            tmp=tmp.next
            i+=1
        temp.next=head
        head=tmp.next
        tmp.next=None
        return head
        
