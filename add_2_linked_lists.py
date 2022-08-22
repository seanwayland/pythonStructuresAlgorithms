class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        result_node = dummyHead
        carry = 0
        ## if we have values to process or a CARRY to process 
        while l1 != None or l2 != None or carry != 0:
            # store the value if it exists else add the other side to zero 
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            ## add the stored values of each column to the carry 
            columnSum = l1Val + l2Val + carry
 
            ### carry = columnSum // 10  ### FANCY PANTS VERSION OF IF STATEMENT 
            if columnSum >= 10:
                carry = 1 
            else:
                carry = 0
            ## create a new node with value of addition
            newNode = ListNode(columnSum % 10)
            ## pop it onto the result list
            result_node.next = newNode
            ### move the result head along 
            result_node = newNode
            ### move the pointers thru the given list nodes checking they exist 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
