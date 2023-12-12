# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = head

        while list1 or list2:
            if list1 is None:
                val = list2.val
                list2 = list2.next
            elif list2 is None:
                val = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            
            if head is None:
                head = ListNode(val=val)
                temp = head
            else:
                temp.next = ListNode(val=val)
                temp = temp.next

        return head