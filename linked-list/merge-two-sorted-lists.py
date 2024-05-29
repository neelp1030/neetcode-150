# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# you are given the heads of two sorted linked lists list1 and list2
# merge the two lists into one sorted linked list and return the head of the new sorted linked list
# the new list should be made up of nodes from list1 and list2

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]

# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]

# Example 3:
# Input: list1 = [], list2 = []
# Output: []

# we'll maintain pointers to the remaining portions of each list
# we'll compare the two values at each iteration, and add the node that is the minimum of the two, incrementing that pointer and moving on
# if at any point, one of the two remaining lists becomes empty, then we can append the remainder of the other list to our result and return

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempRoot = traverseNode = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                traverseNode.next = list1
                list1 = list1.next
            else:
                traverseNode.next = list2
                list2 = list2.next
            
            traverseNode = traverseNode.next
        
        if list1:
            traverseNode.next = list1
        if list2:
            traverseNode.next = list2
        
        return tempRoot.next

# time complexity: O(n)
# space complexity: O(1)