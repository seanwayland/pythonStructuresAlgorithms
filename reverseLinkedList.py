# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        head = None
        while node is not None:
            tempNode = node.next
            node.next = head
            head = node
            node = tempNode
        
        return head
