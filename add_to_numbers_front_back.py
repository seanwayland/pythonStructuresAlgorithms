# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

          l1_copy = l1
          l2_copy = l2
          stack_one = []
          stack_two = []
          while(l1):
                stack_one.append(l1.val)
                l1 = l1.next
          while(l2):
                stack_two.append(l2.val)
                l2 = l2.next
          print(stack_one)
          print(stack_two)
          string_result = ""
          carry = 0
          tester = 9 
          head = ListNode()
          my_bool = 0
          
          
          while(stack_one != [] or stack_two != [] or carry!=0):
              if(stack_one != []):
                s1 = stack_one.pop()
              else:
                s1 = 0
              if(stack_two != []):
                s2 = stack_two.pop()
              else:
                s2 = 0
              if(s1 + s2 + carry > 9):
                result_sum= str(s1 + s2 + carry - 10)
                carry = 1
              else:
                result_sum = str(s1 + s2 + carry) 
                carry = 0 
              print("result_sum: ", result_sum)
              
              new_node = ListNode(result_sum)
              if my_bool is not 0:
                new_node.next = head
              else:
                new_node.next = None
                my_bool = 1
              head = new_node

              print("s1: ", s1)
              print("s2: ", s2)
              print("carry: ", carry)
              print("res: ", string_result)
          return(head)
              
