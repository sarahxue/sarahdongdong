"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two passes
        # time O(n) space O(n)

        nodes = {None : None}

        #copy nodes
        cur = head
        while cur:
            copy = Node(cur.val)
            nodes[cur] = copy
            cur = cur.next
    
        #set connections
        cur = head
        while cur:
            copy = nodes[cur]
            copy.next = nodes[cur.next]
            copy.random = nodes[cur.random]
            cur = cur.next
            
        return nodes[head]