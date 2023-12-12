# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry_over = 0

        while l1 or l2:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            temp_sum = l2_val + l1_val + carry_over

            remainder = temp_sum % 10
            carry_over = temp_sum // 10

            if head is not None:
                temp.next = ListNode(val=remainder)
                temp = temp.next
            else:
                head = ListNode(val=remainder)
                temp = head

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry_over:
            temp.next = ListNode(val=carry_over)
        
        return head