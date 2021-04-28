'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. 

The list should be made by splicing together the nodes of the first two lists.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = [0]
Output: [0]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked List
class Solution_1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass   
                    

if __name__ == '__main__':
    
    s1 = Solution_1()
    print(s1.mergeTwoLists([1,2,4], [1,3,4]))  
    