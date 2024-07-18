# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# you are given the head of a singly linked list
# the positions of a linked list of length = 7 for example, can initially be represented as:
# [0,1,2,3,4,5,6]
# reorder the nodes of the linked list to be in the following order:
# [0,6,1,5,2,4,3]
# notice that in the general case for a list of length = n, the nodes are reordered to be in the following order:
# [0,n-1,1,n-2,2,n-3,...]
# you may not modify the values in the list's nodes, but instead you must reorder the nodes themselves

# Example 1:
# Input: head = [2,4,6,8]
# Output: [2,8,4,6]

# Example 2:
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]

class Solution:
    def reorderList(self, head: ListNode) -> None:

        # find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # at this point, for odd length list, slow is pointing to middle node, and for even length list, slow is pointing to (n/2)th node

        # reverse second half and simultaneously disconnect the two halves of the list
        prev, curr, slow.next = None, slow.next, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
# time complexity: O(n)
# space complexity: O(1)