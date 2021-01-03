from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node: Optional[ListNode] = head

        while node != None:
            while node.next != None and node.val == node.next.val:
                node.next = node.next.next

            node = node.next

        return head


