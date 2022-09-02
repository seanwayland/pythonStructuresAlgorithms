class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mylist = []
        while head.next:
            mylist.append(head.val)
            head = head.next
        mylist.append(head.val)
        return(mylist == mylist[::-1])
