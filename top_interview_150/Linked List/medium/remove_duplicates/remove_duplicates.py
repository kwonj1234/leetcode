class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        new_head = None
        new_head_pointer = None
        current_val = None
        pointer = head

        while pointer:
            if pointer.val != current_val:
                if (pointer.next and pointer.val != pointer.next.val) \
                or pointer.next is None:
                    if new_head is None:
                        new_head = pointer
                        new_head_pointer = new_head
                    else:
                        new_head_pointer.next = pointer
                        new_head_pointer = new_head_pointer.next


            current_val = pointer.val
            pointer = pointer.next

        if new_head_pointer is not None:
            new_head_pointer.next = None

        return new_head