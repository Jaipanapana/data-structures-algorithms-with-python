# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1=0
        head1=l1
        head2=l2
        while l1.next:
            count1+=1
            l1=l1.next
        count2=0
        while l2.next:
            count2+=1
            l2=l2.next
        if count1>count2:
            val=count1-count2
            while val!=0:
                node=ListNode(0,None)
                l2.next=node
                l2=l2.next
                val-=1
        if count1<count2:
            val=count2-count1
            while val!=0:
                node=ListNode(0,None)
                l1.next=node
                l1=l1.next
                val-=1
        tmp=ListNode(0,None)
        head=tmp
        c=0
        while head1:
            value=(head1.val+head2.val+c)%10
            c=(head1.val+head2.val+c)//10
            node=ListNode(value,None)
            tmp.next=node
            head1=head1.next
            head2=head2.next
            tmp=tmp.next
        if c>0:
            node=ListNode(c,None)
            tmp.next=node
        return head.next