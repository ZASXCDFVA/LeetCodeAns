# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def extractNumber(self, node: ListNode) -> int:
        if node.next is not None:
            return self.extractNumber(node.next) * 10 + node.val

        return node.val

    def storeNumber(self, value: int) -> ListNode:
        if value // 10 == 0:
            return ListNode(value, None)

        return ListNode(value % 10, self.storeNumber(value // 10))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1: int = self.extractNumber(l1)
        num2: int = self.extractNumber(l2)

        sum = num1 + num2

        return self.storeNumber(sum)


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()

    result = solution.addTwoNumbers(l1, l2)

    print(solution.extractNumber(result))