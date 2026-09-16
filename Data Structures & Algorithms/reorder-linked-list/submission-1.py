# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1) Find the Middle (Slow & Fast Pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # 2) Reverse Linked List
        prev = None
        curr = second
        while curr:
            nxt = curr.next # save next node so we don't lose it
            curr.next = prev # reverse arrow! point backward
            prev = curr # move prev one step forward
            curr = nxt # move curr one step forward 

        # 3) Merge Two Sorted Lists 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2 






        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next
        #     tail = tail.next
        
        # # what if one is empty and other isn't
        # #so we find non empty list then inset at end of result

        # if l1:
        #     tail.next = l1
        # elif l2:
        #     tail.next = l2












