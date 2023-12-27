# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = None
        fast = head
        for _ in range(n):
            fast = fast.next

        while fast is not None:
            if slow is None:
                slow = head
            else:
                slow = slow.next
            fast = fast.next
        
        if slow is None:
            return head.next
        slow.next = slow.next.next
        return head