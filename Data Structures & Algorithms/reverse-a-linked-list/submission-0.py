# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative, use 2 ptrs prev and curr
        # time O(n) space O(1)
        prev, curr = None, head

        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        return prev