'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # make a copy of the node at the head
        p = head
        # while there are nodes left in the list
        while p:
            # store next node after pointer
            n = p.next
            # create a new node for our result list and set it's value to the value of the pointer
            copy = Node(p.val)
            # set the value of the current head's point to the new node created
            p.next = copy
            #
            copy.next = n
            #
            p = n

        p = head
        while p:
            n = p.next.next
            p.next.next = n.next if n else None
            p.next.random = p.random.next if p.random else None
            p = n
        return head.next if head else None