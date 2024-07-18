# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# you are given the beginning of a linked list head, and an integer n
# remove the nth node from the end of the list and return the beginning of the list

# to delete the nth node from the end of the list, we can find the n - 1 th node in the list and then delete the nth node using it
# to handle edge case of the nth node being the head itself, we can start by creating a dummy node before the head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next

# time complexity: O(n)
# space complexity: O(1)