# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# given the beginning of a linked list head, return true if there is a cycle in the linked list
# otherwise, return false
# there is a cycle in a linked list if there exists at least one node in the list that can be visited again by following the next pointer
# internally, index determines the index of the beginning of the cycle, if it exists
# the tail node of the list will set its next pointer to the index-th node
# if index = -1, then the tail node points to null and no cycle exists
# note: index is not given to you as a parameter

# we will use a slow and fast pointer
# the slow pointer will move forward 1 step at a time
# the fast pointer will move forward 2 steps at a time
# if a cycle exists in the linked list, then we are guaranteed that the fast pointer will catch up to the slow pointer at some point in the future
# since the distance between the two pointers is finite, and each time step will close the distance by 1 unit
# if the fast pointer reaches null (end of list), then there is no cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

# time complexity: O(n)
# space complexity: O(1)