# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# you are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer
# the digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list
# each of the nodes contains a single digit
# you may assume the two numbers do not contain any leading zero, except the number 0 itself
# return the sum of the two numbers as a linked list

# we will start in the lowest place value, and add the values from both lists, and we will need to keep track of a carryover

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# time complexity: O(n)
# space complexity: O(n)