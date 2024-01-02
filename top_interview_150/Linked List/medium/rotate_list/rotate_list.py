class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # find length of linked list
        n = 1
        temp = head
        while temp.next:
            temp = temp.next
            n += 1
        
        # find k
        k = k % n
        if k == 0:
            return head

        prev = None
        new_head = head
        for _ in range(n-k):
            new_head = new_head.next
            if prev is None:
                prev = head
            else:
                prev = prev.next
        
        temp.next = head
        prev.next = None

        return new_head
